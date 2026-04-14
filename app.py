from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model/trained_model.pkl", "rb"))


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        area = float(request.form.get("area"))
        bedrooms = int(request.form.get("bedrooms"))
        bathrooms = int(request.form.get("bathrooms"))

        print("Input:", area, bedrooms, bathrooms)

        # Prediction
        prediction = model.predict([[area, bedrooms, bathrooms]])
        price = round(float(prediction[0])*10, 2)

        return render_template(
            "index.html",
            prediction_text=f"Predicted House Price: ₹ {price}"
        )

    except Exception as e:
        print("❌ Error:", e)

        return render_template(
            "index.html",
            prediction_text="Error during prediction. Please check your input."
        )


if __name__ == "__main__":
    app.run(debug=True)