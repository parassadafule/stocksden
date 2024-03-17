from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, static_url_path='/static')



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


if __name__ == '__main__':
    app.run(debug=True)
