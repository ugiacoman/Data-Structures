'''
CS 241 Lab 9

File:        hashmap.py

Description: Implementation of the HashMap ADT using closed hashing and a 
             probe with single hashing.

             
             Used Array, ArrayIterator, and Array2D from previous lab.

Created by:  Ulises Giacoman (ugiacoma)
'''
from arrayadt import Array

class _MapEntry(object):
    ''' Storage class for holding the key/value pairs. '''
    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashMap:
    ''' Hash Map ADT Implementation '''
    UNUSED = None
    EMPTY = _MapEntry(None, None)

    def __init__(self):
        self._table = Array(7)
        self._count = 0
        self._maxCount = len(self._table) - len(self._table) // 3


    def __len__(self):
        ''' Returns the length of Map'''
        return self._count

    def __contains__(self, key):
        ''' Returns boolean value if key is in Map 
        
        Arguments:
        key - location in Map        
        '''
        slot = self._findSlot(key, False)
        return self._table[slot] is not None
                
   
    def add(self, key, value):
        '''  Adds a new value to the Map if value does not already exist in
             given key. Otherwise, the new value replaces the old value 
             associated with that key.
             
        Arguments:
        key - location in Map
        value - value to be placed in key
        '''
        if key in self:
            slot = self._findSlot(key , False)
            self._table[slot].value = value
            return False
        else:
            slot = self._findSlot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._maxCount:
                self._rehash()
            return True

    def valueOf(self, key):
        ''' Returns value associated with key.
        
        Arguments:
        key - location in Map                
        '''
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key"
        return self._table[slot].value

    def remove(self, key):
        ''' Removes entry associated with given key.
        
        Arguments:
        key - location in Map                
        '''        
        slot = self._findSlot(key, False)
        assert slot is not None, "Invalid map key"
        self._table[slot] = self.EMPTY
        self._count -= 1

    
    def __iter__(self):   
        ''' Returns iterator for traversing map '''
        return _HashTableIterator(self._table)

    def _findSlot(self, key, forInsert):
        ''' Finds slot containing key or where the key may be added; linearly.
            
        Arguments:
        key - location in Map 
        forInsert - indicates if the search is for an insertion, which locates
                    the slot into which the new key can be added.
        '''
        slot = self._hash1(key)
        step = 1 
        while self._table[slot] != self.UNUSED:
            if forInsert and (self._table[slot] == self.UNUSED \
                              or self._table[slot] == self.EMPTY):
                return slot
            elif not forInsert and (self._table[slot] != self.EMPTY and \
                  self._table[slot].key == key):
                return slot
            else:
                slot = (slot + step) 
        return slot
    
    def _rehash(self):
        ''' Rebuilds the hash table. '''
        oriTable = self._table
        newSize = len(self._table) * 2 + 1
        self._table = Array( newSize )

        self._count = 0
        self._maxCount = newSize - newSize // 3

        for entry in oriTable:
            if entry is not self.UNUSED and entry is not self.EMPTY:
                slot = self._findSlot( entry.key, True )
                self._table[slot] = entry
                self._count += 1
    
    def _hash1(self, key):
        ''' main hash function for mapping keys to table '''
        return abs(hash(key)) % len(self._table)

    
    def _hash2(self, key):
        ''' The second hash function used with double hashing probes '''
        return 1 + abs(hash(key)) % (len(self._table) - 2)

class _HashTableIterator:
    ''' Hash Table Iterator '''
    def __init__(self, theArray):
        self._wArray = theArray
        self._curIndex = 0

    def __iter__(self):
        ''' Iterates itself'''
        return self

    def __next__(self):
        """ Traverses to next entry in hash table """
        size = len(self._wArray)
        
        if self._curIndex < size:
            entry = self._wArray[self._curIndex]
            while entry is HashMap.UNUSED or entry is HashMap.EMPTY:
                self._curIndex += 1
                if self._curIndex >= size:
                    raise StopIteration 
                else:
                    entry = self._wArray[self._curIndex]
            self._curIndex += 1
            return entry.key
        else:
            raise StopIteration