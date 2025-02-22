# -*- coding: utf-8 -*-
"""assignment-2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b2h9TjncCK5yI9nH__avvrxYeKgVe2tU

Shaikh Amaan
2019BTECS00076
ASSIGNMENT 2 SET LAB

Linear Regression
"""

# importing libs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')

# reading dataset
dataset = pd.read_csv("/content/drive/My Drive/assignments/Setl/setl-assg-2.csv")

dataset

#ignoring a few null values from the dataset.
dataset = dataset[~dataset['BMI'].isnull()] 
X = dataset.iloc[:, [0,8,3,6]].values #select SEX,BMI,AGE,CURSMOKE #,3,6
y = dataset.iloc[:, 4].values #select SYSBP

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder

labelencoder = LabelEncoder()
X[:, 0] = labelencoder.fit_transform(X[:, 0])

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting Multiple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X)

print( 'R-squared: %.2f' % regressor.score(X_test, y_test))
print (regressor.coef_)

fig, ax = plt.subplots()
ax.set_xticks([18.5, 24.9, 29.9], minor=False) #important values of BMI
ax.set_yticks([120, 130, 140, 180], minor=False) #important values of SysBP
ax.xaxis.grid(True, which='major',linewidth='0.5', color='red')
ax.yaxis.grid(True, which='major',linewidth='0.5', color='blue')

plt.scatter(X[:,1], y_pred, marker='.')
plt.ylabel("Systolic blood pressure")
plt.xlabel("BMI")
plt.show()