from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, static_url_path='/static')

# Load the pre-trained model
with open('insurance_cost_model.pkl', 'rb') as model_file:
    insurance_price_model = pickle.load(model_file)

with open('insurance_plan_model.pkl', 'rb') as model_file:
    insurance_plan_model = pickle.load(model_file)


@app.route('/')
def index():
    return render_template('home_page.html')
@app.route('/home_page')
def home():
    return render_template('home_page.html')

@app.route('/login_page')
def login_page():
    return render_template('login_page.html')

@app.route('/register_page')
def register_page():
    return render_template('register_page.html')


@app.route('/scratch')
def scratch():
    return render_template('scratch.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')


@app.route('/scratch_page')
def scratch_page():
    return render_template('scratch_page.html')


@app.route('/stock_prediction')
def stock_prediction():
    return render_template('stock_prediction.html')


@app.route('/payment_page')
def payment_page():
    return render_template('payment_page.html')

@app.route('/return_calculator')
def return_calculator():
    return render_template('return_calculator.html')

@app.route('/wellness_prediction')
def wellness():
    return render_template('wellness_prediction.html')

@app.route('/two_page')
def twopage():
    return render_template('two_page.html')
@app.route('/insurance_price')
def insurance_price():
    return render_template('insurance_price_form.html')

@app.route('/insurance_plan')
def insurance_plan():
    return render_template('insurance_plan_form.html')



@app.route('/insurance_plan', methods=['POST'])
def insurance_plan_predict():
    # Extract input parameters from the form
    age = int(request.form.get('age'))
    gender = 1 if request.form.get('gender') == 'female' else 0
    chest_pain = int(request.form.get('chest_pain'))
    blood_pressure = int(request.form.get('blood_pressure'))
    cholesterol = int(request.form.get('cholesterol'))
    fasting_sugar = int(request.form.get('fasting_sugar'))
    rest_ecg = int(request.form.get('rest_ecg'))
    max_heart_rate = int(request.form.get('max_heart_rate'))
    exercise_angina = 1 if request.form.get('exercise_angina') == 'true' else 0
    st_depression = float(request.form.get('st_depression'))
    slope_peak_st = int(request.form.get('slope_peak_st'))
    num_vessels = int(request.form.get('num_vessels'))
    thal = int(request.form.get('thal'))
    # smoker = 1 if request.form.get('smoker') == 'true' else 0

    # Convert input values to a NumPy array
    input_data = np.array([[age, gender, chest_pain, blood_pressure, cholesterol, fasting_sugar, rest_ecg,max_heart_rate, exercise_angina, st_depression, slope_peak_st, num_vessels, thal]])

    # Make a prediction using the trained model
    prediction =insurance_plan_model.predict(input_data)

    # Display the prediction
    return render_template('insurance_plan_result.html', prediction=prediction[0])


@app.route('/insurance_cost', methods=['POST'])
def insurance_price_predict():
    # Retrieve form data
    age = int(request.form.get('age'))
    sex = request.form.get('sex') == 'true'
    bmi = float(request.form.get('bmi'))
    children = int(request.form.get('children'))
    smoker = request.form.get('smoker') == 'true'
    region = int(request.form.get('region'))

    # Create a feature vector
    features = np.array([[age, sex, bmi, children, smoker, region]])
    # Make a prediction using the pre-trained model
    prediction = insurance_price_model.predict(features)
    # For now, let's just print the prediction
    print('Prediction:', prediction)
    # You can return the prediction as JSON or any other format
    return render_template('insurance_price_result.html', prediction=prediction[0])


   

if __name__ == '__main__':
    app.run(debug=True)