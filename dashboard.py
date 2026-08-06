import streamlit as st
import matplotlib.pyplot as plt

st.title("📊 Model Dashboard")

col1, col2 = st.columns(2)

col1.metric("Precision","98.1%")
col2.metric("Recall","70.3%")

col1.metric("F1 Score","81.9%")
col2.metric("PR-AUC","81.1%")

st.markdown("---")

st.subheader("Model Comparison")

st.table({
    "Model":[
        "Logistic Regression",
        "Random Forest",
        "XGBoost"
    ],
    "PR-AUC":[
        0.630,
        0.811,
        0.006
    ]
})