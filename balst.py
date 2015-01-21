'''
CS 241 Extra Lab

File:        balst.py

Description: Balanced Search Tree Implemenation (AVL TREE)
             
Created by:  Ulises Giacoman (ugiacoma)
'''

LEFT_HIGH  = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1

class MyBalST:
    """Implementation of a Balanced Search Tree using an AVL tree """
    def __init__(self):
        self._root = None
        self._size = 0
    
    def insert(self, key):
        """ Add new entry to the map or replaces the value of an existing key
        
        Arguments:
        key - value to be inserted        
        """
        node = self._bstSearch(self._root, key)
        if node is not None:
            return False
        else:
            (self._root, _) = self._avlInsert(self._root, key)
            self._size += 1
            return True

    def search(self, key):
        ''' Searches for key in balanced search tree, returns True if found
        
        Arguments:
        key - value to be inserted        
        '''
        if (self._bstSearch(self._root, key)):
            return True

    def _bstSearch(self, subtree, target):
        """Helper method recursively searching the tree for a target key.
        
        Arguments:
        subtree - node that contains values in structural subtree form
        target - key to be looked for
        """
        if subtree is None:
            return None
        elif target < subtree.key:
            return self._bstSearch(subtree.left, target)
        elif target > subtree.key:
            return self._bstSearch(subtree.right, target)
        else:
            return subtree
        
    def _avlInsert(self, subtree, key):
        """Recursive method to handle the insertion into an AVL tree. The
        function returns a tuple containing a reference to the root of the
        subtree and a boolean to indicate if the subtree grew taller 
        
        Arguments:
        subtree - node that contains values in structural subtree form
        key - value to be inserted
        """
        if subtree is None:
            subtree = _AVLMapNode(key)
            taller = True
        elif key == subtree.key:
            taller = False
        elif key < subtree.key:
            (subtree.left, taller) = self._avlInsert(subtree.left, key)
            if taller:
                if subtree.bfactor == LEFT_HIGH:
                    subtree = self._avlLeftBalance(subtree)
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = LEFT_HIGH
                    taller = True
                else: 
                    subtree.bfactor = EQUAL_HIGH
                    taller = False
        else:  
            (subtree.right, taller) = self._avlInsert(subtree.right, key)
            if taller:
                if subtree.bfactor == LEFT_HIGH:
                    subtree.bfactor = EQUAL_HIGH
                    taller = False
                elif subtree.bfactor == EQUAL_HIGH:
                    subtree.bfactor = RIGHT_HIGH
                    taller = True
                else: 
                    subtree = self._avlRightBalance(subtree)
                    taller = False
        return (subtree, taller)

    def _avlLeftBalance(self, pivot):
        """Rebalance a node when its left subtree is higher. 
        
        Arguments:
        pivot - node that stores directional information (left,right) depending
                on balancing case        
        """
        ccc = pivot.left

        if ccc.bfactor == LEFT_HIGH:
            pivot.bfactor = EQUAL_HIGH
            ccc.bfactor = EQUAL_HIGH
            pivot = self._avlRotateRight(pivot)
            return pivot
        elif ccc.bfactor == EQUAL_HIGH:
            pivot.bfactor = LEFT_HIGH
            ccc.bfactor = RIGHT_HIGH
            pivot = self._avlRotateRight(pivot)
            return pivot
        else:
            ggg = ccc.right
            if ggg.bfactor == LEFT_HIGH:
                pivot.bfactor = RIGHT_HIGH
                ccc.bfactor = EQUAL_HIGH
            elif ggg.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                ccc.bfactor = EQUAL_HIGH
            else:
                pivot.bfactor = EQUAL_HIGH
                ccc.bfactor = LEFT_HIGH
                
            ggg.bfactor = EQUAL_HIGH

            pivot.left = self._avlRotateLeft(ccc)
            pivot = self._avlRotateRight(pivot)
            return pivot

    def _avlRightBalance(self, pivot):
        """ Rebalance a node when its right subtree is higher 
        
        Arguments:
        pivot - node that stores directional information (left,right) depending
                on balancing case        
        """
        ccc = pivot.right
        if ccc.bfactor == RIGHT_HIGH:
            pivot.bfactor = EQUAL_HIGH
            ccc.bfactor = EQUAL_HIGH
            pivot = self._avlRotateLeft(pivot)
            return pivot
        elif ccc.bfactor == EQUAL_HIGH:
            pivot.bfactor = RIGHT_HIGH
            ccc.bfactor = LEFT_HIGH
            pivot = self._avlRotateLeft(pivot)
            return pivot
        else:  
            ggg = ccc.left
            if ggg.bfactor == LEFT_HIGH:
                pivot.bfactor = EQUAL_HIGH
                ccc.bfactor = RIGHT_HIGH
            elif ggg.bfactor == EQUAL_HIGH:
                pivot.bfactor = EQUAL_HIGH
                ccc.bfactor = EQUAL_HIGH
            else:
                pivot.bfactor = LEFT_HIGH
                ccc.bfactor = EQUAL_HIGH
                
            ggg.bfactor = EQUAL_HIGH
            
            pivot.right = self._avlRotateRight(ccc)
            pivot = self._avlRotateLeft(pivot)
            return pivot

    def _avlRotateRight(self, pivot):
        """ Rotate the pivot to the right around its left child
        
        Arguments:
        pivot - node that stores directional information (left,right) depending
                on balancing case        
        """
        ccc = pivot.left
        pivot.left = ccc.right
        ccc.right = pivot
        return ccc

    def _avlRotateLeft(self, pivot):
        """ Rotates the pivot to the left around its right child.
        
        Arguments:
        pivot - node that stores directional information (left,right) depending
                on balancing case
        """
        ccc = pivot.right
        pivot.right = ccc.left
        ccc.left = pivot
        return ccc

class _AVLMapNode:
    """ Storage class for creating the AVL tree node """
    def __init__(self, key):
        self.key = key
        self.bfactor = EQUAL_HIGH
        self.left = None
        self.right = None