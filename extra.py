'''
CS 241 Extra Lab

File:        extra.py

Description: Balanced Search Tree Implemenation (AVL TREE) TEST CODE

Created by:  Ulises Giacoman (ugiacoma)
'''

import random
import time

from balst import MyBalST

def generateRandomAlphaNumChar():
    ''' Generates random char for 'phrases' '''
    code = random.randint(0,61)
    if code < 10:
        code += ord('0')
    elif code < 36:
        code -= 10
        code += ord('A')
    else:
        code -= 36
        code += ord('a')
    return chr(code)

def generateOnePhrase(maxl):
    ''' Generates a random character phrase using characters generated from
        generateRandomAlphaNumChar
        
    Arguments:
    max1 - max phrase length length
    '''
    mylen = random.randint(5, maxl)
    mystr = list()
    for i in range(mylen):
        mystr.append(generateRandomAlphaNumChar())
    return ''.join(mystr)

def generateRandomPhrases(n):
    ''' Creates list of phrases from previously generated individual phrases,
        in other words combines them.
        
    Arguments:
    n - number of phrases to be tested
    '''
    phrases = list()
    for i in range(n):
        phrase = generateOnePhrase(20)
        phrases.append(phrase)
    return phrases

def pickPhrases(phrases):
    ''' Creates a subset of 'phrases': hitPhrases
        
    Arguments:
    phrases - list of all phrases to be tested
    '''    
    hitPhrases = list()
    n = len(phrases) // 10
    for i in range(n):
        x = random.randint(0, len(phrases)-1)
        hitPhrases.append(phrases[x])
    return hitPhrases

def linearSearch(phrases, xphrases):
    ''' Helper function for doLinearSearch to search through list of phrases
        linearly
        
    Arguments:
    phrases - list of all phrases
    xphrases - list of phrases to be checked
    '''    
    n = len(phrases)
    for i in range(n):
        if phrases[i] == xphrases:
            return True
    return False

def doLinearSearch(phrases, hitPhrases, missPhrases):
    ''' Searches through list of phrases linearly
        
    Arguments:
    phrases - list of all phrases
    hitPhrases - subset of phrases to be verified in 'phrases'
    missPhrases - list of phrases to be verified not in 'phrases'
    '''       
    for phs in hitPhrases:
        found = linearSearch(phrases, phs)
        assert found, "doLinearSearch: Failed!"
        
    for phs in missPhrases:
        found = linearSearch(phrases, phs)
        assert not found, "doLinearSearch: Failed \
        - there is a slight chance this indeed fails- try again!"

def buildBalST(phrases):
    ''' Builds balanced search tree
        
    Arguments:
    phrases - list of all phrases
    '''           
    mybalst = MyBalST()
    for phs in phrases:
        mybalst.insert(phs)
    return mybalst

def doBalStSearch(balst, hitPhrases, missPhrases):
    ''' Builds balanced search tree
        
    Arguments:
    balst - built binary search tree
    hitPhrases - subset of phrases to be verified in 'phrases'
    missPhrases - list of phrases to be verified not in 'phrases'
    '''         
    for phs in hitPhrases:
        found = balst.search(phs)
        assert found, "Failed!"
    
    for phs in missPhrases:
        found = balst.search(phs)
        assert not found, "doBalastSearch: Failed \
        - there is a slight chance this indead fails - try again!"

def writePhrasesToFile(phrases, fname):
    ''' Writes phrases to an external file for sanity checks
        
    Arguments:
    phrases - list of all phrases
    fname - filename to be created
    '''        
    f = open(fname, 'w')
    for phs in phrases:
        f.write(phs)
        f.write('\n')
    f.close()
    

def main():
    ''' Main Execution of Test Script'''
    #initialize random number generator
    random.seed()
    
    print()
    print("For debugging purposes, use a smaller number.")
    print("For final test, use a larger number such as > 100000.")
    print()
    n = int(input("Enter number of phrases to be tested: "))
    #print(n)
   
    # generate 'n' random phrases
    phrases = generateRandomPhrases(n)
    # print(phrases)
   
    # write "phrases" to a file for post examination
    writePhrasesToFile(phrases, "phrases.txt")
   
    hitPhrases = pickPhrases(phrases)
    writePhrasesToFile(hitPhrases, "hits.txt")
    # randomly pick 'n/10' phrases out of the generated "phrases"
    # using any of these phrases for the search is likely not going to be hit
    missPhrases = generateRandomPhrases(n//10)
    writePhrasesToFile(missPhrases, "misses.txt")
   
    # do a linear search of all picked / new phrases in the "phrases"
    # Time this operation (see how slow it is)
    t0 = time.time()
    doLinearSearch(phrases, hitPhrases, missPhrases)
    t1 = time.time()
    print("doLinearSearch elapsed time is %5.3f." % (t1 - t0))
    print()
   
    # Build binary search tree (add all phrases into the tree)
    mybalst = buildBalST(phrases)
   
    # do a balanced search for all picked / new phrases in the "phrases"
    # Time this operation (see how fast this time)    
    t0 = time.time()
    doBalStSearch(mybalst, hitPhrases, missPhrases)
    t1 = time.time()
    print("doBalSTSearch elapsed time is %5.3f." % (t1 - t0))
    print()
    
    print("Sanity check those phrase files.")
    print()
    
main()