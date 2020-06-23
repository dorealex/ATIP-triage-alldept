#this is what was used to train the model for June 2020

import os

import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import FeatureUnion, Pipeline, make_pipeline
from sklearn.svm import LinearSVC

import joblib

file_path = 'ati (7).csv'
df = pd.read_csv(file_path)
df.dropna(inplace=True)


stopwords = text.ENGLISH_STOP_WORDS

X = df['summary_en']
y = df['owner_org']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

word_vectorizer = TfidfVectorizer(stop_words=stopwords)
calibrated_svc = CalibratedClassifierCV(LinearSVC(), method='sigmoid')
pipeline = make_pipeline(word_vectorizer, calibrated_svc)
pipeline.fit(X,y)
print("Model trained, saving")
#joblib.dump(pipeline,"model_full_june2020.jl")
joblib.dump(pipeline,"../models/model_full_June2020.jl", 3) 
