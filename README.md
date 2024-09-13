# Income Prediction Application

## Overview
This is a web application built using Flask that predicts whether an individual's income is greater than or less than $50K based on various demographic features such as age, education, marital status, and more. The model is trained on the popular **Adult Census Income Dataset**.

The project uses a **RandomForestClassifier** from `scikit-learn` for the prediction model and provides a user-friendly interface built with **HTML**, **Bootstrap**, and **CSS**.

## Features
- Predict income category (`<=50K` or `>50K`) using user-provided data.
- Upload a CSV file with data for bulk predictions.
- User-friendly interface with responsive design (Bootstrap).
- Data preprocessing pipeline to convert categorical variables into numerical features.
  
## Tech Stack
- **Backend:** Flask, Python
- **Frontend:** HTML, Bootstrap, CSS
- **Machine Learning:** Scikit-learn, Pandas, Pickle
- **Model:** Random Forest Classifier
- **Deployment:** Local Flask server

## Project Structure

```
├── templates/
│   └── input.html       # The HTML template for input form and result display
├── static/
│   └── style.css        # (Optional) Custom CSS (if needed)
├── model.pkl            # Pre-trained RandomForestClassifier model
├── app.py               # The main Flask application script
├── README.md            # Project documentation
└── requirements.txt     # Python dependencies
```
## Prerequisites

Make sure you have the following installed:
- Python 3.x
- Flask
- Pandas
- Scikit-learn
- Bootstrap (via CDN)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/income-prediction-app.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd income-prediction-app
    ```

3. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Download or generate the pre-trained model file (model.pkl)** and place it in the root directory.

## Usage

1. **Run the Flask app:**
    ```bash
    python app.py
    ```

2. **Open your browser and go to:**
    ```bash
    http://127.0.0.1:5000/
    ```

3. **Make Predictions:**
    - You can either manually input the data using the web form or upload a CSV file to make batch predictions.

## Data Format

If you upload a CSV file, make sure it contains the following columns in the specified format:

| age | fnlwgt | education.num | marital.status | sex | capital.gain | capital.loss | hours.per.week |
| --- | ------ | ------------- | ---------------| --- | ------------ | ------------ | -------------- |
| 45  | 172274 | 16            | Married        | Male| 3004         | 0            | 40             |
## Example Input (Web Form)

- **Age:** 34
- **Sex:** Female
- **Marital Status:** Divorced
- **Education Number:** 10
- **Final Weight:** 216864
- **Capital Gain:** 0
- **Capital Loss:** 3770
- **Hours per Week:** 40

## Example Prediction

After entering data or uploading a CSV, the model will return whether the predicted income is `<=50K` or `>50K`.




## Contact

For any questions or suggestions, please contact:
- **Kanhaiya Chaudhary** - [kanhiyachaudhary772@gmail.com](mailto:kanhiyachaudhary772@gmail.com)
- **GitHub**: [github.com/Kanhaiya772](https://github.com/Kanhaiya772)
