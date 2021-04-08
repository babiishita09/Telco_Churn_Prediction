
import pandas as pd
from flask_cors import CORS, cross_origin
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

@app.route("/",methods=['GET'])
@cross_origin()
def HomePage():
	return render_template('home.html')

@app.route('/predict', methods=["POST","GET"])
@cross_origin()
def predict():
    if request.method == "POST":
        SeniorCitizen=request.form['SeniorCitizen']
        if (SeniorCitizen=='Yes'):
            SeniorCitizen=1
        else:
            SeniorCitizen=0
        MonthlyCharges=float(request.form['MonthlyCharges'])
        TotalCharges=float(request.form['TotalCharges'])
        gender=int(request.form['gender'])
        Partner=int(request.form['Partner'])
        Dependents=int(request.form['Dependents'])
        PhoneService=int(request.form['PhoneService'])
        MultipleLines=int(request.form['MultipleLines'])
        InternetService=int(request.form['InternetService'])
        OnlineSecurity=int(request.form['OnlineSecurity'])
        OnlineBackup=int(request.form['OnlineBackup'])
        DeviceProtection=int(request.form['DeviceProtection'])
        TechSupport=int(request.form['TechSupport'])
        StreamingTV=int(request.form['StreamingTV'])
        StreamingMovies=int(request.form['StreamingMovies'])
        Contract=int(request.form['Contract'])
        PaperlessBilling=int(request.form['PaperlessBilling'])
        PaymentMethod=int(request.form['PaymentMethod'])
        tenure_group= int(request.form['tenure_group'])

    model = pickle.load(open("churn_model_final.sav", "rb"))
    data = np.array([[gender, SeniorCitizen, Partner, Dependents, PhoneService,
       MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
       DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
       Contract, PaperlessBilling, PaymentMethod, MonthlyCharges,
       TotalCharges, tenure_group]])


    prediction = model.predict(data)
    # probablity = model.predict_proba(new_df__dummies.tail(1))[:, 1]
    if prediction[0] == 1:
        o = "This customer is likely to be churned!!"
    else:
        o = "This customer is likely to continue!!"

    return render_template('home.html', output=o)

if __name__ == "__main__":
    app.run(port=8000, debug=True)









