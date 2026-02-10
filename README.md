# Credit Risk Prediction App

A simple Machine Learning project that predicts the probability of loan default based on borrower financial details.  
Includes data analysis, logistic regression model training, and a Streamlit web app for live predictions.

---

# Credit Risk Prediction App

🚀 **Live App:** [Credit Risk Prediction App](/https://github.com/Ritesh0802/credit-risk-default-prediction)

A simple Machine Learning project that predicts the probability of loan default...

---

## Project Overview

This project analyzes credit risk using financial and credit-related features such as:

- Credit lines outstanding  
- Loan amount and total debt  
- Income level  
- Employment stability  
- Credit score  
- Debt-to-income ratio  

The trained Logistic Regression model predicts whether a borrower is likely to default on a loan.

---

## Tech Stack

- Python  
- Pandas / NumPy  
- Scikit-learn  
- Matplotlib / Seaborn (EDA)  
- Streamlit (Deployment)

---

## Project Structure

```
Credit-Risk-Prediction/
│
├── app.py                      # Streamlit prediction app
├── credit_model.pkl            # Trained ML model
├── credit_risk_analysis.ipynb  # Data analysis + model training
├── Task 3 Loan_Data.csv        # Dataset
├── requirements.txt            # Dependencies
└── README.md
```

---

## How to Run Locally

### 1. Clone repository

```
git clone https://github.com/YOUR_USERNAME/Credit-Risk-Prediction.git
cd Credit-Risk-Prediction
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
python -m streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## Model Details

- Algorithm: Logistic Regression  
- Target Variable: Loan Default (0 = No, 1 = Yes)  
- Evaluation Metrics:
  - Accuracy
  - Confusion Matrix
  - Classification Report
  - Probability Prediction

---

## Key Insights from Analysis

- Higher debt-to-income ratio strongly correlates with default risk.  
- Lower credit score increases probability of default.  
- Income alone is not a strong predictor.  
- Employment stability contributes to risk assessment.

---

## Disclaimer

This project is for educational and portfolio purposes only.  
It is not intended for real financial decision-making.

---

## Future Improvements

- Feature scaling and advanced ML models  
- Better UI/UX improvements in Streamlit  
- Explainable AI integration (SHAP or feature importance)  
- Automated deployment pipeline

---

## Author

**Ritesh Prasad**  
Electronics & Communication Graduate  
Aspiring Data Analyst / ML Enthusiast


