# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:27:55 2018

@author: niioto
"""


def exponentialSmoothing(current_values, alpha=0.5):
    """ Exponential Smoothing Function
        takes a list parameter and returns a forecast based on the alpha value. 
        If alpha is not specified a default value of 0.5 is used.
        Reutrns a list of forecast values
        #exponential smoothing logic
        F(t+1) = (alpha*Yt) + Ft*(1-alpha)
    """
    forecast = [current_values[0]]
    for index in range(1,len(current_values)):
        forecast_value = alpha*current_values[index-1] + (1-alpha)*forecast[index-1]
        forecast.append(round(forecast_value,2))
    return forecast

def filename():
    """Captures excel file name without the extension (.xlsx) from the user"""
    filename = input('Enter filename ... ')
    while filename == '':
        filename = input('Enter name of the excel file ...')
    return 

def sheetname():
    """Captures the name of the excel sheet where data is located"""
    sheetname = input('Enter name of excel sheet containing data ...')
    while sheetname == '':
        sheetname = input('Enter name of excel sheet containing data ...')
    return sheetname

def inputAlpha():
    """Captures alpha value input by user"""
    try:
        alpha = float(input('Please enter alpha value in decimal \n between from 0 to 1 ...' ))
    except:
        alpha = inputAlpha()
    while alpha<0 or alpha>1:
        alpha = float(input('Please enter alpha value in decimal \n between from 0 to 1 ...' ))
    return alpha   

def userSatisfaction():
    """Captures user's satisfaction response and returns response"""
    user_response = str(input('Are you satisified with the outcome ...? Yes or No' ))
    user_response = user_response.upper()
    while user_response not in ('YES','NO'):
        user_response =  (input('Please input a YES OR a NO')).upper()
    return user_response

def sum_of_squares(s):
    """Takes a list of integers or floats and returns sum of squares of the list"""
    return sum(pow(s,2))

def sum_of_product_xy(s,t):
    """Takes two lists of floats or ints and returns sum of their products"""
    product = []
    for i in range(0,len(s)):
      product.append(s[i]*t[i])
    return sum(product)

def linreg(independent_variable,intercept,regression_coefficient):
    """Uses a linear model to predict dependent variable based on the\n
    regression coefficient, independent variable and the value of the \n
    independent variable"""
    dependent_variable = intercept + regression_coefficient*independent_variable
    print('Predicted Stock Value for time period, '+str(independent_variable)+' is : '+str(round(dependent_variable,2)))
    
def inputTime():
    """Captures the independent variable(time period) as an integer from the user"""
    try:
        time = int(input('Please enter time value as an integer ...' ))
    except:
        time = inputTime()
    return time   
    
    