import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("credit_model.pkl", "rb"))

st.set_page_config(page_title="Credit Risk Prediction", layout="centered")

st.title("Credit Risk Prediction App")

st.markdown("""
This app predicts the probability of loan default using a Logistic Regression model.
Enter borrower financial details below.
""")

# ---- Inputs ----
credit_lines = st.number_input("Credit Lines Outstanding", value=1)
loan_amt = st.number_input("Loan Amount Outstanding", value=5000.0)
total_debt = st.number_input("Total Debt Outstanding", value=3000.0)
income = st.number_input("Income", value=50000.0)
years_emp = st.number_input("Years Employed", value=3)
fico = st.number_input("FICO Score", value=650)

# ---- Validation ----
if income <= 0:
    st.warning("Income must be greater than zero.")
    st.stop()

debt_to_income = total_debt / income

# ---- Prediction ----
if st.button("Predict Risk"):

    features = np.array([[
        credit_lines,
        loan_amt,
        total_debt,
        income,
        years_emp,
        fico,
        debt_to_income
    ]])

    probability = model.predict_proba(features)[0][1]

    st.subheader(f"Default Probability: {probability:.2%}")

    st.write("Model Coefficients:", model.coef_)

    if probability > 0.5:
        st.error("High Default Risk")
    else:
        st.success("Low Default Risk")

st.markdown("""
---
**Model Inputs Used:**
- Credit lines outstanding  
- Loan amount & total debt  
- Income level  
- Employment stability  
- Credit score  
- Debt-to-income ratio  

This is a basic demonstration ML project, not a real financial advisory tool.
""")
