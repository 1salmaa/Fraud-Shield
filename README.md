# 🛡️ FraudShield AI

A Machine Learning-powered web application for detecting fraudulent credit card transactions using a **Random Forest Classifier**. The application allows users to predict fraudulent transactions through an interactive Streamlit interface.

🔗 **Live Demo:** https://srxesydyh52crkcymjvwor.streamlit.app/

---

# 📌 Project Overview

Credit card fraud causes significant financial losses worldwide. This project applies supervised machine learning to identify fraudulent transactions from a highly imbalanced dataset.

The application was developed as part of the **Introduction to Artificial Intelligence** course and demonstrates the complete machine learning workflow—from data preprocessing and model training to deployment as a web application.

---

# ✨ Features

- 🛡️ Detect fraudulent credit card transactions
- 📊 Interactive Streamlit dashboard
- 🔍 Predict fraud using a trained Random Forest model
- 📈 View model performance metrics
- ☁️ Live web deployment
- 💻 Open-source code on GitHub

---

# 🧠 Machine Learning Workflow

```
Credit Card Dataset
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Train / Validation / Test Split
        │
        ▼
Random Forest Classifier
        │
        ▼
Hyperparameter Tuning
(RandomizedSearchCV)
        │
        ▼
Model Evaluation
        │
        ▼
Model Deployment
(Streamlit)
```

---

# 📊 Dataset

**Dataset:** Credit Card Fraud Detection Dataset

- Total Transactions: **284,807**
- Legitimate Transactions: **284,315**
- Fraudulent Transactions: **492**

The dataset is highly imbalanced, making Precision, Recall, F1-score, and PR-AUC more appropriate evaluation metrics than accuracy alone.

---

# 🤖 Model

**Algorithm Used**

- Random Forest Classifier

The model was selected after comparing multiple approaches due to its strong performance on imbalanced data and its ability to generalize well.

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| Precision | **98.1%** |
| Recall | **70.3%** |
| F1 Score | **81.9%** |
| ROC-AUC | **0.93** |
| PR-AUC | **0.81** |

These results demonstrate that the model achieves excellent precision while maintaining strong recall for detecting fraudulent transactions.

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Matplotlib

---

# 📂 Project Structure

```text
Fraud-Shield/
│
├── app.py
├── fraud_model.pkl
├── requirements.txt
├── README.md
│
└── pages/
    ├── dashboard.py
    ├── predict.py
    └── about.py
```

---

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/1salmaa/Fraud-Shield.git
```

Navigate into the project folder:

```bash
cd Fraud-Shield
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

# 🌐 Live Application

Access the deployed application here:

**https://srxesydyh52crkcymjvwor.streamlit.app/**

---

# 📸 Screenshots

<img width="1163" height="675" alt="image" src="https://github.com/user-attachments/assets/73087d7a-8d1a-4393-abaa-9564e80b55cb" /> 




### 🏠 About Page

<img width="1180" height="678" alt="image" src="https://github.com/user-attachments/assets/52b8489b-a8b2-4d76-bda6-a9ae0ee07299" />

### 📊 Dashboard

<img width="1162" height="657" alt="image" src="https://github.com/user-attachments/assets/ed9d524c-cecf-4a11-87b4-5ddac2469446" />

### 🔍 Prediction Page

<img width="787" height="463" alt="image" src="https://github.com/user-attachments/assets/ecfab533-a32b-4487-9af7-16309306ac8b" />

---

# 🔮 Future Improvements

- Real-time fraud monitoring
- Explainable AI using SHAP values
- Deep Learning models
- User authentication
- Batch CSV prediction uploads
- REST API integration
- Cloud database support

---

# 👩‍💻 Author

**Salma A.D. Nabonadam**

BSc Computer Science

Ashesi University

Introduction to Artificial Intelligence

---

# 📄 License

This project was developed for educational purposes as part of the Introduction to Artificial Intelligence course.
