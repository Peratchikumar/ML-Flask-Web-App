# 📈 Marketing Campaign Response Prediction

A Machine Learning web application built with **Python, Scikit-learn, and Flask** to predict whether a customer is likely to respond to a marketing campaign based on demographic and purchasing behavior.

---

## 📌 Project Overview

This project predicts whether a customer will respond to a marketing campaign using a supervised Machine Learning model. The application provides a simple web interface where users can enter customer information and instantly receive a prediction.

---

## 🎯 Objectives

- Predict customer responses to marketing campaigns.
- Build an end-to-end Machine Learning pipeline.
- Deploy the trained model using Flask.
- Create an interactive web application.
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
├── app.py                           # Flask application
├── requirements.txt                 # Python dependencies
├── README.md                        # Project documentation
│
├── model/
│   ├── model.pkl                    # Trained Machine Learning model
│   ├── scaler.pkl                   # StandardScaler object
│   └── encoder.pkl                  # Optional (for categorical features)
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
Data Preprocessing
   │
   ▼
Feature Engineering
   │
   ▼
Train-Test Split
   │
   ▼
Feature Scaling & Encoding
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
Save Model (.pkl)
   │
   ▼
Flask Web Application
   │
   ▼
Prediction
```

---

## 📂 Dataset

**Dataset Name:**

```
superstore_data.csv
```

The dataset contains customer demographic and purchasing information used to predict whether a customer will respond to a marketing campaign.

---

## 📊 Features

- Customer response prediction
- User-friendly Flask interface
- Machine Learning model integration
- Fast prediction results
- Responsive web design
- Error handling

---

## 📈 Model Evaluation

The model performance can be evaluated using:

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

### Navigate to the Project Folder

```bash
cd Marketing_Campaign_Response_Prediction
```

### Install the Required Packages

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

## 💻 Web Application

The application allows users to:

- Enter customer information
- Submit customer details
- Predict customer response
- View prediction results instantly
- Handle invalid inputs gracefully

---

## 📷 Screenshots

### Home Page

```
screenshots/home.png
```

### Prediction Result

```
screenshots/prediction.png
```

---

## 🔮 Future Improvements

- Batch prediction using CSV upload
- REST API integration
- Docker deployment
- Cloud deployment (Render, AWS, Azure)
- Interactive Dashboard
- Model Monitoring

---

## 👨‍💻 Author

**K. Peratchi Kumar**

AI Engineer | Machine Learning Enthusiast

GitHub: https://github.com/Peratchikumar

---

## ⭐ Support

If you found this project helpful, please give this repository a ⭐ on GitHub.

Your support is appreciated!

---

## 📄 License

This project is licensed under the MIT License.