# 2022Fall_assignment2_template
2022Fall_assignment2_template (made by TA: Pohan Wang)

**Due at Oct. 4 11:59 pm**

## Problem sets
Please refer to the Google doc: [LINK][link1]

[link1]: https://docs.google.com/document/d/1yKY06WHkL9MhC-1dU_Odsr2k-vbcIvsW4aNhbT7yMHw/edit




## Files
- `assignment2.py` : This is an empty framework of the code template. Please follow the structure of the pre-defined functions below:

| Method           | Description                                                                             |
|------------------|-----------------------------------------------------------------------------------------|
| `__add__`        | method used for obj1 + obj2                                                             |
| `__init__`       | method for instance a new object from the class                                         |
| `__str__`        | method for print(object)                                                                |
| `Add`            | self defined function for adding                                                        |
| `getRandomValue` | we have prespecified to use random.choice(values) generate random number   from the set |
| `grootNorm`      | return a float by doing grootNorm                                                       |
| `oneNorm`        | return an int by doing oneNorm                                                          |

1. Q1: 
    - Create an `myAwesomeMatrix` class that can handel the arguments as below
    
       ```python
         '''
         kwargs can be :
         n =>  size of nxn matrix NOTE: You can assume if n is passed, i and j won't be
         i =>  number of rows     NOTE: If i is passed, assume j will be too
         j =>  number of columns
         range => [min, max] list 
                     NOTE: Can also be reversed [max,min]
         set   => [number1, ..., numberN]
                     NOTE: If set is specified, use that over range
                     NOTE: If not specified, assume the set is the range
         style => a string which can be anything in {diagonal, upper, lower, symmetric, random}
                     NOTE: Any non-square matrix will be random
                     NOTE: Different styles will always be square matrices
                     NOTE: Use zeroes in the stylized matrices even if not in the given numbers
         format1 => string for formating 1st  element of each row
         format2 => string for formating last element of each row
                     NOTE: If both formats are '', assume the default of no format
                     NOTE: If one format is '', assume the other format is a string that is reversable
         Assume all matrix entries are a single digit (i.e. no 10's 100's, etc)

   - Print out format (refer to the sample outputs of my_mat_tests)
     ```python
     ## print out matrix with newlines between rows
     ## print out elements in rows 1 space apart, with space between the format strings and the values
     ## use the getRandomValue helper function to generate random numbers from an input list
     e.g.:
     myAwesomeMatrix Test 1
     0 0 1 0 
     1 1 1 1 
     0 0 1 0 
     1 1 0 1 

     myAwesomeMatrix Test 6
     cool 0 0 1 0 cool
     cool 1 1 1 1 cool
     cool 0 0 1 0 cool
     cool 1 1 0 1 cool
     ```
2. Q2:

      ```python
      '''Assume all operators will be valid from the set: + - * / ^ ( )
      NOTE: Only 2c will use ()
      Assume all inputs will be valid numbers, operators, or 'q'
      Return answer as a decimal rounded to 1 place 
      ```
- `*.yml`: yml files are our meta file for the testing, be sure to put them under the same folder while testing.
- `my_mat_tests`: the sample outputs of matrix generator are in here.

- `test_assignment2.py` : A test script written with pytest. It is not necessary to run these tests to earn full credit on this assignment, but it is for your benefit as they are similar to how you will be graded.
  - test use command: `!python -m pytest test_assignment2.py` (for spyder's terminal)
  - The way to specify file path depends on OS: L12, 13 provides the format for linux/MacOS, and Windows (just leave the right path format for your python running OS)

    ```python

    path  = os.getcwd() + '/' + 'assignment1.py' #linux, mac user
    # path  = os.getcwd() + '\\' + 'assignment1.py' #windows user

    ```

## Reminders
- Make sure that your submitted code is compilable
- You may import any packages for processing this assignment but do not use any exactly same functions to do the works. (e.g. use `numpy.norm` or any other matrix operation to complete it.). However, our pre-defined packages should be enough for you to obtain the same results.
