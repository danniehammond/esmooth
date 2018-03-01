# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:45:06 2018

@author: daniel hammond
"""
import pandas as pd 
import support_library as sl # Custom Supporting Library
import matplotlib.pyplot as pp
import sys as s

#import data from excel file
#---------------------------
excel_filename = sl.filename()+'.xlsx'
excel_sheetname = sl.sheetname()
try:
    df = pd.read_excel(excel_filename, sheetname = excel_sheetname)
except FileNotFoundError:
    print('We could not find your file...\nProgram is terminating')
    s.exit('Program Terminated') #program exits when the file is not found
except:
    print('The name of your excel sheet was not found...\nProgram is terminating')
    s.exit('Program Terminated') #program exits when the sheet is not found

#Exponential Smoothing
#---------------------
user_satisfaction = 'NO'
while user_satisfaction == 'NO':
    alpha = sl.inputAlpha()
    df['forecast'] = sl.exponentialSmoothing(df['value'],alpha)
    timeline = [51,51,51,51,51,51,51,51]
    print(df)
    x = df['time period']
    y = df['value']
    f = df['forecast']
    pp.plot(x,y)
    pp.plot(x,f)
    pp.plot(x,timeline, label='Time Period')
    pp.axis('auto')
    pp.ylabel('Stock Value')
    pp.xlabel('Time')
    pp.legend()
    pp.show()
    t9 = (alpha*df['value'].iloc[-1])+(1-alpha)*df['forecast'].iloc[-1]
    print('With an alpha value of '+str(alpha)+', the Forecast value for period 9 is '+str(round(t9,2)))
    user_satisfaction = sl.userSatisfaction()

#Regression Analysis
#-------------------
sigma_x = sum(x) #sum of indepedent variable x
sigma_y = sum(y) #sum of dependent variable y
n = x.count() #number of observations
sigma_x_squared = sl.sum_of_squares(x) #sum of squares for x
sigma_y_squared = sl.sum_of_squares(y) #sum of squares for y
sigma_xy = sl.sum_of_product_xy(x,y)

#regression coefficient b
#------------------------
regression_coefficient = (n*sigma_xy - (sigma_x*sigma_y))/(n*sigma_x_squared - sigma_x**2)
print('Regression coefficient : '+ str(regression_coefficient))

#Intercept
#---------
intercept = (sigma_y*sigma_x_squared-sigma_x*sigma_xy)/(n*sigma_x_squared - sigma_x**2)
print('Intercept: ' + str(intercept))

#Regession model
#---------------
print('Regression Model :\n'+'Y = '+str(intercept)+' + '+str(regression_coefficient)+'*X')

#Predicting stock value based on time value
#-------------------------------------------
time_value = sl.inputTime() 
sl.linreg(time_value,intercept,regression_coefficient)

# Correlation coefficient
print('Correlation coefficient : '+str(round(x.corr(y),2)))
