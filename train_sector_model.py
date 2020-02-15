import numpy as np
import pandas as pd
data_file = 'ised_atip_clean-23-Jan.csv'
df = pd.read_csv(data_file)
blanks = []  # start with an empty list
x = len(df['summary text'])
for i in range(0,x):
  val = df['summary text'].iloc[i]
  if type(val)==str:
    if val.isspace():
      blanks.append(i)
df.drop(blanks,inplace=True)
X = df['clean']
y_cols = ['AEB', 'CB', 'CIO', 'CIPO', 'CMS',
       'DMO', 'DTSS', 'IC', 'IS', 'MIN', 'OCS', 'OCSA', 'SBMS', 'SCMS', 'SIPS',
       'SRS', 'STS']
y = df[y_cols]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier, ExtraTreeClassifier
from sklearn.feature_extraction import text
stopwords = text.ENGLISH_STOP_WORDS
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import label_ranking_average_precision_score
from sklearn.metrics import coverage_error
text_clf = Pipeline([('tfidf',TfidfVectorizer(stop_words=stopwords)),
                     ('clf', MLPClassifier(max_iter=1000))])
text_clf.fit(X_train, y_train)
predictions = text_clf.predict(X_test)
from sklearn.metrics import classification_report
print(classification_report(y_test,predictions, target_names=y_cols))
text_clf.fit(X,y)
from sklearn.externals import joblib
joblib.dump(text_clf,'ISED_SECTOR.jl')