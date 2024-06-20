from flask import Flask,jsonify,request
from flask_cors import CORS

import util1,dbb
__disease=None

app=Flask(__name__)
CORS(app)

@app.route('/get_Symptom_names')
def get_Symptom_names():
    response=jsonify({
        'Symptoms':util1.get_Symptom_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_Symptom_names2')
def get_Symptom_names2():
    response=jsonify({
        'Symptoms':util1.get_Symptom_names2()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_Symptom_names3')
def get_Symptom_names3():
    response=jsonify({
        'Symptoms':util1.get_Symptom_names3()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_Symptom_names4')
def get_Symptom_names4():
    response=jsonify({
        'Symptoms':util1.get_Symptom_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/get_City_names')
def get_City_names():
    response=jsonify({
        'City':util1.get_City_names()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_disease',methods=['POST'])
def predict_disease():
    Symptom_1=request.form['Symptom_1']
    Symptom_2=request.form['Symptom_2']
    Symptom_3=request.form['Symptom_3']
    Symptom_4=request.form['Symptom_4']
    global __disease
    __disease=util1.predict_dis(Symptom_1,Symptom_2,Symptom_3,Symptom_4)

    response=jsonify({
        'disease':__disease
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/Recommend_doctor',methods=['POST'])
def recommend_doctor():
    City=request.form['City']
    li=dbb.read(City,"Drug Reaction")
    length=len(li)
    for i in range(0,length,1):
        response=jsonify({
            'doctor':li[0][i][0],
            'review':li[0][i][1]
        })
    
    # response = jsonify({'doctors': doctors})
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

    

if __name__ =="__main__":
    print("starting Python Flask Server for house price prediction")
    util1.load_saved_artifacts()
    app.run()