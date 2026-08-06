import streamlit as st

st.title("ℹ️ About")

st.markdown("""

## Credit Card Fraud Detection

This project uses machine learning to identify fraudulent credit card transactions.

### Dataset

European credit card transactions.

### Models Evaluated

- Logistic Regression
- Random Forest
- XGBoost

### Final Model

Random Forest

### Why Random Forest?

It achieved the highest PR-AUC and F1-score while maintaining excellent precision on an imbalanced dataset.

""")