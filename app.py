import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn import preprocessing
import pickle

app = Flask(__name__)
model = pickle.load(open('trained_model_NB.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    category = int(request.form.get('category'))
    type1 = int(request.form.get('type'))
    year = int(request.form.get('year'))
    month = int(request.form.get('month'))
    features = [[category, type1, year, month]]
    
    
    prediction = model.predict(features)
    output = int(prediction[0])
    text = output

    return render_template('index.html', prediction_text='#of Accidents predicted are {}'.format(text))


if __name__ == "__main__":
    app.run(debug=True)
