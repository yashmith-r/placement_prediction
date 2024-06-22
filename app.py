from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
import pickle
app= Flask(__name__)
model = tf.keras.models.load_model("my_model")
scaler = pickle.load(open('scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        gender = int(request.form['gender'])
        ssc_p = float(request.form['ssc_p'])
        ssc_b_Central = int(request.form['ssc_b'])
        hsc_p = float(request.form['hsc_p'])
        hsc_b_Central = int(request.form['hsc_b'])
        hsc_s = request.form['hsc_s']
        degree_p = float(request.form['degree_p'])
        degree_t = request.form['degree_t']
        workex = int(request.form['workex'])
        etest_p = float(request.form['etest_p'])
        specialisation = int(request.form['specialisation'])
        mba_p = float(request.form['mba_p'])
        print('Gender : ',gender)
        print('ssc_p : ',ssc_p)
        print('ssc_b_Central : ',ssc_b_Central)
        print('hsc_p : ',hsc_p)
        print('hsc_b_Central : ',hsc_b_Central)
        print('hsc_s : ',hsc_s)
        print('degree_p : ',degree_p)
        print('degree_t : ',degree_t)
        print('workex : ',workex)
        print('etest_p : ',etest_p)
        print('specialisation : ',specialisation)
        print('mba_p : ',mba_p)

        scaled = scaler.transform(np.array([gender,ssc_p,ssc_b_Central,hsc_p,hsc_b_Central,hsc_s,degree_p,degree_t,workex,etest_p,specialisation,mba_p]).reshape(1, -1))
        
        prediction = (model.predict(scaled) * 100).round(2)[0][0]
        if prediction < 0:
            prediction = 0
    return render_template('prediction.html',result=prediction)


