import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load saved model and scaler
with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("💓 Heart Disease Risk Prediction App")

# Input form
age = st.number_input("Age", 20, 100)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting BP (trestbps)", 90, 200)
chol = st.number_input("Cholesterol (chol)", 100, 400)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
thalach = st.number_input("Max Heart Rate (thalach)", 60, 220)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression (oldpeak)", 0.0, 6.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST Segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of Vessels Colored (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Prepare input for prediction
features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach,
                      exang, oldpeak, slope, ca, thal]])
scaled_features = scaler.transform(features)

# Predict
prediction = model.predict(scaled_features)[0]
probability = model.predict_proba(scaled_features)[0][1]

# Display result
st.subheader("Prediction Result")
if prediction == 1:
    st.error("⚠️ The person is at risk of heart disease.")
else:
    st.success("✅ The person is not at risk of heart disease.")

st.write(f"Prediction probability (risk score): **{probability:.2%}**")
