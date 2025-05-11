# 💓 Heart Disease Risk Prediction App

This is a Streamlit web application that allows users to input health information and receive a prediction of their heart disease risk using a trained Logistic Regression model.

**🔗 Live Demo:** [Click here to open the deployed app](https://your-deployed-streamlit-url.streamlit.app)
or here if above do not work : [https://heartproject-uyihlyyaxvhnwsmrtj8ksv.streamlit.app/](url)
 
---

## 🚀 Features
- Collects user input through a simple form
- Applies Box-Cox transformation to skewed features
- Scales features using StandardScaler
- Predicts risk using a trained logistic regression model
- Displays probability of risk with a clear success/warning message

---

```
### 🛠 Technologies and Tools Used
To bring this app to life, the following tools and libraries were used:

Tool / Library	Purpose
Python	Core programming language
Streamlit	-> To build the interactive web interface
scikit-learn	->For training the Logistic Regression model and scaling inputs
pandas & numpy	-> For data handling and numerical operations
pickle	-> To save and load the trained ML model and preprocessing tools
Box-Cox Transformation	-> To normalize skewed data (oldpeak) for better model performance
```

--- 

## 📁 Files Included

| File                   | Description                                      |
|------------------------|--------------------------------------------------|
| `app.py`               | Main Streamlit application                       |
| `heart_model.pkl`      | Trained logistic regression model                |
| `scaler.pkl`           | StandardScaler used to scale input features      |
| `oldpeak_lambda.pkl`   | Lambda value used in Box-Cox transformation      |
| `requirements.txt`     | List of required Python packages                 |

---

## 🛠 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/heart-disease-predictor.git
   cd heart-disease-predictor
