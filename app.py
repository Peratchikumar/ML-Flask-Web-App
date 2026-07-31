from flask import Flask, render_template, request
import pandas as pd
import joblib

# ==============================
# Create Flask App
# ==============================

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

        # Get input values from HTML form
        income = float(request.form["Income"])
        kidhome = int(request.form["Kidhome"])
        teenhome = int(request.form["Teenhome"])
        recency = float(request.form["Recency"])
        mntwines = float(request.form["MntWines"])

        # Create DataFrame
        input_df = pd.DataFrame({
            "Income": [income],
            "Kidhome": [kidhome],
            "Teenhome": [teenhome],
            "Recency": [recency],
            "MntWines": [mntwines]
        })

        # Predict
        prediction = model.predict(input_df)[0]

        # Prediction Probability (if available)
        probability = None

        if hasattr(model, "predict_proba"):
            probability = round(
                model.predict_proba(input_df)[0].max() * 100,
                2
            )

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
# Run Flask
# ==============================

if __name__ == "__main__":
    app.run(debug=True)