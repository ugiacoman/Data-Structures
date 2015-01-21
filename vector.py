# CS 241 Lab 2
# vector.py
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                 
# Creates a Vector ADT which uses a modified version of the Array ADT
#

# Imports custom Array ADT
from arrayadt import Array


'''Creates a Vector class'''
class Vector:
     
     ''' Initializes Vector with empty array size = 2''' 
     def __init__(self):
          
          self._myVector = Array[2]
          vector = self._myVector

     '''Returns the number of items contained in the vector'''
     def __len__(self):
          return len(self._myVector)
     
     '''Determines if the given item is containe din the vector'''
     def __contains__(self, item):
          for x in self._myVector:
               if x == item:
                    return True
          return False
     
     '''Returns the item stored in the ndx element of the list.'''
     def getitem(self, ndx):
          if ndx in range(len(self._myVector)):
               return self._myVector[ndx]
          else:
               return 'The index inputed is out of range.'
     
     ''' Sets the element at position nedx to contain the given item'''
     def __setitem__(self, index, item):       
          if ndx in range(len(self._myVector)):
               self._myVector[ndx] = item               
          else:     
               return 'The index inputed is out of range.'
     
     ''' Adds the given item to the end of the list'''
     def append(self, item):
          assert ndx >= 0 and ndx < len(self), "Index out of range"                
          if self.contains(None) == False:
               appendArrayLen = len(self._myVector) * 2
               appendArray = Array(appendArrayLen)
               for eleVect in range(0, len(self._myVector)):
                    appendArray[eleVect] = self._myVector[eleVect]
                    self._myVector = appendArray
          else:
               counter = 0 
               for x in self.vector:
                    if x != None:
                         counter = counter + 1
                    self._myVector[count] = item
     
     '''Inserts the given item in the element at position ndx'''     
     def insert(ndx, item):
          insertArray = Array(length(self._myVector) * 2)
               
          for x in range(0, ndx):
               insertArray[x] = self._myVector[x]
               
          insertArray[ndx] = item
          
          for x in range(ndx, length(self._myVector)):
              insertArray[x + 1] = self._myVector[x]
              
          self._myVector = insertArray          
          
     '''Removes the item from the element from the given ndx position'''
     def remove(ndx):
          removeArray = Array(length(self._myVector))
          
          for x in range(0, ndx):
               removeArray[x] = self._myVector[x]
          number = self._myVector[ndx]
          
          for x in range(ndx, length(self._myVector)):
               removeArray[x - 1] = self._myVector[x]
          self._myVector = removeArray
          return number
     
     '''Returns the index of the vector element containing the given item'''
     def indexOf(self, item):
          if self._myVector.contains(item):
               for z in range(self._myVector):
                    
                    if item == self._myVector[z]:
                         return z
                    
               return 'The item inputed is not on the list.'
          
     '''Extends this vector by appending the entire contents of otherVector'''
     def extend(self, other_myVector):
          self._myVector = self._myVector.append(other_myVector)
     
     '''Creates a new vector that contains a subsequence of items in vector'''
     def sub_myVector(fromndx, to):
          create._myVector = _myVector()
          for x in range (fromndx, to + 1):
               create._myVector.append(self._myVector[x])
          return create._myVector
     
     '''Creates an iterator that can be used to traverse elements of vector'''
     def iterator(self):
          return __iter__ (_myVector)