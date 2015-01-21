'''
CS 241 Lab 7

File:        myDeque.py

Description: Python Deque Implentation. The difference between a Queue and
             Deque is that Deque allows for appending an item both in the
             front of the list and end. The difference between a Stack and 
             a Queue is that a Stack is LIFO and Queue is FIFO.

Functions:   isEmpty(), length(), addFirst(), addLast(), removeFirst(),
             removeLast(), peekFirst(), peekLast()

Created by:  Ulises Giacoman (ugiacoma)
'''

class myDeque:
    ''' Creates a new empty deque. '''
    def __init__(self):
        self.deque = list()

    def isEmpty(self):
        ''' Returns a boolean value indicating whether the deque is empty '''
        return (self) == 0
    
    def __len__(self):
        ''' Returns the number of items currently in deque, via len(). '''
        return len(self.deque)
    
    
    def addFirst(self, item):
        ''' Inserts the specified item at the front of this deque. 
        
        Arguments:
        item - the item to be added to the front of the deque
        '''
        self.deque.append(item)
    

    def addLast(self, item):
        ''' Adds the specified item at the back of the deque.
        
        Arguments: 
        item - the item to be added to the back of the deque
        '''
        self.deque.insert(0,item)
    

    def removeFirst(self):
        ''' Removes and returns the first item of this deque. '''
        assert not self.isEmpty(), 'Cannot remove item if queue is empty.'
        return self.deque.pop() 
    
      
    def removeLast(self):
        ''' Removes and returns the last item of the deque. '''  
        assert not self.isEmpty(), 'Cannot remove item if queue is empty.'
        return self.deque.pop(0)       
    
    def peekFirst(self):
        ''' Returns but does not remove the first item of the deque. '''
        if self.isEmpty():
            return None
        else:
            return self.deque[len(self.deque) -1]
        
    def peekLast(self):
        ''' Returns but does not remove the last item of the deque. '''
        if self.isEmpty():
            return None
        else:
            return  self.deque[0]