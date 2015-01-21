# CSCI 241 Lab 3
# Ulises Giacoman
# disjointset.py

from linearset import Set


''' Implementation of Disjoint Set ADT '''
class DisjointSet():
    
    ''' Initialization'''
    def __init__(self):
        self.mainSet = Set()
    
    ''' Returns length of Disjoint Set '''
    def __len__(self):
        return len(self.mainSet)
    
    ''' Checks whether an element is in Set '''
    def __contains__(self, element):
        truthStatement = 0
        for subset in self.mainSet:    
            if element in subset:
                truthStatement = True                
            else:
                truthStatement = False
        return truthStatement 
            
    ''' Adds element to Disjoint Set '''    
    def add(self, element):
        addSet = list()
        for subset in self.mainSet:
            assert element not in subset, "Element not found."
        addSet.append(element)
        self.mainSet.add(addSet)   
        return self.mainSet
    
    ''' Removes element from Disjoin Set '''
    def remove(self, element):
        for subset in self.mainSet:
            if element in subset:
                subset.remove(element)    
                if subset == []:  # If the subset is empty
                    self.mainSet.remove(subset)
                return self.mainSet            
        return False 
    
    ''' If the two elements do not belong to the same subset, a union
    will be performed over the two subsets '''
    def union(self, element1, element2):
        unionSet = Set()
        assert element1 and element2 not in self.mainSet, 'No union.'
        for subset in self.mainSet:
            for itemSubset in self.mainSet:
                if element1 == subset:
                    union_set.add(element1)
                    self.mainSet.remove(subset)
                if element2 == itemSubset: 
                    union_set.add(element2)
                    self.mainSet.remove(itemSubset)
        self.mainSet.add(unionSet)
        return self.mainSet
    
    ''' Returns the subset this element belongs to '''
    def subset(self, element):
        for subset in self.mainSet:
            if element in subset:
                return subset
            else:
                return False