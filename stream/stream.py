import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model_filename = 'model.pkl'
loaded_model = joblib.load(model_filename)

# Create a simple form to collect input
st.title("Heart Disease Risk Prediction")

age = st.number_input("Enter your age", min_value=1)
male = st.selectbox("Select your gender", [0, 1], format_func=lambda x: 'Male' if x == 1 else 'Female')
currentSmoker = st.selectbox("Do you smoke?", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
cigs_per_day = st.number_input("Cigarettes per day", min_value=0)
BPMeds = st.selectbox("Are you on BP medication?", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
prevalent_stroke = st.selectbox("Have you had a stroke?", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
prevalent_hyp = st.selectbox("Do you have hypertension?", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
diabetes = st.selectbox("Do you have diabetes?", [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
totChol = st.number_input("Enter your total cholesterol level", min_value=0)
sysBP = st.number_input("Enter your systolic blood pressure", min_value=0)
diaBP = st.number_input("Enter your diastolic blood pressure", min_value=0)
BMI = st.number_input("Enter your BMI", min_value=0)
heart_rate = st.number_input("Enter your heart rate", min_value=0)
glucose = st.number_input("Enter your glucose level", min_value=0)

# Collect the user input in a DataFrame

    
user_data = pd.DataFrame({
    'male': [male],'age': [age],  'currentSmoker': [currentSmoker], 'cigsPerDay': [cigs_per_day],
    'BPMeds': [BPMeds], 'prevalentStroke': [prevalent_stroke], 'prevalentHyp': [prevalent_hyp],
    'diabetes': [diabetes], 'totChol': [totChol], 'sysBP': [sysBP], 'diaBP': [diaBP],
    'BMI': [BMI], 'heartRate': [heart_rate], 'glucose': [glucose]

})
# Predict the result
if st.button("Predict"):
    prediction = loaded_model.predict(user_data)
    if prediction[0] == 1:
        st.write("The model predicts that you are at risk of coronary heart disease in the next 10 years.")
    else:
        st.write("The model predicts that you are NOT at risk of coronary heart disease in the next 10 years.")
