# CS 241 Lab 5
# GList.py
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                 
#
# A Python Implementation of a Doubly Linked List.
# Has the following operations: length, contains, append, clear, findNext,
# findPrevious, get, getFirst, getLast, getNext, getPrevious, insert, prepend,
# and remove.

''' Storage Class'''
class DoubleListNode:
    def __init__(self, node):
        self.node =  node
        self.prev = None
        self.next = None 

''' Doubly Linked List Implementation '''
class GList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.cNode = None
        self.size = 0  
    
    ''' Returns Size of List '''
    def __len__(self):
        return self.size
        
    ''' Returns whether node is in list, if not returns None '''    
    def __contains__ (self, node):
        self.cNode = self.head
        
        assert self.cNode.node == node, "Data not here."
        while self.cNode is not None and self.cNode.node != self.node :
            if self.cNode.node == node:
                self.cNode = self.cNode.prev.next
                return True
            elif self.cNode == self.tail:
                self.cNode = None
                return False 
            else:
                self.cNode = self.cNode.next
            
        
    ''' Adds a new node to the end of the list '''
    def append(self, node):
        newnode= DoubleListNode(node)
        self.size += 1
        
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        elif node < self.head.node:
            newnode.next = self.head
            self.head.prev= newnode
            self.head= newnode
        elif node > self.tail.node:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        else:
            self.cNode = self.head
            while self.cNode is not None and self.cNode.node < self.node:
                self.cNode = self.cNode.next            
                newnode.next = self.cNode
                newnode.prev = self.cNode.prev
                self.cNode.prev.next = newnode
                self.cNode.prev = newnode
        self.cNode = self.tail
    
    ''' Clears all nodes from list by individually removing each item '''    
    def clear(self):
        self.head = None
        self.cNode = None
        self.tail = None
        self.size = 0

    ''' Finds next node '''
    def findNext(self, node):
        self.cNode = self.head
        assert self.cNode != None
        while self.cNode is not None and self.cNode.node != self.node:
            self.cNode = self.cNode.next

    ''' Finds previous node '''   
    def findPrevious(self, node): 
        self.cNode = self.tail
        assert self.cNode != None
        while self.cNode is not None and self.cNode.node != self.node:
            self.cNode = self.cNode.prev

    ''' Returns current node '''
    def get(self):
        if self.cNode is None:
            self.cNode == None
        else:
            return self.cNode.node
    
    ''' Returns first node in list '''
    def getFirst(self):
        self.cNode = self.head
        if self.cNode is None: 
            return None
        else:
            return self.cNode.node

    ''' Returns last node in list '''    
    def getLast(self):
        self.cNode = self.tail
        if self.cNode is None: 
            return None
        else:
            return self.cNode.node 

    ''' Returns next node in list '''
    def getNext(self):
        if self.cNode.next is None:
            self.cNode = None
            return None
        else:
            self.cNode = self.cNode.next
            return self.cNode.node
    
    ''' Returns previous node in list '''   
    def getPrevious(self):
        if self.cNode.prev is None:
            self.cNode = None
            return None
        else:
            self.cNode = self.cNode.prev
            return self.cNode.node

    ''' Inserts node at current location in list '''
    def insert(self, node):
        newNode = DoubleListNode(node)
        self.size+=1
        assert self.cNode != None, 'None' 
        if self.head == self.cNode:
            self.prepend(node)        
            
        else:
            newNode.next = self.cNode
            newNode.prev = self.cNode.prev
            self.cNode.next = newNode
            self.cNode.prev = newNode
    
    ''' Inserts node at the begining of the list '''
    def prepend(self, node): 
        self.size+=1
        newNode = DoubleListNode(node)
        newNode.next = self.head
        self.head = newNode
        self.cNode = self.head
    
    ''' Removes current node from list'''
    def remove(self):
            self.cNode = self.head
            self.cNode = self.cNode.next
            if self.cNode is not None:
                self.size -=1
                if self.cNode is self.head:
                    self.head = self.cNode.next
                else:
                    self.cNode.prev = self.cNode.next
                if self.cNode is self.tail:
                    self.tail = self.cNode.prev
                else:
                    self.cNode.next.prev = self.cNode.prev
                    self.cNode = self.cNode.prev
            else:
                return None