# 📈 Marketing Campaign Response Prediction

A Machine Learning web application built with **Python**, **Scikit-learn**, and **Flask** to predict whether a customer is likely to respond to a marketing campaign based on customer demographic and purchasing information.

---

## 📌 Project Overview

Marketing campaigns are essential for improving customer engagement and increasing sales. This project uses a Machine Learning classification model to predict whether a customer will respond to a marketing campaign.

The trained model is deployed using the Flask web framework, allowing users to enter customer information through a web interface and receive instant predictions.

---

## 🎯 Objectives

- Predict customer responses to marketing campaigns.
- Build an end-to-end Machine Learning pipeline.
- Deploy the trained model using Flask.
- Create an interactive and user-friendly web application.
- Demonstrate a real-world Machine Learning deployment project.

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Joblib
- HTML5
- CSS3
- JavaScript

---

## 📁 Project Structure

```text
Marketing_Campaign_Response_Prediction/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── model.pkl
│
├── templates/
│   ├── index.html
│   ├── result.html
│   └── error.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── dataset/
    └── superstore_data.csv
```

---

## ⚙️ Machine Learning Workflow

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis
   │
   ▼
Feature Engineering
   │
   ▼
Data Preprocessing
   │
   ▼
Train-Test Split
   │
   ▼
Model Training
   │
   ▼
Hyperparameter Tuning (GridSearchCV)
   │
   ▼
Model Evaluation
   │
   ▼
Save Trained Model (model.pkl)
   │
   ▼
Flask Web Application
   │
   ▼
Customer Response Prediction
```

---

## 📂 Dataset

**Dataset Name**

```
superstore_data.csv
```

The dataset contains customer demographic and purchasing information used to train a Machine Learning classification model that predicts customer responses to marketing campaigns.

---

## ✨ Features

- Customer response prediction
- Interactive Flask web interface
- Responsive web design
- Machine Learning model deployment
- Error handling
- Prediction result page
- Clean project structure

---

## 📊 Machine Learning Model

The model was trained using:

- Supervised Machine Learning
- GridSearchCV for hyperparameter tuning
- Classification algorithms
- Model serialization using Joblib

---

## 📈 Evaluation Metrics

The model can be evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Peratchikumar/Marketing_Campaign_Response_Prediction.git
```

### Navigate to the Project Directory

```bash
cd Marketing_Campaign_Response_Prediction
```

### Install Dependencies

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

## 💻 Application Workflow

1. Open the web application.
2. Enter customer details.
3. Click **Predict Response**.
4. View the prediction result.
5. Predict another customer if needed.

---

## 📷 Screenshots

### Home Page

```
screenshots/home_page.png
```

### Prediction Result

```
screenshots/prediction_result.png
```

---

## 🔮 Future Enhancements

- CSV file upload for batch prediction
- REST API development
- Docker containerization
- Cloud deployment (Render, AWS, Azure)
- Interactive dashboard
- Model monitoring
- User authentication

---

## 👨‍💻 Author

**K. Peratchi Kumar**

AI Engineer | Machine Learning Enthusiast

GitHub:
https://github.com/Peratchikumar

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📄 License

This project is licensed under the MIT License.