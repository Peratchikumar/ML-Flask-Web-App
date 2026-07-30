# 📈 Marketing Campaign Response Prediction

A Machine Learning web application built with **Python, Scikit-learn, and Flask** to predict whether a customer is likely to respond to a marketing campaign based on demographic and purchasing behavior.

---

## 🚀 Project Overview

Marketing campaigns help businesses engage customers and improve sales. This project uses a supervised machine learning model to predict whether a customer will respond to a marketing campaign.

The application provides a simple web interface where users can enter customer details and receive an instant prediction.

---

## 🎯 Objectives

- Predict customer responses to marketing campaigns.
- Build an end-to-end Machine Learning pipeline.
- Deploy the trained model using Flask.
- Create an interactive and responsive web interface.
- Demonstrate a real-world ML deployment project.

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- Matplotlib
- Seaborn
- HTML5
- CSS3
- JavaScript

---

## 📂 Project Structure

```text
Marketing-Campaign-Response-Prediction/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── artifacts/
│   ├── model.pkl
│   ├── preprocessor.pkl
│   └── feature_columns.pkl
│
├── data/
│   ├── marketing_campaign.csv
│   └── sample_input.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── Model_Training.ipynb
│   └── Deployment.ipynb
│
├── src/
│   ├── train.py
│   ├── preprocess.py
│   ├── predict.py
│   └── utils.py
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── screenshots/
    ├── home.png
    └── prediction.png
```

---

## ⚙️ Machine Learning Workflow

```text
Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Train-Test Split
    │
    ▼
Model Training
    │
    ▼
GridSearchCV
    │
    ▼
Best Model Selection
    │
    ▼
Model Evaluation
    │
    ▼
Save Model (.pkl)
    │
    ▼
Flask Deployment
```

---

## 📊 Features

- Customer response prediction
- Machine Learning pipeline
- Flask web application
- Responsive user interface
- Real-time prediction
- Easy deployment

---

## 📁 Dataset Features

The model uses customer information such as:

- Age
- Income
- Education
- Marital Status
- Number of Children
- Recency
- Total Spending
- Purchase History
- Customer Behavior

---

## 📈 Model Evaluation

The model is evaluated using:

- Accuracy Score
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Peratchikumar/Marketing-Campaign-Response-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Marketing-Campaign-Response-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Screenshots

### 🏠 Home Page

Add your screenshot here:

```
screenshots/home.png
```

### 📊 Prediction Result

Add your screenshot here:

```
screenshots/prediction.png
```

---

## 🔮 Future Improvements

- Batch prediction using CSV upload
- REST API integration
- Docker deployment
- Cloud deployment
- Interactive Dashboard
- Model Monitoring
- Authentication System

---

## 👨‍💻 Author

**K. Peratchi Kumar**

GitHub: https://github.com/Peratchikumar

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

**Thank you for visiting this repository!**