import streamlit as st
import pickle
import numpy as np
import os

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
model = pickle.load(open(model_path, "rb"))# Load model

st.title("Loan Default Prediction System")# Streamlit app title

st.write("Enter applicant details below:")

# Input fields
income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.number_input("Credit History (0 or 1)")
loan_term = st.number_input("Loan Amount Term")

# Prediction button
if st.button("Predict Loan Status"):

    features = features = np.array([[ 
    income,        # ApplicantIncome
    0,             # CoapplicantIncome
    loan_amount,   # LoanAmount
    loan_term,     # Loan_Amount_Term
    credit_history,# Credit_History
    1,             # Gender_Male
    1,             # Married_Yes
    0,             # Dependents_1
    0,             # Dependents_2
    0,             # Dependents_3+
    0,             # Education_Not Graduate
    0,             # Self_Employed_Yes
    0,             # Property_Area_Semiurban
    1              # Property_Area_Urban
]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")