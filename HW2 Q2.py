# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:44:41 2022

@author: jusxp
"""

def myCalculator2A():

    expression = str()
    expression = input("Enter expression: ")
    
    while expression != 'q':
        expression_string = expression.split(" ")
        
        while len(expression_string) > 1:
            
            a = float(expression_string[0])
            b = float(expression_string[2])
            
            if expression_string[1] == '+':
                result = a + b
            elif expression_string[1] == '-':
                result = a - b
            elif expression_string[1] == '*':
                result = a*b
            elif expression_string[1] == '/':
                result = a/b
            elif expression_string[1] == '^':
                result = a**b
            else:
                print("expression not valid")
            
            expression_string[2] = result
            expression_string.pop(0)
            expression_string.pop(0)
             
        print(round(expression_string[0], 1))
        expression = input("Enter expression: ")          
        

def myCalculator2B():    
    myCalculator2A()
    
            
#myCalculator2A()
#myCalculator2B()  
#myCalculator2C()     