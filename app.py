from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ==============================
# Load Trained Model
# ==============================

model = joblib.load("model/model.pkl")


# ==============================
# Home Page
# ==============================

@app.route("/")
def home():
    return render_template("index.html")


# ==============================
# Prediction
# ==============================

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Collect input from the HTML form
        input_data = {
            "Age": float(request.form["Age"]),
            "Income": float(request.form["Income"]),
            "Recency": float(request.form["Recency"]),
            "Total_Spending": float(request.form["Total_Spending"]),
            "NumWebPurchases": float(request.form["NumWebPurchases"]),
            "NumCatalogPurchases": float(request.form["NumCatalogPurchases"]),
            "NumStorePurchases": float(request.form["NumStorePurchases"]),
            "Education": request.form["Education"],
            "Marital_Status": request.form["Marital_Status"]
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Prediction
        prediction = model.predict(input_df)[0]

        # Prediction Probability (if supported)
        probability = None
        if hasattr(model, "predict_proba"):
            probability = round(model.predict_proba(input_df)[0].max() * 100, 2)

        return render_template(
            "result.html",
            prediction=prediction,
            probability=probability
        )

    except Exception as e:

        return render_template(
            "error.html",
            error=str(e)
        )


# ==============================
# Run Application
# ==============================

if __name__ == "__main__":
    app.run(debug=True)