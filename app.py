from flask import Flask,request,render_template
import pandas as pd
import joblib


model=joblib.load('Model/model.pkl')

app=Flask(__name__)


@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='GET':
        return render_template('index.html')
    else:
        STATE_NAME=request.form['state']
        DISTRICT_NAME=request.form['district']

        NO_OF_ROAD_WORK_SANCTIONED=float(request.form['NO_OF_ROAD_WORK_SANCTIONED'])
        LENGTH_OF_ROAD_WORK_SANCTIONED=float(request.form['LENGTH_OF_ROAD_WORK_SANCTIONED'])
        NO_OF_BRIDGES_SANCTIONED=float(request.form['NO_OF_BRIDGES_SANCTIONED'])
        COST_OF_WORKS_SANCTIONED=float(request.form['COST_OF_WORKS_SANCTIONED'])
        NO_OF_ROAD_WORKS_COMPLETED=float(request.form['NO_OF_ROAD_WORKS_COMPLETED'])
        
        LENGTH_OF_ROAD_WORK_COMPLETED=float(request.form['LENGTH_OF_ROAD_WORK_COMPLETED'])
        NO_OF_BRIDGES_COMPLETED=float(request.form['NO_OF_BRIDGES_COMPLETED'])
        EXPENDITURE_OCCURED=float(request.form['EXPENDITURE_OCCURED'])
        NO_OF_ROAD_WORKS_BALANCE=float(request.form['NO_OF_ROAD_WORKS_BALANCE'])
        LENGTH_OF_ROAD_WORK_BALANCE=float(request.form['LENGTH_OF_ROAD_WORK_BALANCE'])
        NO_OF_BRIDGES_BALANCE=float(request.form['NO_OF_BRIDGES_BALANCE'])

        input=pd.DataFrame(
            [[
            STATE_NAME,
            DISTRICT_NAME,
            NO_OF_ROAD_WORK_SANCTIONED,
            LENGTH_OF_ROAD_WORK_SANCTIONED,
            NO_OF_BRIDGES_SANCTIONED,
            COST_OF_WORKS_SANCTIONED,
            NO_OF_ROAD_WORKS_COMPLETED,
            LENGTH_OF_ROAD_WORK_COMPLETED,
            NO_OF_BRIDGES_COMPLETED,
            EXPENDITURE_OCCURED,
            NO_OF_ROAD_WORKS_BALANCE,
            LENGTH_OF_ROAD_WORK_BALANCE,
            NO_OF_BRIDGES_BALANCE
            ]],
            columns=[
            'STATE_NAME',
            'DISTRICT_NAME',
            'NO_OF_ROAD_WORK_SANCTIONED',
            'LENGTH_OF_ROAD_WORK_SANCTIONED',
            'NO_OF_BRIDGES_SANCTIONED',
            'COST_OF_WORKS_SANCTIONED',
            'NO_OF_ROAD_WORKS_COMPLETED',
            'LENGTH_OF_ROAD_WORK_COMPLETED',
            'NO_OF_BRIDGES_COMPLETED',
            'EXPENDITURE_OCCURED',
            'NO_OF_ROAD_WORKS_BALANCE',
            'LENGTH_OF_ROAD_WORK_BALANCE',
            'NO_OF_BRIDGES_BALANCE'
            ]
        )
        result=model.predict(input)[0]

        return render_template('index.html',ans=result)






if __name__=='__main__':
    app.run(debug=True)