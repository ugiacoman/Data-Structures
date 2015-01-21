# CS 241 Lab 6
# esolver.py
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
# 
# This esolver will evaluate Postfix and Prefix expressions.
# Example Postfix expression: 2 3 4 + -
# Example Prefix expression: - + 2 3 4

from lstack import Stack

''' Evaluates a PostFix Expression'''
def evalPostfix(postfixExpression):
    myStack = Stack()
    valueList = postfixExpression.split()
    
    for item in valueList:
        if item not in "+/-*":
            myStack.push(float(item))
        else:
            if not myStack.isEmpty():
                x = myStack.pop()
                if myStack.isEmpty():
                    return None
                else:
                    y = myStack.pop()
                    if item == "+":
                        result = x + y
                    elif item == "-":
                        result = y - x
                    elif item == "*":
                        result = x * y
                    else:
                        result = y / x
                    myStack.push(result)
            else:
                return None
    value = myStack.pop()    
    return value

''' Evaluates a Prefix Expression'''
def evalPrefix(prefixExpression):  
    myStack = Stack()
    valueList = prefixExpression.split()
    valueList.reverse()                 # Reverses List for Postfix evaluation
    
    for item in valueList:
        if item not in "+/-*":
            myStack.push(float(item))
        elif not myStack.isEmpty():
            x = myStack.pop()
            if myStack.isEmpty():
                return None    
            else:
                y = myStack.pop()
                if item == "+":
                    result = x + y
                elif item == "-":
                    result = x - y          # Switches x and y for reversal exception
                elif item == "*":
                    result = x * y
                else:
                    result = x / y          # Switches x and y for reversal exception
                myStack.push(result)
        else:
            return None         
    value = myStack.pop()      
    return value