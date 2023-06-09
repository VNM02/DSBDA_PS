# -*- coding: utf-8 -*-
"""PS13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jnBL1Tf4gpazpA2PGYYruCq5d_Aldc2M
"""

import pandas as pd 
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data=pd.read_csv('heart.csv')
print(data)

data.describe()

print("Rows := "+str(data.shape[0]))
print("Cols := "+str(data.shape[1]))

null_values=data.isnull().sum()
print(null_values)

corr_matrix = data.corr()
sns.heatmap(corr_matrix, annot=True)

# Check for outliers
z_scores = (data - data.mean()) / data.std()
print(z_scores)

# Remove outliers if any 
data = data[(z_scores < 3).all(axis=1)]

x = data.drop('target', axis=1)
y=data['target']
print(x)

print(y)

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=42)

regression_model = LogisticRegression()
regression_model.fit(X_train, y_train)

y_pred_regression = regression_model.predict(X_test)
regression_accuracy = accuracy_score(y_test, y_pred_regression)
print(y_pred_regression)

print(y_train)

print(regression_accuracy)

knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
y_pred_knn = knn_model.predict(X_test)
knn_accuracy = accuracy_score(y_test, y_pred_knn)
print(y_pred_knn)
print(knn_accuracy)