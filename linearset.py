# CSCI 241 Lab 3
# Ulises Giacoman
# linearset.py

# Iterator class taken from textbook.

''' Iterator class for Set ADT'''
class _SetIterator:
    
    ''' Initializes Iterator '''
    def __init__(self,theSet):
        self._setRef = theSet
        self._curNdx = 0

    ''' Returns Set '''
    def __iter__(self):
        return self


    ''' Iteratates to the next element in Set'''
    def __next__(self): 
        if self._curNdx < len(self._setRef):
            entry = self._setRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration 

''' Implementation of list based Set ADT '''
class Set: 
    
    ''' Initializes Set ADT'''
    def __init__( self ): 
            self._theElements = list()
  
    ''' Returns length of Set ADT'''
    def __len__( self ): 
        return len( self._theElements )  

    ''' Checks if element is already in set'''
    def __contains__( self, element ): 
        return element in self._theElements 
    
    ''' Adds a new element to the set '''
    def add( self, element ): 
        if element not in self._theElements : 
            self._theElements.append( element )
   
    ''' Removes an element from the set '''
    def remove( self, element ): 
        assert element in self._theElements, 'Element not in set.'
        self._theElements.remove( element ) 
        set_empty = set()
        if set_empty in self._theElements:
            self._theElements.remove(set_empty)
    
    ''' Checks to see whether two sets are identical '''
    def __eq__( self, setB ): 
        if len( self._theElements ) != len( setB ) : 
            return False 
        else : 
            return self.isSubsetOf( setB )
  
    ''' Checks to see whether main set is subset of setB '''
    def isSubsetOf( self, setB ): 
        for element in self: 
            if element not in setB : 
                return False 
        return True   
    
    ''' Creates new set from the union of main set and setB '''
    def union( self, setB ): 
        newSet = Set() 
        newSet._theElements.extend( self._theElements ) 
        for element in setB : 
            if element not in self: 
                newSet._theElements.append( element )
                return newSet 
            
    ''' Creates new set from intersection of main set and setB '''
    def intersect( self, setB ): 
        intersect_set = Set()
        for element in self._theElements:
            if element in setB:
                intersect_set.append(element)
                return intersect_set
    
    ''' Creates new set from difference of main set and setB '''
    def difference( self, setB ): 
        difference_set = Set()
        for element in self._theElements:
            if element not in setB:
                difference_set.append(element)
                return difference_set        
    
    ''' Returns iterator for traversing list of items '''
    def __iter__( self ): 
        return _SetIterator( self._theElements )