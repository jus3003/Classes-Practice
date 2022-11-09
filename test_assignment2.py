##
## Unit tests for ME369P/396P/ES122 Fall 2022 Assignment 2
##

import pytest
import importlib
import os
import io
import sys
import random
import yaml
import traceback

path  = os.getcwd() + '/' + 'assignment2.py' #linux, mac user
# path  = os.getcwd() + '\\' + 'assignment2.py' #windows user
spec = importlib.util.spec_from_file_location("assignment2", path)
my_script = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(my_script)
    print("PASS: SCRIPT IS EXECUTABLE")
except Exception as ex:
    print('\n\nFAIL: EXCEPTION THROWN WHILE RUNNING FUNCTION:')
    print(type(ex).__name__,': ',ex, end='\n\n', sep='')
except:
    print('\n\nFAIL: NON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


def test_myAwesomeMatrix():
    # redirect student stdout

    with open('matrix.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
        
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            test_output = specs['output']
            random.seed(1)




            my_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = my_output

            print(test_name)
            kwargs1 = test_input

            try:
                m = my_script.myAwesomeMatrix(**kwargs1)
                if 'input2' in specs:
                    kwargs2 = specs['input2']
                    m2 = my_script.myAwesomeMatrix(**kwargs2)
                    matComp = specs['matComp']
                    if matComp == 'Add':
                        print(m.Add(m2))
                    elif matComp == '+':
                        print(m + m2)
                    else:
                        print(m < m2)
                elif 'norm' in specs:
                    print('One Norm')
                    print(m.oneNorm())
                    print('Groot Norm')
                    print(m.grootNorm())
                else:
                    print(m)
            except Exception as ex:
                print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                print(traceback.format_exc())
            except:
                print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


            #stdout is to console again
            sys.stdout = old_stdout
            my_output = my_output.getvalue()

            with open(test_output, 'r') as expected_out:
                expected_out = expected_out.read()

            assert expected_out in my_output

def test_myCalculator2A():
    # redirect student stdout
    random.seed(1)

    with open('calculator_2a.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
        
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            test_output = specs['output']


            print(test_name)
            print(test_input)
            print(test_output)
            old_stdin = sys.stdin
            s = io.StringIO(test_input)
            sys.stdin  = s

            my_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = my_output

            try:
                my_script.myCalculator2A()
            except Exception as ex:
                print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                # print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                print(traceback.format_exc())
            except:
                print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


            sys.stdin = old_stdin
            #stdout is to console again
            sys.stdout = old_stdout
            my_output = my_output.getvalue()

            assert str(test_output) in my_output

def test_myCalculator2B():
    # redirect student stdout
    random.seed(1)

    with open('calculator_2b.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
        
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            test_output = specs['output']


            print(test_name)
            print(test_input)
            print(test_output)
            old_stdin = sys.stdin
            s = io.StringIO(test_input)
            sys.stdin  = s

            my_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = my_output

            try:
                my_script.myCalculator2B()
            except Exception as ex:
                print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                # print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                print(traceback.format_exc())
            except:
                print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


            sys.stdin = old_stdin
            #stdout is to console again
            sys.stdout = old_stdout
            my_output = my_output.getvalue()

            assert str(test_output) in my_output

def test_myCalculator2C():
    # redirect student stdout
    random.seed(1)

    with open('calculator_2c.yml', 'r') as tests:
        tests = yaml.load(tests, Loader=yaml.FullLoader)
        
    for testcase in tests:
        for testname, specs in testcase.items():
            test_name = specs['name']
            test_input = specs['input']
            test_output = specs['output']


            print(test_name)
            print(test_input)
            print(test_output)
            old_stdin = sys.stdin
            s = io.StringIO(test_input)
            sys.stdin  = s

            my_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = my_output

            try:
                my_script.myCalculator2C()
            except Exception as ex:
                print('\n\nEXCEPTION THROWN WHILE RUNNING FUNCTION:')
                # print(type(ex).__name__,': ',ex, end='\n\n', sep='')
                print(traceback.format_exc())
            except:
                print('\n\nNON-STANDARD EXCEPTION THROWN WHILE RUNNING FUNCTION\n\n') 


            sys.stdin = old_stdin
            #stdout is to console again
            sys.stdout = old_stdout
            my_output = my_output.getvalue()

            assert str(test_output) in my_output