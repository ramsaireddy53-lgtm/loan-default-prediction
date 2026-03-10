import streamlit as st
import pickle
import numpy as np
import os

# Load model
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
model_path = os.path.join(BASE_DIR, "model", "model.pkl")
model = pickle.load(open(model_path, "rb"))

st.title("🏦 Loan Approval Prediction System")

st.write("Fill in the applicant details below to predict loan approval.")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    applicant_income = st.number_input("Applicant Income", min_value=0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
    loan_amount = st.number_input("Loan Amount", min_value=0)
    loan_term = st.number_input("Loan Amount Term", min_value=0)

with col2:
    credit_history = st.selectbox("Credit History", [1,0])
    gender = st.selectbox("Gender", ["Male","Female"])
    married = st.selectbox("Married", ["Yes","No"])
    property_area = st.selectbox("Property Area", ["Urban","Semiurban","Rural"])

# Prediction button
if st.button("Predict Loan Status"):

    # Convert categorical values
    gender_male = 1 if gender == "Male" else 0
    married_yes = 1 if married == "Yes" else 0
    property_semiurban = 1 if property_area == "Semiurban" else 0
    property_urban = 1 if property_area == "Urban" else 0

    features = np.array([[ 
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        gender_male,
        married_yes,
        0,0,0,      # Dependents
        0,          # Education
        0,          # Self employed
        property_semiurban,
        property_urban
    ]])

    prediction = model.predict(features)

    prob = model.predict_proba(features)
    approval_prob = prob[0][1] * 100

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

    st.write(f"Approval Probability: {approval_prob:.2f}%")    