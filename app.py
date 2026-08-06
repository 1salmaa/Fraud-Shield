import streamlit as st

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ FraudShield AI")

st.subheader("Machine Learning Credit Card Fraud Detection")

st.markdown("""
Welcome to **FraudShield AI**.

This application uses a trained **Random Forest** machine learning model to
detect fraudulent credit card transactions.

### Features

- Predict fraudulent transactions
- Batch prediction from CSV files
- Dashboard with model performance
- Feature importance visualization

Use the menu on the left to navigate through the application.
""")

col1, col2, col3 = st.columns(3)

col1.metric("Precision", "98.1%")
col2.metric("Recall", "70.3%")
col3.metric("PR-AUC", "81.1%")

st.success("Final Model: Random Forest")