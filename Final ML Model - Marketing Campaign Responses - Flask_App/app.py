from flask import Flask, render_template, request
import pandas as pd
import joblib

# Create Flask app
app = Flask(__name__)

# Load trained model and preprocessor
model = joblib.load("artifacts/model.pkl")
preprocessor = joblib.load("artifacts/preprocessor.pkl")
feature_columns = joblib.load("artifacts/feature_columns.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Read values from HTML form
        input_data = {}

        for feature in feature_columns:
            value = request.form.get(feature)

            # Convert numeric values
            try:
                value = float(value)
            except:
                pass

            input_data[feature] = value

        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Preprocess
        transformed_data = preprocessor.transform(input_df)

        # Prediction
        prediction = model.predict(transformed_data)[0]

        # Probability (if supported)
        probability = None
        if hasattr(model, "predict_proba"):
            probability = model.predict_proba(transformed_data)[0][1]

        # Convert prediction to readable text
        if prediction == 1:
            result = "Customer will respond to the marketing campaign."
        else:
            result = "Customer is unlikely to respond to the marketing campaign."

        return render_template(
            "result.html",
            prediction=result,
            probability=round(probability * 100, 2) if probability else None
        )

    except Exception as e:
        return render_template(
            "result.html",
            prediction=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)


    

