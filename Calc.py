'''
Calc is short for calculator btw
Does 5 basic operations and supports decimals
Has 2 different calculator styles
'''



#basic imports for resources that are used
from time import sleep
import os
import sys
import subprocess
import math
#This is method 1 of the calculator. Python is single threaded so I put this before it is called.
def calc1():
    #"cls" just clears the screen
    os.system('cls')
    #gets the values
    firstnum = float(input("First Number: "))

    operator = input("Input Operator (+,-,*,/,^)\n")
    secondnum = float(input("Second Number: "))
 
    
   
    #does math based on the operator
    if operator == "+":
        result = firstnum + secondnum
    elif operator == "-":
        result = firstnum - secondnum
    elif operator == "*":
        result = firstnum * secondnum
    elif operator == "/":
        result = firstnum / secondnum
    elif operator == "^":
        result = pow(firstnum, secondnum)
    else:
        #what happens if the operator is invalid
        os.system('cls')
        print("OPERATOR INVALID")
        #restarts the program
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
    #shows you the result
    print(result)
    #allows you to do another calculation
    again = input("Another Calculation? Y/N\n")
    if again == "Y" or again == "y":
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
    elif again == "N" or again == "n":
        sys.exit("Bye!")
    else:
        raise Exception("I said Y or N")



#same thing as calc1 on this, but with method 2
def calc2():

    os.system('cls')
    #what this code does up to the if loop is it gets the input, splits it wherever there is a space, and assigns the different list objects to seperate variables
    rawproblem = input("Enter Your First Number, Operator, And Second Number Seperated Spaces (If you encounter any errors double check your formatting)\n")
    problem = rawproblem.split(" ")
    firstnum = float(problem[0])
    
    
    operator = problem[1]
    secondnum = float(problem[2])
    
   
    #same thing as calc1
    if operator == "+":
        result = firstnum + secondnum
    elif operator == "-":
        result = firstnum - secondnum
    elif operator == "*":
        result = firstnum * secondnum
    elif operator == "/":
        result = firstnum / secondnum
    elif operator == "^":
        result = pow(firstnum, secondnum)
    else:
        os.system('cls')
        print("OPERATOR INVALID")
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
    print(result)
    again = input("Another Calculation? Y/N\n")
    if again == "Y" or again == "y":
        subprocess.call([sys.executable, os.path.realpath(__file__)] +
sys.argv[1:])
    elif again == "N" or again == "n":
        sys.exit("Bye!")
    else:
        raise Exception("I said Y or N")

#doesn't acually load lol just for fun
print("Loading Calculator...\n")
sleep(0.3)
#gets the type of calculator you want to use
calctype = input("Would You Like To Use Type 1 or 2?\n")
#logic
if calctype == "1":
    calc1()
elif calctype == "2":
    calc2()

