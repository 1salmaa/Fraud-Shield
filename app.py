import streamlit as st

st.set_page_config(
    page_title="FraudShield AI",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
.main{
    background-color:#f8fafc;
}

.hero{
    padding:40px;
    border-radius:15px;
    background:linear-gradient(90deg,#0f172a,#2563eb);
    color:white;
}

.metric{
    background:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
    text-align:center;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:60px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
<h1>🛡️ FraudShield AI</h1>

<h3>Machine Learning Powered Credit Card Fraud Detection</h3>

Detect fraudulent transactions using a trained Random Forest model.

Built for the Introduction to AI Project at Ashesi University.
</div>
""", unsafe_allow_html=True)

st.write("")

c1,c2,c3,c4=st.columns(4)

with c1:
    st.metric("Precision","98.1%")

with c2:
    st.metric("Recall","70.3%")

with c3:
    st.metric("F1 Score","81.9%")

with c4:
    st.metric("PR-AUC","81.1%")

st.divider()

left,right=st.columns([2,1])

with left:

    st.header("About FraudShield AI")

    st.write("""
FraudShield AI is a machine learning application that identifies potentially fraudulent
credit card transactions.

The application uses a Random Forest classifier trained on highly imbalanced transaction
data and was evaluated using Precision, Recall, F1-score and Precision-Recall AUC.

Use the navigation menu on the left to:

• Upload transaction data

• Predict fraudulent transactions

• View model performance

• Explore feature importance
""")

with right:

    st.info("Model")

    st.success("Random Forest Classifier")

    st.info("Dataset")

    st.write("284,807 Transactions")

    st.info("Fraud Cases")

    st.write("492")

st.divider()

st.markdown(
"""
<div class='footer'>

Developed by Salma A.D. Nabonadam

Ashesi University

Introduction to Artificial Intelligence

2026

</div>
""",
unsafe_allow_html=True)