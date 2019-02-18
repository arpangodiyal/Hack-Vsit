from flask import Flask, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask import render_template
from file2 import makePrediction
import numpy as np

app = Flask(__name__)

@app.route('/survey', methods = ['POST', 'GET'])
def funcPost():
    c = None
    if request.method == 'POST':
        age = request.form['group0']

        dict1 = {"Male":1, "Female":0, "Other":2}
        gender = dict1[request.form['group1']]

        dict1 = {"Yes":1, "No":0}
        self_emp = dict1[request.form['group2']]

        dict1 = {"Yes":2, "Don't Know":0, "No":1}
        mental_disorders = dict1[request.form['group3']]

        dict1 = {"Yes":1, "No":0}
        mental_healthinPast = dict1[request.form['group4']]

        dict1 = {"Yes":2, "No":1, "Don't Know":0}
        work_from_home = dict1[request.form['group5']]

        dict1 = {"Yes":2, "No":1, "Kind off":0}
        technology = dict1[request.form['group6']]

        dict1 = {"Yes":2, "No":1, "Don't Know":0}
        benefits = dict1[request.form['group7']]

        dict1 = {"Yes":2, "No":1, "Don't Know":0}
        know_benefits = dict1[request.form['group8']]

        dict1 = {"Yes":2, "No":1, "May be":0}
        wellness = dict1[request.form['group9']]

        dict1 = {"Yes":2, "No":1, "May be":0}
        mental_issues = dict1[request.form['group10']]

        dict1 = {"Yes":2, "No":1, "May be":0}
        mental_health = dict1[request.form['group11']]

        arr1 = [age, gender, self_emp, mental_disorders, mental_healthinPast, work_from_home, technology, benefits, know_benefits, wellness, mental_issues, mental_health]
        try:
            c = makePrediction(np.array(arr1,dtype='int'))
            c = c[0]
        except:
            c = 2
        dict1 = {0:"Mild", 1:"No", 2:"Depression"}
        return render_template('results.html', result=dict1[c])
    return render_template('survey.html', result = c)

@app.route('/')
def index():
    return render_template('index.html')
#FAA831

class HelloWorld(Resource):
    def get(self):
        json_data = request.get_json(force=True)
        age = json_data['age']
        gender = json_data['gender']
        self_emp = json_data['self_emp']
        mental_disorders  = json_data['mental_disorders ']
        mental_healthinPast = json_data['mental_healthinPast']
        work_from_home = json_data['work_from_home']
        technology = json_data['technology']
        benefits = json_data['benefits']
        know_benefits = json_data['know_benefits']
        wellness = json_data['wellness']
        mental_issues = json_data['mental_issues']
        mental_health = json_data['mental_health']
        arr1 = [age, gender, self_emp, mental_disorders, mental_healthinPast, work_from_home, technology, benefits, know_benefits, wellness, mental_issues, mental_health]
        return jsonify(makePrediction(np.array(arr1,dtype='int')))

api.add_resource(HelloWorld, '/testing')

if __name__ == "__main__":
    app.run(debug=True)

#2 - Depression
#1-No
#0-mild