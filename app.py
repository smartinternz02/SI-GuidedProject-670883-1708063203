import pickle
from flask import Flask, render_template, request,session
import pandas as pd
import numpy as пр
import pickle
import joblib
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)
model = pickle.load (open("model.pkl", 'rb'))
ct=joblib.load('column')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('predict.html')

@app.route('/predict', methods= ['POST'])
def predict():
    output=" "
    print("HI")
    a=request.form['a']
    b=request.form['b']
    c=request.form['c']
    d=request.form['d']
    e=request.form['e']
    f=request.form['f']
    g=request.form['g']
    data=[[a,b,c,d,e,f,g]]
    # data=ct.transform(data)
    scale = StandardScaler()
    data =scale.fit_transform(data)
    print(data)
    precition=model.predict(data)
    if precition==0:
            output='Yes. with the help of meteorological and geospatial features we suspect a strong posibility of occurence of lumpy skin Disease(LSD) in this area'
    else:
            output='No. with the help of meterological and geospatial features we DO NOT see posibility of occurence of lumpy skin Disease(LSD) in this area'
    return render_template('result.html',output=output)


if __name__=='__main__':
    app.run(debug=True)