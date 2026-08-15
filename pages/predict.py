#import streamlit as st
import pandas as pd
import joblib

model = joblib.load("C:/Users/DELL/Desktop/project_beginning/Fraud-Shield/fraud_model.pkl")

#st.title("🔍 Fraud Prediction")
uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

uploaded_file = pd.read_csv('C:/Users/DELL/Desktop/project_beginning/Fraud-Shield/test.csv')

prediction = model.predict(uploaded_file)

probability = model.predict_proba(uploaded_file)[:,1]

results = {}
results = pd.DataFrame(results)
results["Prediction"] = prediction

results["Fraud Probability"] = probability

results["Prediction"] = results["Prediction"].map({
        0:"Legitimate",
        1:"Fraud"
    })
print(results)


    