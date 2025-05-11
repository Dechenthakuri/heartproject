# heartproject
Model predicts whether the user is in risk to have a heart attack or not.


💓 Heart Disease Risk Prediction App

This is a Streamlit web application that allows users to input health information and receive a prediction of their heart disease risk using a trained Logistic Regression model.

🚀 Features

Collects user input through a simple form

Applies Box-Cox transformation to skewed features

Scales features using StandardScaler

Predicts risk using a trained logistic regression model

Displays probability of risk with a clear success/warning message

📁 Files Included

File

Description

app.py

Main Streamlit application

heart_model.pkl

Trained logistic regression model

scaler.pkl

StandardScaler used to scale input features

oldpeak_lambda.pkl

Lambda value used in Box-Cox transformation

requirements.txt

List of required Python packages

🛠 How to Run Locally

Clone the repo

git clone https://github.com/yourusername/heart-disease-predictor.git
cd heart-disease-predictor

Install dependencies

pip install -r requirements.txt

Run the app

streamlit run app.py

🌐 How to Deploy on Streamlit Cloud

Push your files to a public GitHub repo

Go to streamlit.io/cloud

Click "New app" and connect your repo

Set the app file path to app.py

Deploy and share the public link

📊 Model Info

Algorithm: Logistic Regression

Target: 0 = Not at Risk, 1 = At Risk

Evaluation Metric: Accuracy and AUC Score

👩‍💻 Built With

Python 🐍

Scikit-learn 🤖

Pandas & NumPy 📊

Streamlit 🌐

📬 Contact

Created by Dechen Thakuri. Feel free to reach out for feedback or collaboration!

