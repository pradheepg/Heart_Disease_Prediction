from flask import Flask, request, render_template
import pandas as pd
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load the saved model
model_filename = 'model.pkl'
loaded_model = joblib.load(model_filename)

# Define the home route to display the form
@app.route('/')
def home():
    return render_template('index.html')

# Define the route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form inputs
    age = int(request.form['age'])
    male= int(request.form['sex'])
    currentSmoker= int(request.form['is_smoking'])
    cigs_per_day = float(request.form['cigs_per_day'])
    BPMeds = float(request.form['BPMeds'])
    prevalent_stroke = int(request.form['prevalent_stroke'])
    prevalent_hyp = int(request.form['prevalent_hyp'])
    diabetes = int(request.form['diabetes'])
    totChol = float(request.form['totChol'])
    sysBP = float(request.form['sysBP'])
    diaBP = float(request.form['diaBP'])
    BMI = float(request.form['BMI'])
    heart_rate = float(request.form['heart_rate'])
    glucose = float(request.form['glucose'])

    # Create a DataFrame with the user input
    '''user_data = pd.DataFrame({
        'male' [sex],'age' [age],  'currentSmoking' [is_smoking], 'cigsPerDay' [cigs_per_day],
        'BPMeds' [BPMeds], 'prevalentStroke' [prevalent_stroke], 'prevalentHyp' [prevalent_hyp],
        'diabetes' [diabetes], 'totChol' [totChol], 'sysBP' [sysBP], 'diaBP' [diaBP],
        'BMI' [BMI], 'heartRate' [heart_rate], 'glucose' [glucose]
    })'''
    user_data = pd.DataFrame({
    'male': [male],'age': [age],  'currentSmoker': [currentSmoker], 'cigsPerDay': [cigs_per_day],
    'BPMeds': [BPMeds], 'prevalentStroke': [prevalent_stroke], 'prevalentHyp': [prevalent_hyp],
    'diabetes': [diabetes], 'totChol': [totChol], 'sysBP': [sysBP], 'diaBP': [diaBP],
    'BMI': [BMI], 'heartRate': [heart_rate], 'glucose': [glucose]

})

    # Make the prediction
    prediction = loaded_model.predict(user_data)

    # Determine the result message
    if prediction[0] == 1:
        result = "The model predicts that you are at risk of coronary heart disease in the next 10 years."
    else:
        result = "The model predicts that you are NOT at risk of coronary heart disease in the next 10 years."

    # Render the result on a new page
    return render_template('result.html', prediction_text=result)

# Run the Flask app
if __name__ == __name__:
    app.run(debug=True)
