# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10QIKLc3DuUtisGwgfvqSKVs460VC7J56
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression

data=fetch_california_housing()
X=data.data
y=data.target

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(x_train,y_train)

score_train_val=model.score(x_test,y_test)
print(f'Train/Validation score:{score_train_val}')

score_cv=cross_val_score(LinearRegression(),x,y,cv=10)
print(f'Cross-validation score:{score_cv}')
print(f'Averrage Cross-Validation score:{np.mean(score_cv)}')

#vitulize score
plt.figure(fidgsize=(12,6))
plt.bar(range(1,11),scores_cv,color='Gray',label='cross validation score')