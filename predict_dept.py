from sklearn.svm import LinearSVC
#from sklearn.externals import joblib
import joblib
import numpy as np
model = joblib.load("full_model2.jl")

def predict_dept(text):
    dept = model.predict([text])[0]
    pct = np.round(model.predict_proba([text])[0],2).max()
    d = {'dept':dept,'pct':pct}
    return d