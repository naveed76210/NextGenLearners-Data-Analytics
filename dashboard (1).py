
import streamlit as st
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Internship Performance Dashboard",
    layout="wide"
)

conn = sqlite3.connect("nextgen.db")

applicants = pd.read_sql("SELECT * FROM applicants", conn)
interns = pd.read_sql("SELECT * FROM interns", conn)
hackathon_scores = pd.read_sql("SELECT * FROM hackathon_scores", conn)

conn.close()

st.title("Internship Performance Dashboard")
st.write("Program Performance Overview")

domains = ["All"] + sorted(applicants["domain"].unique().tolist())

selected_domain = st.selectbox("Select Domain", domains)

if selected_domain == "All":
    filtered_applicants = applicants
    filtered_interns = interns
    filtered_scores = hackathon_scores
else:
    filtered_applicants = applicants[applicants["domain"] == selected_domain]
    filtered_interns = interns[interns["domain"] == selected_domain]
    filtered_scores = hackathon_scores[hackathon_scores["domain"] == selected_domain]

total_applicants = len(filtered_applicants)
total_interns = len(filtered_interns)

completed = filtered_interns[
    filtered_interns["completion_status"] == "Completed"
]

completion_rate = (
    len(completed) / total_applicants * 100
    if total_applicants > 0 else 0
)

average_score = (
    filtered_scores["score"].mean()
    if not filtered_scores.empty else 0
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Applicants", total_applicants)
col2.metric("Total Interns", total_interns)
col3.metric("Completion Rate", f"{completion_rate:.1f}%")
col4.metric("Average Score", f"{average_score:.1f}")

st.subheader("Completion Rate by Domain")

completion_data = (
    interns[interns["completion_status"] == "Completed"]
    .groupby("domain").size()
    / applicants.groupby("domain").size()
    * 100
).fillna(0)

if selected_domain == "All":
    st.bar_chart(completion_data)
else:
    st.bar_chart(completion_data.reindex([selected_domain]).dropna())

st.subheader("Average Hackathon Score by Domain")

score_data = hackathon_scores.groupby("domain")["score"].mean()

if selected_domain == "All":
    st.bar_chart(score_data)
else:
    st.bar_chart(score_data.reindex([selected_domain]).dropna())

st.subheader("Top 10 Leaderboard")

leaderboard = pd.merge(
    filtered_interns,
    filtered_scores,
    on=["intern_id", "domain"],
    how="inner"
)

leaderboard = leaderboard[
    ["intern_id", "domain", "completion_status", "score"]
].sort_values("score", ascending=False).head(10)

st.dataframe(leaderboard, use_container_width=True)
