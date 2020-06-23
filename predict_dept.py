from sklearn.svm import LinearSVC
#from sklearn.externals import joblib
import joblib
import numpy as np
model = joblib.load("full_model3.jl")

def predict_dept(text):
    dept = model.predict([text])[0]
    pct = np.round(model.predict_proba([text])[0],2).max()
    #pct="ok"
    d = {'dept':dept,'pct':pct}
    return d

print(predict_dept("medical marijuana"))