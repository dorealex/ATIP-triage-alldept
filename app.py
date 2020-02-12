import pandas as pd
from flask import Flask, jsonify, request
import pickle
from sklearn.svm import LinearSVC
from sklearn.externals import joblib

# load model
#model = pickle.load(open('trained_model-[all].pkl','rb'))
model = joblib.load("full_model2.jl")
# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)
    data = [data.get('text')]
    # convert data into dataframe
    

    # predictions
    result = {}
    result['result'] = model.predict(data)[0]
    result['pct'] = round(model.predict_proba(data).max(),2)

    # send back to browser
    

    # return data
    #return jsonify(results=result[0])
    return jsonify(result)
if __name__ == '__main__':
    app.run(port = 5000, debug=True)