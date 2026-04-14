# END-TO-END House Price Prediction Using Machine Learning

PROJECT OVERVIEW
# DATA SCIENCE PROJECT: House Price Prediction Project
This project is an end-to-end Data Science solution that predicts house prices using Machine Learning. It covers the complete pipeline from data preprocessing and model training to deployment using a Flask web application.
# KEY STEPS
Collected and analyzed housing dataset
Performed Exploratory Data Analysis (EDA)
Handled missing values and feature selection
Trained a regression model for price prediction
Evaluated model using metrics like RMSE and R² score
Saved model using pickle (.pkl)
Deployed model using Flask for real-time predictions
# AI / ML USAGE
A supervised machine learning model (regression) is used to learn patterns from housing data and predict prices based on user inputs like area, bedrooms, and bathrooms.
# DEPLOYMENT
The trained model is integrated into a Flask application where users can input values and get predictions in real time.
# TECHNOLOGIES USED
Python
NumPy, Pandas
Scikit-learn
Flask
HTML, CSS

## Project Structure
- data/ → dataset
- notebooks/ → model training notebook
- model/ → saved ML model
- templates/ → HTML frontend
- static/ → CSS styling
- app.py → Flask backend

## How to Run

1. Install libraries:
cd pip install -r requirements.txt

2. Train model:
Open notebooks/model_training.ipynb and run all cells.

3. Run Flask app:
python app.py

4. Open browser:
http://127.0.0.1:5000

OR 

1.BACKEND :open app.py 
2.Run:cd backend
3.python app.py
4.Open browser:
http://127.0.0.1:5000

## Input Features
- Area
- Bedrooms
- Bathrooms

Output
- House Prediction price


