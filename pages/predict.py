import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_model.pkl")

st.title("🔍 Fraud Prediction")

uploaded_file = st.file_uploader(
    "Upload a CSV file",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    prediction = model.predict(df)

    probability = model.predict_proba(df)[:,1]

    results = df.copy()

    results["Prediction"] = prediction

    results["Fraud Probability"] = probability

    results["Prediction"] = results["Prediction"].map({
        0:"Legitimate",
        1:"Fraud"
    })

    st.dataframe(results)

    csv = results.to_csv(index=False)

    st.download_button(
        "Download Results",
        csv,
        "predictions.csv"
    )