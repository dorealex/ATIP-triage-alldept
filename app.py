import pandas as pd
from flask import Flask, jsonify, request
import pickle
from sklearn.svm import LinearSVC

# load model
model = pickle.load(open('trained_model-[all].pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)
    data = list(data.get('text'))
    # convert data into dataframe
    

    # predictions
    result = model.predict(data)

    # send back to browser
    

    # return data
    return jsonify(results=result[0])

if __name__ == '__main__':
    app.run(port = 5000, debug=True)