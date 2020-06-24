from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV

import joblib
import numpy as np
model = joblib.load("model_full_June2020.jl")

def predict_dept(text):
    dept = model.predict([text])[0]
    pct = np.round(model.predict_proba([text])[0],2).max()
    d = {'dept':dept,'pct':pct}
    return d