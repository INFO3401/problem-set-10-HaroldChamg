import pandas as pd
import numpy as np
import csv 
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score


#Woked with Steve, Andrew, Lucas, Annastasia



class AnalysisData:


    def __init__(self):
        self.dataset = []
        self.variables = []
    def parseFile (self, filename):
        self.dataset = pd.read_csv(filename)
        for column in self.dataset.columns.values:
            if column != "competitorname": 
                self.variables.append(column)  
                
class LinearAnalysis:
    def __init__ (self, _targetY):
        self.targetY = _targetY
        self.bestX = ""
        
    def runSimpleAnalysis(self, data):
        best_r2 = -1
        best_variable = ""
        for column in data.variables:
            if column != self.targetY:
                inde_variable = data.dataset[column].values
                inde_variable = inde_variable.reshape(len(inde_variable),1)
                regression = LinearRegression()
                regression.fit(inde_variable, data.dataset[self.targetY])
                predict = regression.predict(inde_variable)
                r_score = r2_score(data.dataset[self.targetY],predict)
            if r_score > best_r2:
                best_r2 = r_score
                best_variable = column
        self.bestX = best_variable
        print(best_variable, best_r2)

data = AnalysisData()
data.parseFile("candy-data.csv")

final_analysis = LinearAnalysis('sugarpercent')
final_analysis.runSimpleAnalysis(data)




# Monday Wednesday Problem


class LogisticAnalysis:
    def __init__(self,targetY):
        self.bestX = ""
        self.targetY = targetY
        self.fit = ""
        
    def runSimpleAnalysis1(self, data):
        best_sugar_variable = ""
        best_r2 = -1
        
        for column in data.variables:
            if column != self.targetY:
                data_variable=data.dataset[column].values
                data_variable=data_variable.reshape(len(data_variable),1)
                
                regre = LinearRegression()
                regre.fit(data_variable, data.dataset[self.targetY])
                
                prediction = regre.predict(data_variable)
                
                r_score = r2_score(data.dataset[self.targetY], prediction)
                if r_score > best_r2:
                    best_r2 = r_score
                    best_sugar_variable = column
        
                self.bestX = best_sugar_variable

                print(best_sugar_variable, best_r2)
                print('Simple Logistic Regression Analysis coefficients: ', regre.coef_)
                print('Simple Logistic Regression Analysis intercept: ', regre.intercept_)




# From the code that I have, they found the different optimal variables.
# When running linear analysis it prints out pricepercent 0.10870630201695808, while when running LogisticAnalysis it prints out Fruit 0.5501501291324922 . So on my computer logistics analysis performes better in this case.

def runMultipleRegression(self, data):
    multi_regre = LogisticRegression()
    mp_regre = [val for val in data.variables if val != self.targetY]
    multi_regre.fit(data.dataset[mp_regre], data.dataset[self.targetY])

    prediction = multi_regre.predict(data.dataset[mp_regre])
    r_score = r2_score(data.dataset[self.targetY],variable_prediction)

            
    print(fruitlv, r_score)
    print('Multiple Regression Analysis coefficients: ', regre.coef_)
    print('Multiple Regression Analysis intercept: ', regre.intercept_)

data = AnalysisData()
data.parseFile("candy-data.csv")


data_analysis = LogisticAnalysis("chocolate")
data_analysis.runSimpleAnalysis1(data)


data_analysis = LogisticAnalysis("chocolate")
data_analysis.runMultipleRegression(data)

#I would say multi test performs better than simple test(around 30 percent better)
#When using multiple testing, there are multiple independent variables are tested at once, which increases the accuracy of the testing.


#Equation

##Linear Regression y = b0 + b1x
#Logistic Regression p = 1/1+e^-(b0+b1x)
#Multiple Regression p = 1/1+e^-(b0+b1x+b2x+b3x+...)

#Linear Regression Equation y = -0.73964166 + 0.7659574468085104x


#Logistic Regression Equation p = 1/1+e^-(0.33400402 +  0.3802816901408451x)

#Multiple Regression Equation p = 1/1+e^-( 0.50503018+ 0.35211267605633806x +0.45970696 + 0.39743589743589747x +0.61538462 + 0.38461538461538464x + -0.44761905 + 0.5142857142857143x + -0.33702882 +0.6097560975609756x)


# Friday problem

#dependent = things that you wanna know
#independent = things that are compared

#independent= Caramel and Chocolate, they are Categorical Variable
#dependent= sugar percent, that is a Continous variable
#null hypothesis:  Caramel and chocolate have the same amount of sugar percent.

#independent= Blue and Red States,they are Categorical variable
#dependent= number of split ticket holders Discret variable(you cant have 0.5 voter)
#null hypothesis: Blue and Red states have the same amount of split ticket holders


#independent= battery life(Continous variable)
#dependent= selling rate(Continous variable)
#null hypothesis: Batteries performances wouldnt affect the sales rate.





























