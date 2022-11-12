from flask import Flask
from flask import render_template
from flask import request

import pickle
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method=='GET':
        return('sd')
    elif request.method=='POST':
        name = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        sslc = request.form['sslc']
        plustwo = request.form['plustwo']
        degree = request.form['degree']
        pg = request.form['pg']
        cert = request.form['cert']
        tech = request.form['tech']
        exp = request.form['exp']        
        pcomp = request.form['pcomp']
        psal = request.form['psal']
        ccomp = request.form['ccomp']
        result = round(predict([[gender,age,sslc,plustwo,degree,pg,cert,tech,exp,pcomp,psal,ccomp]])[0])
        return render_template('result.html',name=name,res=result)
    else:
        return("ok")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('err404.html'), 404

def predict(input):
    reg = pickle.load(open('model/final_model.sav', 'rb'))
    df = pd.DataFrame(input)
    res = reg.predict(df)
    return res