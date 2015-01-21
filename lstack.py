# CS 241 Lab 6
# lstack.py
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                 
# Python Stack Implentation.

# Ask TA about minus having 3 numbers and peek situation


class Stack:
    def __init__(self):
        self._theItems = list()
    
    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0
    
    # Returns the number of items in the stack.
    def __len__(self):
        return len(self._theItems)
    
    # Returns the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]
    
    # Removes and returns the top item on the stack.
    def pop(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems.pop()
    
    # Push an item onto the top of the stack.
    def push(self ,item):
        self._theItems.append(item)