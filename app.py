from flask import Flask, render_template, request
import numpy as np
import h5py
import tensorflow
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
app = Flask(__name__)
model = load_model('car_purchase.h5')
@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

scaler = MinMaxScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0
        Age=int(request.form['Age'])
        Annual_Salary=float(request.form['Annual_Salary'])
        Credit_Card_Debt=float(request.form['Credit_Card_Debt'])
        Net_Worth=float(request.form['Net_Worth'])


        prediction=model.predict([[Gender, Age, Annual_Salary, Credit_Card_Debt, Net_Worth]])
        output=prediction[:,0]
        return render_template('home.html',prediction_amount=output[0])
    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)