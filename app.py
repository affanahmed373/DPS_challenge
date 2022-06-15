import numpy as np
import pandas as pd
from flask import Flask, request, render_template, jsonify
from sklearn import preprocessing
import pickle

app = Flask(__name__)
model = pickle.load(open('trained_model_NB.pkl', 'rb'))

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    features = [[year, month]]
    
    
    prediction = model.predict(features)
    output = int(prediction[0])
    text = output

    return render_template('index.html', prediction_text='#of Accidents predicted are {}'.format(text))

@app.route("/api/predict", methods=["POST"])
def apiPredict():
    if "year" not in request.get_json() or "month" not in request.get_json():
        return {"Missing Values Year and/Or Month"}, 400

    data = request.get_json()
    year = data['year']
    month = data['month']

    if type(year) != int or month not in range(1, 13):
        return {"Faulty Input"}, 400
    else:
        features = [[year, month]]
        prediction = int(model.predict(features)[0])
        return {'prediction': prediction}
if __name__ == "__main__":
    app.run(debug=True)
