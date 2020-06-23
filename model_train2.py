import numpy as np
import pandas as pd
file_path = 'https://open.canada.ca/data/dataset/0797e893-751e-4695-8229-a5066e4fe43c/resource/19383ca2-b01a-487d-88f7-e1ffbc7d39c2/download/ati.csv'
df = pd.read_csv(file_path)
df.dropna(inplace=True)
from sklearn.svm import LinearSVC
from sklearn import metrics
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split
from sklearn.calibration import CalibratedClassifierCV
stopwords = text.ENGLISH_STOP_WORDS
import pickle
X = df['summary_en']
y = df['owner_org']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
isotonic_svc = CalibratedClassifierCV(
    base_estimator=LinearSVC(),
    method='isotonic') # isotonic calibration
text_clf = Pipeline([('tfidf',TfidfVectorizer(stop_words=stopwords)),
                    ('clf', isotonic_svc)])
#text_clf.fit(X_train, y_train)
#predictions = text_clf.predict(X_test)

text_clf.fit(X, y)

pickle.dump(text_clf, open('trained_model-[all]_full_train.pkl','wb'))
#from sklearn.externals import joblib
#joblib_file = 'jl_model.pkl'
#joblib.dump(text_clf,joblib_file)

#import _pickle as cPickle
#cPickle.dump(text_clf, open('trained_model-[all].pkl','wb'))