# -*- coding: utf-8 -*-
"""
Created on Tue May 16 10:04:05 2023

@author: 90539
"""

import numpy as np
import pandas as pd
import matplotlib as mp


df=pd.read_csv('data.csv')

#Imputation Missing Values

#kolonlara göre kaç eksik verimiz olduğunu görelim
print(df.isnull().sum())


#ortalama alma yöntemi ile eksik veri tamamlama işlemi
from sklearn.impute import SimpleImputer

'''
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
X =df.iloc[:,1:4].values
imp = imp.fit(X[:,1:4])
X[:,1:4]=imp.transform(X[:,1:4])

print(X)
'''

#median alma yöntemi ile eksik veri tamamlama işlemi
imp = SimpleImputer(missing_values=np.nan, strategy='median')
X =df.iloc[:,1:4].values
imp = imp.fit(X[:,1:4])
X[:,1:4]=imp.transform(X[:,1:4])

print(X)


#most frequent yöntemi ile eksik veri tamamlama işlemi
'''
imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
X =df.iloc[:,1:4].values
imp = imp.fit(X[:,1:4])
X[:,1:4]=imp.transform(X[:,1:4])

print(X)
'''

