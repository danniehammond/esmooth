# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 21:14:32 2018

@author: niioto
"""

import pandas as pd
df = pd.read_excel('data.xlsx', sheetname='data')
print(df['time period'])
#print(df.loc[:,'forecast'])
#sum_y = sum(df['forecast'])
#print(sum_y)
#a = [5,2,1,3,4]
#a.sort()
#print(a)
#L=[1, 2, 7, 3, 4, 12]
#print(max(L))
#L1=[ [ 1, 4, 3 ], [ 5, 6, 7, 9 ] ]
#print(L1[ 1 ][ 2 ])

print(sum(pow(df['time period'],2)))
def sum_of_squares(s):
    return sum(pow(s,2))

def sum_of_product_xy(s,t):
    product = []
    for i in range(0,len(s)):
      product.append(s[i]*t[i])
    return sum(product)
    
#print(sum_of_squares(df['forecast']))
x = df['time period']
y = df['value']



sigma_x = sum(x) #sum of indepedent variable x
sigma_y = sum(y) #sum of dependent variable y
n = x.count()
sigma_x_squared = sum_of_squares(x) #sum of squares for x
sigma_y_squared = sum_of_squares(y) #sum of squares for y
sigma_xy = sum_of_product_xy(x,y)
#regression coefficient b 
#b = (x.count()*(sum_product_xy) - (sum(x)*sum(y))) / (x.count()*sum(x**2) - sum(x)**2)

regression_coefficient = (n*sigma_xy - (sigma_x*sigma_y))/(n*sigma_x_squared - sigma_x**2)
print('regression coefficient : '+ str(regression_coefficient))
intercept = (sigma_y*sigma_x_squared-sigma_x*sigma_xy)/(n*sigma_x_squared - sigma_x**2)
print('intercept: ' + str(intercept))

#regression model dependent_variable = intercept + regression_coefficient*independent_variable
def forecast(independent_variable):
    dependent_variable = intercept + regression_coefficient*independent_variable
    print('Y is : '+str(dependent_variable))
forecast(float(input('Enter the stock value in decimal: ')))
#correlation coefficient
corr = df['time period'].corr(df['value'])
print(round(corr,2))