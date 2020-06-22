import pandas as pd
from flask import Flask, jsonify, request, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, FileField
from wtforms.validators import DataRequired
import pickle
from sklearn.svm import LinearSVC
#from sklearn.externals import joblib
import joblib
import requests
import json
from flask_bootstrap import Bootstrap

# load model
#model = pickle.load(open('trained_model-[all].pkl','rb'))
#model = joblib.load("full_model2.jl")
# app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
bootstrap = Bootstrap(app)
#forms
class TriageForm(FlaskForm):
    req_text = StringField("Please enter the ATIP request text", validators=[DataRequired()])
    req_type = SelectField(u'Select the request type:',
                            choices=[('','Default, blank'),
                            ('dept-only','Department Only'),
                            ('prob_dept','Departments and their probabilities'),
                            ('ised_sector',"ISED's Sectors")])
    submit = SubmitField('Submit')

class RedactForm(FlaskForm):
    picture = FileField("Please select image to redact text", validators=[DataRequired()])
    submit = SubmitField('Submit')

# routes
@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/triage/', methods=['GET','POST'])
def triage():
    form = TriageForm()
    if form.validate_on_submit():
        url='https://atip-triage-alldept.herokuapp.com/request/'
        session['req_text'] = form.req_text.data
        session['req_type'] = form.req_type.data
        input_data={}
        input_data['text'] = session['req_text'] 
        input_data['what'] = session['req_type'] 
        
        data = json.dumps(input_data)
        send_request = requests.post(url,data)
        if send_request.status_code == 200:
            response = send_request.json()
        else:
            response = f"Error, code:({send_request.status_code})"
        
        #return "Error: "+str(send_request.status_code)
        return render_template ('triage.html', form=form, output=(data, response))
    return render_template('triage.html', form=form)

@app.route('/todo/', methods=['GET'])
def todo():
    return render_template('todo.html')

@app.route('/doc_ret/', methods=['GET'])
def doc_ret():
    return render_template('doc_ret.html')

@app.route('/redact/', methods=['GET','POST'])
def redact():
    form = RedactForm()

    return render_template('redact.html',form=form)

@app.route('/links/', methods=['GET'])
def links():
    return render_template('links.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')



@app.route('/request/', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    if data.get('what')=='ised_sector':
        from predict_ised_sector import predict_sector_ised as pis
        result = pis(data.get('text'))
        return jsonify(result)
    elif data.get('what')=='prob_dept':
        from dept_prob import predict_dept_prob
        result = predict_dept_prob(data.get('text'))
        return jsonify(result)
    else:
        from predict_dept import predict_dept
        result = predict_dept(data.get('text'))
        if result['dept']=='ic' and data.get('what') != 'dept-only':
            from predict_ised_sector import predict_sector_ised as pis
            sectors = pis(data.get('text'))['sectors']
            result['sectors'] = sectors
        #data = [data.get('text')]

    # convert data into dataframe
    
#
    # predictions
        #result = {}
        #result['result'] = model.predict(data)[0]
        #result['pct'] = round(model.predict_proba(data).max(),2)

    # send back to browser
    

    # return data
    #return jsonify(results=result[0])
    return jsonify(result)
if __name__ == '__main__':
    app.run(port = 5000, debug=True)