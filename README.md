# 🛡️ FraudShield AI

An AI-powered web application for detecting fraudulent credit card transactions using Machine Learning.

## Live Demo

https://intro-to-ai-app-bhbagg58tu6zfrqowmkrnr.streamlit.app/

## Overview

FraudShield AI is a machine learning application built to identify fraudulent credit card transactions. The application uses a trained Random Forest classifier and provides an interactive Streamlit interface for predicting whether a transaction is legitimate or fraudulent.

This project was developed as part of the Introduction to Artificial Intelligence course.

---

## Features

- Predict fraudulent credit card transactions
- Upload CSV files for batch predictions
- View model performance metrics
- Interactive Streamlit web interface
- Download prediction results

---

## Machine Learning Model

Final Model: Random Forest Classifier

The model was trained on the Credit Card Fraud Detection dataset and optimized for highly imbalanced data.

### Performance

| Metric | Score |
|---------|-------|
| Precision | 98.1% |
| Recall | 70.3% |
| F1 Score | 81.9% |
| ROC-AUC | 92.99% |
| PR-AUC | 81.08% |

These results indicate that the model detects fraudulent transactions with high precision while maintaining strong recall.

---

## Dataset

Dataset: Credit Card Fraud Detection Dataset

- Total Transactions: 284,807
- Fraudulent Transactions: 492
- Legitimate Transactions: 284,315

The dataset is highly imbalanced, making Precision-Recall AUC an important evaluation metric.

---

## Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Matplotlib
- Joblib

---

## Project Structure

```
FraudShield-AI/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── README.md
└── pages/
    ├── Dashboard.py
    ├── Predict.py
    └── About.py
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/1salmaa/-.git
```

Move into the project directory

```bash
cd FraudShield-AI
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## Screenshots

Add screenshots of:

- Home Page
- Dashboard
- Prediction Page

---

## Future Improvements

- Real-time transaction monitoring
- Deep Learning models
- Explainable AI (SHAP)
- User authentication
- Cloud database integration
- REST API for predictions

---

## Author

Salma A.D. Nabonadam

Ashesi University

Introduction to Artificial Intelligence

2026

---

## License

This project was developed for educational purposes.
