from flask import Flask,render_template, request
import pandas as pd
import numpy as np
import joblib  

app = Flask(__name__)
model = joblib.load('SVR_model.pkl','r+')
x_sc = joblib.load('x_transform.pkl','r+')
y_sc = joblib.load('y_transform.pkl','r+')
@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/prediction',methods=['GET','POST'])
def prediction():
    if request.method == 'POST':
        try:
            level = float(request.form['level'])
            prediction = round(y_sc.inverse_transform(model.predict(x_sc.transform([[level]])))[0],2)
        except ValueError:
            return "Please check if values are correct!!!"
    return render_template("prediction.html", prediction_result = prediction)

if __name__=="__main__":
    app.run(debug=True)
