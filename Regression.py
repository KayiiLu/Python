# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 13:05:21 2017

@author: Jiayin
"""

'''Week June 18th: Basic Regression'''
import pandas as pd
 #import numpy as np
import statsmodels.api as sm


# from sklearn.linear_model import LinearRegression


#Read data from csv file and return a pandas Dataframe to use later
def csvDF(csvFile):
    df = pd.read_csv(csvFile)
    return df
    
#Get column names and return a list of column names
def columnNames (dataframe):
    return list(dataframe)

#Read Column Names and make a data frame
def frameFromCol (listOfNames, dataframe):
    NewDf = dataframe[listOfNames]
    return NewDf
    
  
#Summary Statistics for every column in a dataframe  
def summary_stat(df):
    return df.describe()    

#Regression: 
#y is the target data, dependent variable; 
#x can be multiple variables, are the festures/independent variables

#x and y are dataframes, contant = True pre-set the intercept != 0; if =0 need to type in False
def regression(y, x, constant = True):
    if constant == True:
        X = sm.add_constant(x)
    else:
        X = x
        
    results = sm.OLS(y, X).fit()
    return results

import matplotlib.pyplot as plt











#Testing Regression functions
df = csvDF('mydata.csv')
#Inspect the first five lines of the data
df.head()
#Define independent variables and dependent variables and form new dataframes
x =  df[['COUNT FEMALE', 'COUNT PACIFIC ISLANDER', 'COUNT AMERICAN INDIAN']]
y = df[['COUNT PUBLIC ASSISTANCE TOTAL']]
#Do regression on x and y dataframes
results = regression(y, x)
#Look at summary statistics of regression
results.summary()   #Note: many choices to call here 
results.rsquared
'''
If want to use the trained model to predict y using some new dataframe x2, can use
results.predict(x2)
'''

#Testing Summary_stat for columns in a dataframe
summary_stat(x)

'''Also, maybe make one for dummy variables
    And consider plots with y and x1, x2, x3... etc'''


