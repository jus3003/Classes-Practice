## Assignment2 ME369P/ME396P/ES122
## Name: Justin Lam
## EID : JHL2965
## Section: 396P

## Fill in the class and functions below. 
## Make sure your class runs with the tests in main
## You may use any imports, but do not use any import function for 
## norm calculation or matrix operations. Be wary of numpy.


import random
import math
import numpy as np

class myAwesomeMatrix:
    #Initialize Variables for Base Case of Matrix
    n = 0
    i = 4
    j = 4
    set = [0, 1]
    style = 'random'
    range = [0,0]
    format1 = ''
    format2 = ''
           
    def __init__(self, **kwargs):
    
    #Instance matrix generator here
        #Setup Variables
        for key, value in kwargs.items():
            setattr(self, key, kwargs[key])
        
        #Setup matrix row/col dimensions
        if self.n > 0:
            row = self.n
            col = self.n
        else: 
            row = self.i
            col = self.j    
        self.row = row
        self.col = col
       
        #Create Base Array w/ Dimensions
        array = np.zeros(shape = (row,col), dtype = int)
        
        #Convert Numpy Array to List of Lists
        matrix = array.tolist()
        
        #Set Random Values: Prioritize Set Over Range, if No Set or Range Specified then use Default Set [0,1]
        if self.set != [0,1]:
            numbers = self.set
            self.numbers = numbers
        elif self.range != [0,0]:
            maximum = max(self.range)
            minimum = min(self.range)
            numbers = list(range(minimum,maximum+1))
            self.numbers = numbers
        else:
            numbers = self.set
            self.numbers = numbers

        #Edit Matrix Based on Different Shapes
        
        ### Random Matrix  
        if self.style == 'random': 
            for i in range(row):
                for j in range(col):
                        matrix[i][j] = self.getRandomValue(self.numbers)
        
        ### Diagonal Matrix
        if self.style == 'diagonal':
            diagonal_length = row
            i = 0
            j = 0
            while i < diagonal_length:
                matrix[i][j] = self.getRandomValue(self.numbers)
                i += 1
                j += 1

        ### Upper Diagonal Matrix       
        if self.style == 'upper':
            for i in range(row):
                for j in range(i,col):
                    matrix[i][j] = self.getRandomValue(self.numbers)

        ### Lower Diagonal Matrix
        if self.style == 'lower':
            for i in range(row):
                for j in range(0,i+1):
                    matrix[i][j] = self.getRandomValue(self.numbers) 
                    
        ### Symmetric Matrix
        if self.style == 'symmetric':
            for i in range(row):
                for j in range(i,col):
                    matrix[i][j] = self.getRandomValue(self.numbers)
                    matrix[j][i] = matrix[i][j]
        
        #Assign Matrix to Self
        self.matrix = matrix      
        self.output_matrix = matrix

        #Extend Matrix if Format Specified
        if self.format1 or self.format2 != '':
            beginning = str()
            end = str()
            if self.format1 and self.format2 !='':
                beginning = str(self.format1)
                end = str(self.format2)
            elif self.format1 != '': 
                beginning = str(self.format1)
                end = beginning[::-1]
            else: 
                end = str(self.format2)
                beginning = end[::-1]
       
        ### Create Extended Array    
            extended_array = np.empty(shape = (row,col+2), dtype = int)
            extended_matrix = extended_array.tolist()
        
        ### Upload Existing Matrix to Extended Matrix
            for i in range(row):
                for j in range(col):
                    extended_matrix[i][j+1] = matrix[i][j]
                    
        ### Add Formatting
            for i in range(row):
                extended_matrix[i][0] = beginning
                extended_matrix[i][col+1] = end
            
        ### Rewrite Extended Matrix
            self.output_matrix = extended_matrix

    def Add(self, other_matrix):
        # Add another matrix to the current
        
        #Add Matrices without Formatting
        matrix_A = self.matrix
        matrix_B = other_matrix.matrix
        
        ### Create New Added Matrix
        matrix_C_array = np.zeros(shape = (self.row,self.col), dtype = int)
        matrix_C = matrix_C_array.tolist()
        
        ### Add Matrices and Append to New Matrix
        for i in range(self.row):
            for j in range(self.col):
                matrix_C[i][j] = matrix_A[i][j] + (matrix_B[i][j])
        print("")
        
        combined_matrix = matrix_C
        
        #Add Formatting from First String
        
        #Extend Matrix if Format Specified
        if self.format1 or self.format2 != '':
            beginning = str()
            end = str()
            if self.format1 and self.format2 !='':
                beginning = str(self.format1)
                end = str(self.format2)
            elif self.format1 != '': 
                beginning = str(self.format1)
                end = beginning[::-1]
            else: 
                end = str(self.format2)
                beginning = end[::-1]
       
        ### Create Extended Array    
            extended_combined_array = np.empty(shape = (self.row,self.col+2), dtype = int)
            extended_combined_matrix = extended_combined_array.tolist()
        
        ### Upload Existing Matrix to Extended Matrix
            for i in range(self.row):
                for j in range(self.col):
                    extended_combined_matrix[i][j+1] = combined_matrix[i][j]
                    
        ### Add Formatting
            for i in range(self.row):
                extended_combined_matrix[i][0] = beginning
                extended_combined_matrix[i][self.col+1] = end
            
         ### Rewrite Extended Matrix
            new_matrix = extended_combined_matrix
            self.new_matrix = new_matrix
            return '\n'.join(' '.join(map(str, row)) for row in self.new_matrix)
        
        else: 
            new_matrix = combined_matrix
            self.new_matrix = new_matrix
            return '\n'.join(' '.join(map(str, row)) for row in self.new_matrix)
        
        return new_matrix
   
   
   
    def oneNorm(self):
        if self.row == self.col:
            sum_cols = list(0 for i in range(0, self.col))
            for i in range(self.col):
                for j in range(self.row):
                    sum_cols[i] += self.matrix[j][i]
            a_value = max(sum_cols)
        else:
            a_value = 0
            print("ERROR! Matrix is not square")
        return a_value
    
    def grootNorm(self):
        if self.row == self.col:
            sum_integrals = list(0 for i in range(0, self.row))
            
            #Calculate integral for each row
            for i in range(1, self.row+1):
                var_input = self.matrix[i-1][0]
            
                for j in range(2, self.col+1):
                    sum_integrals[i-1] += (var_input**j)/j * self.matrix[i-1][j-1]
                    
            #Sum integrals of all rows
            a_value = round(sum(sum_integrals), 2)
        else:
            a_value = 0
            print("ERROR! Matrix is not square")  
        return a_value
   

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.output_matrix)
    
    def getRandomValue(self,values):
        return random.choice(values)
    
    def __add__(self, other_matrix):
        new_matrix = self.Add(other_matrix)
        return new_matrix
                
    def __lt__(self, other_matrix):
        #Create Two Matrices
        #matrix_A = self.matrix
        matrix_B = other_matrix.matrix
        norm_A = self.oneNorm()
        
        #Copy code from def oneNorm to evaluate norm of matrix B, (Note: doing this since oneNorm only has input 'self', cannot call one Norm for the second matrix)
        sum_cols = list(0 for i in range(0, self.col))
        for i in range(len(matrix_B)):
            for j in range(len(matrix_B)):
                sum_cols[i] += matrix_B[j][i]
        norm_B = max(sum_cols)
        
        #Evaluate if Norm 1 is less than Norm 2 
        if norm_A < norm_B:
            return True
        else:
            return False    

'''
PROBLEM 2
Assume all operators will be valid from the set: + - * / ^ ( )
    NOTE: Only 2c will use ()
Assume all inputs will be valid numbers, operators, or 'q'
Return answer as a decimal rounded to 1 place 
'''
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

def myCalculator2C():
    ## Put code for question 2a in this function
    pass
  
  
if __name__ == '__main__':

    # You may enter your own tests here
    # Nothing in the main function will interfere with grading
    m = myAwesomeMatrix()
    print(m)

    myCalculator2A()
    myCalculator2B()
    myCalculator2C()
