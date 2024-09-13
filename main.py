from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('input.html')

# Preprocess input data
def preprocess_user_input(data):
    # Convert categorical inputs to numerical values
    data["sex"] = 1 if data["sex"] == "Female" else 0
    data["marital.status"] = 1 if data["marital.status"] in ['Married-civ-spouse', 'Married-AF-spouse'] else 0
    
    # Create a DataFrame with the input values
    features = pd.DataFrame(data, index=[0])
    return features

# Route to handle prediction request from user form input
@app.route('/predict', methods=['POST'])
def predict():
    # Get form data from the user
    input_data = {
        "age": int(request.form["age"]),
        "sex": request.form["sex"],
        "marital.status": request.form["marital.status"],
        "education.num": int(request.form["education.num"]),
        "fnlwgt": int(request.form["fnlwgt"]),
        "capital.gain": int(request.form["capital.gain"]),
        "capital.loss": int(request.form["capital.loss"]),
        "hours.per.week": int(request.form["hours.per.week"]),
    }

    # Preprocess the input data
    features = preprocess_user_input(input_data)

    # Make prediction
    prediction = model.predict(features)

    # Map prediction to readable format
    result = '<=50K' if prediction[0] == 0 else '>50K'

    # Render the prediction result on the same page
    return render_template('input.html', prediction_text_rfc=result)

if __name__ == '__main__':
    app.run(debug=True)
