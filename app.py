from flask import Flask,request,json,render_template
import joblib


model=joblib.load('Model/P8.pickle')

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def predict():
    return ''






if __name__=='__main__':
    app.run(debug=True)