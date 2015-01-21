# CS 241 Lab 2
# ppmimageadt.py
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                 
#
# In union with ppmtest.py, this file provides the structure of the flag file

# Imports custom Array2D ADT 
from arrayadt import Array2D

class PPMImage():
    
    '''Creates 2D array'''
    def __init__(self, width, height):
        self.width = width
        self.height = height 
        self.flag_array = Array2D(height, width)
    
    '''Sets the element at position ndxTuple'''
    def __setitem__(self,ndxTuple, value):
        self.flag_array[ndxTuple] = value
       
    '''Returns the ndxTuple Stored'''
    def __getitem__(self, ndxTuple):
        return self.flag_array[ndxTuple]
     
    '''Writes Flag into separate file'''
    def writeToFile(self,filename):
        flagPic = open(filename, 'wb')
        header = "P6\n%d %d 255\n" % (self.width, self.height)
        flagPic.write(bytes(header, "utf-8"))    # UTF-8
        
        for x in range(self.height):
            for y in range(self.width):
                flagPic.write(bytes(self[x,y])) # String to bytes
        flagPic.close()
                
            
        
               
        