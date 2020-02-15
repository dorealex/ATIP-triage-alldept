import joblib
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
stopwords = text.ENGLISH_STOP_WORDS
from sklearn.neural_network import MLPClassifier
model = joblib.load('ISED_SECTOR.jl')

def predict_sector_ised(text):
    y_cols = ['AEB', 'CB', 'CIO', 'CIPO', 'CMS',
       'DMO', 'DTSS', 'IC', 'IS', 'MIN', 'OCS', 'OCSA', 'SBMS', 'SCMS', 'SIPS',
       'SRS', 'STS']
    pct = list(np.round(model.predict_proba([text]),2)[0])
    r = dict(zip(y_cols,pct))
    return r