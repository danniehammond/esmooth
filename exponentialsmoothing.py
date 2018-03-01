# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:27:55 2018

@author: niioto
"""
#exponential smoothing logic
#F(t+1) = (alpha*Yt) + F*(1-alpha)

def exponentialSmoothing(current_values, alpha=0.5):
    """ Exponential Smoothing Function
        takes a list parameter and returns a forecast based on the alpha value. 
        If alpha is not specified a default value of 0.5 is used.
        Reutrns a list of forecast values 
    """
    forecast = []
    for index in range(0,len(current_values)):
        if index==0 or index ==1:
            forecast_value = current_values[0]
            forecast.append(forecast_value)
        else:
            forecast_value = alpha*current_values[index] + (1-alpha)*forecast[index-1]
            forecast.append(forecast_value)
    return forecast

def filename():
    filename = input('Enter filename ... ')
    while filename == '':
        filename = input('Enter filename ... ')
    return filename
def sheetname(): 
    sheetname = input('Enter name of excel sheet containing data ...')
    while sheetname == '':
        sheetname = input('Enter name of excel sheet containing data ...')
    return sheetname
def inputAlpha():
    alpha = float(input('Please enter alpha value in decimal \n between from 0 to 1 ...' ))
    while alpha<0 or alpha>1:
        alpha = float(input('Please enter alpha value in decimal \n between from 0 to 1 ...' ))
    return alpha   
def userSatisfaction():
    user_response = str(input('Are you satisified with the outcome ...? Yes or No' ))
    user_response = user_response.upper()
    while user_response not in ('YES','NO'):
        user_response =  (input('Please input a YES OR a NO')).upper()
    while user_response != 'YES':
        return user_response
    print('Thank you. Program is terminating ....')
    return user_response
