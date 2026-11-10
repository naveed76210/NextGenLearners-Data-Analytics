Week 4 Capstone: Internship Selection Outcome Prediction

Project Overview

This project explores internship selection outcome prediction using Python, Pandas, and Machine Learning.

The project combines data preparation, feature engineering, model training, evaluation, and interpretation.

Objective

To build and evaluate a Logistic Regression model that predicts internship selection outcomes using applicant domain information and additional simulated features.

Dataset

- Original dataset: 58 applicants
- Original columns: 7
- Applicants excluded due to Under Review status: 15
- Final modeling dataset: 43 applicants

Simulated Features

The following features were generated using random values:

- Number of skills listed
- Portfolio availability
- Prior hackathon participation
- Statement quality score

Important: These four features are simulated and do not represent actual applicant history.

Tools and Libraries

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab

Methodology

1. Loaded and inspected the cleaned applicant dataset.
2. Generated four simulated features using a fixed random seed.
3. Excluded applicants whose status was Under Review.
4. Created a binary target variable:
   - Approved = Selected (1)
   - Pending or Rejected = Not Selected (0)
5. Converted Yes/No features into numeric values.
6. Applied one-hot encoding to applicant domains.
7. Excluded personal identifiers from model features.
8. Split the data into training and testing sets.
9. Trained a Logistic Regression model.
10. Evaluated the model using accuracy, precision, recall, and a confusion matrix.
11. Examined Logistic Regression coefficients.

Model Evaluation

The model was evaluated on a test set of 9 applicants.

Metric| Result
Accuracy| 33.3%
Precision| 0.00
Recall| 0.00

The confusion matrix showed that the model correctly identified three Not Selected applicants but did not correctly identify any Selected applicants.

Key Findings

The model produced positive coefficients for portfolio availability, prior hackathon participation, and statement quality score.

These findings describe the behavior of this model using simulated features. They do not establish actual factors affecting internship selection.

Limitations

- The dataset contains only 58 original applicants.
- Four features were simulated rather than collected from real applicants.
- The test set contains only 9 applicants.
- Model performance was weak.
- Results may change with a different dataset or split.
- The model is not suitable for real internship selection decisions.

Recommendation

Future work should use a larger dataset with verified applicant information and actual selection outcomes. The model should be evaluated on more data and checked for fairness before any practical use.

Human review should remain central to internship selection.

How to Run

1. Open the project notebook in Google Colab.
2. Upload the cleaned applicant CSV file.
3. Run the notebook cells from top to bottom.
4. Review the model evaluation and limitations.

Project Deliverables

- Week 4 Capstone notebook
- Executive Summary
- Model evaluation
- Feature interpretation
- README documentation

Author

Naveed Tariq

Project Note

This is an educational capstone project. The model is experimental and should not be used to make real applicant selection decisions.
