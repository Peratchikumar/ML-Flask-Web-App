from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# ==========================
# Load Saved Files
# ==========================

model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

try:
    encoder = joblib.load("model/encoder.pkl")
except:
    encoder = None


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # --------------------------
        # Get Form Values
        # --------------------------

        age = float(request.form["Age"])
        income = float(request.form["Income"])
        recency = float(request.form["Recency"])
        total_spending = float(request.form["Total_Spending"])
        num_web_purchases = float(request.form["NumWebPurchases"])
        num_catalog_purchases = float(request.form["NumCatalogPurchases"])
        num_store_purchases = float(request.form["NumStorePurchases"])

        education = request.form["Education"]
        marital_status = request.form["Marital_Status"]

        # --------------------------
        # Encode Categorical Data
        # --------------------------

        if encoder is not None:

            encoded = encoder.transform(
                [[education, marital_status]]
            )

            encoded = np.array(encoded).flatten()

        else:

            encoded = np.array([])

        # --------------------------
        # Numerical Features
        # --------------------------

        numerical = np.array([
            age,
            income,
            recency,
            total_spending,
            num_web_purchases,
            num_catalog_purchases,
            num_store_purchases
        ]).reshape(1, -1)

        # --------------------------
        # Scale Numerical Data
        # --------------------------

        numerical_scaled = scaler.transform(numerical)

        # --------------------------
        # Final Input
        # --------------------------

        final_input = np.concatenate(
            [numerical_scaled, encoded.reshape(1, -1)],
            axis=1
        )

        # --------------------------
        # Prediction
        # --------------------------

        prediction = model.predict(final_input)[0]

        probability = model.predict_proba(final_input)[0].max()

        return render_template(
            "result.html",
            prediction=prediction,
            probability=round(probability * 100, 2)
        )

    except Exception as e:

        return render_template(
            "error.html",
            error=str(e)
        )


# ==========================
# Run Application
# ==========================

if __name__ == "__main__":
    app.run(debug=True)