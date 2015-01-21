'''
CS 241 Lab 8

File:        nqueens.py

Description: Implementation of the n-queens problem. Prompts the user for
             the size of the board, searches for a solution, and prints the
             resulting board if a solution was found.
             
             Used Array, ArrayIterator, and Array2D from previous lab.

Created by:  Ulises Giacoman (ugiacoma)
'''

import ctypes 

class _Array:
    ''' Creates an array with size elements. '''
    
    def __init__( self, size ):
        assert size > 0, "Array size must be > 0"
        self._size = size
        # Create the array structure using the ctypes module.
        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()
        # Initialize each element
        self.clear( None )


    def __len__(self ):
        ''' Returns the size of the array '''
        return self._size
    
    
    def __getitem__(self, index):
        ''' Gets the contents of the index element 
        
        Arguments:
        index - Index of item
        '''
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]


    def __setitem__(self, index, value):
        ''' Puts the value in the array element at index position 
        
        Arguments:
        index - Index of item
        value - Value of item to be added to array
        '''
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ] = value


    def clear(self, value):
        ''' Clears the array by setting each element to the given value 
        
        Arguments:
        value - Value to set all elements to
        '''
        for i in range( len(self) ):
            self._elements[i] = value


    def __iter__( self ):
        ''' Returns the array's iterator for traversing the elements '''
        return _ArrayIterator( self._elements )



class _ArrayIterator:
    ''' An iterator for the Array ADT '''
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def next(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration

        
class _Array2D:
    '''  '''
    
    def __init__(self, numRows, numCols):
        self._theRows = _Array(numRows)
        
        for i in range(numRows):
            self._theRows[i] = _Array(numCols)


    def numRows(self):
        ''' Returns the number of rows in the 2-D array '''
        return len(self._theRows)


    def numCols(self):
        ''' Returns the number of columns in the 2-D array '''
        return len(self._theRows[0])

    
    def clear(self, value):
        ''' Clears the array by setting every element to the given value 
        
        Arguments:
        value - Value to set all elements to
        '''
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    
    def __getitem__(self, ndxTuple):
        ''' Gets the contents of the element at position [i, j] 
        
        Arguments:
        ndxTuple - Index of item in 2D array (tuple)
        '''
        assert len(ndxTuple) == 2, "Invalid number of array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]


    def __setitem__(self, ndxTuple, value):
        '''Sets the contents of the element at position [i, j] to value. 
        
        Arguments:
        ndxTuple - Index of item in 2D array (tuple)        
        value - Value of item to be added to 2D array
        '''
        assert len(ndxTuple) == 2, "Invalid number of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
            "Array subscripts out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

class QueensBoard():
    queenCell = 'Q '
    emptyCell = '_ '
    
    def __init__(self, n):
        ''' Creates an n*n empty board. '''
        self._board = _Array2D(n, n)
        self._clear(self.emptyCell)

    def _clear(self, value):
        self._board.clear(value)
    
    def size(self):
        ''' Returns the size of the board '''
        return self._board.numRows()
    
    def numQueens(self):
        ''' Returns the number of queens currently on board '''
        count = 0
        for i in range(self.size()):
            for j in range(self.size()):
                if self._board[i, j] == self.queenCell:
                    count += 1
        return count

    def unguarded(self, row, col):
        '''Returns a boolean value if given cell is unguarded. 
        
        Arguments:
        row - row of Board
        col - column of Board        
        '''
        iRange = range(self.size())
        jRange = range(1, self.size())
        check = ''
        
        for cell in iRange:
            # vertical 
            if cell != row and self._board[cell, col] == self.queenCell:
                return False
            
            else:
                # horizontal
                if cell != col and self._board[row, cell] == self.queenCell:
                    return False
            
        for cell in jRange:   # northwest
            if row - cell < 0 or col - cell < 0:
                check = 'checked'
            else:
                if self._board[row - cell, col - cell] == self.queenCell:
                    return False
            
        for cell in jRange:   # northeast
            if row + cell >= self.size() or col - cell < 0:
                check = 'checked'
            else:
                if self._board[row + cell, col - cell] == self.queenCell:
                    return False            
            
        for cell in jRange:   # southeast
            if row + cell >= self.size() or col + cell >= self.size():
                check = 'checked'
            else:
                if self._board[row + cell, col + cell] == self.queenCell:
                    return False
            
        for cell in jRange:   # southwest
            if row - cell < 0 or col + cell >= self.size():
                check = 'checked'
            else:
                if self._board[row - cell, col + cell] == self.queenCell:
                    return False
            
        return True
    
    def placeQueen(self, row, col):
        ''' Places Queen on board at position (row, col) 
        
        Arguments:
        row - row of Board
        col - column of Board
        '''
        self._board[row, col] = self.queenCell

    def removeQueen(self, row, col):
        ''' Removes Queen from position (row, col) 
        
        Arguments:
        row - row of Board
        col - column of Board        
        '''
        self._board[row, col] = self.emptyCell

    def reset(self):
        ''' Resets board '''
        self._clear(self.emptyCell)

    def draw(self):
        for i in range(self.size()):
            for j in range(self.size()):
                print(self._board[i, j], end='')
            print()


count = 0         
def solveNQueens(board, col):
    ''' Solves for N amount of queens. Will enumerate all solutions.
    
    Arguments:
    board - Size of Board
    col - Starting Column of Queen
    '''
    global count
    if board.numQueens() == board.size():  
        print()
        count += 1
        print('Solution: ', count)
        board.draw()  # Prints board
        return True
    
    else:
        check = False
        for row in range(board.size()):
            if board.unguarded(row, col):
                board.placeQueen(row, col)
                if solveNQueens(board, col + 1): # Recursivly solves for NQueens
                    check = True
                board.removeQueen(row, col)
        return False


def main():
    print()
    boardSize = int(input('Please enter the size of the board: '))  
    board = QueensBoard(boardSize)
    solveNQueens(board, 0)
    
main()