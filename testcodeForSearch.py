def linearSearch(theValues, target):
    for number in range (len(theValues)):
        if theValues[number] == target:
            return True
    return False
            
def sortedLinearSearch(theValues, target):
    for number in range(len(theValues)):
        if theValues[number] == target:
            return True
        elif theValues[number] > target:
            return False
    return False

def findSmallest(theValues):
    smallest = theValues[0]
    for number in range(1, len(theValues)):
        if theValues[number] < smallest:
            smallest = theValues[number]
    return smallest

def binarySearch(theValues, target):
    low = 0
    high = (len(theValues) - 1)
    
    while low <= high:
        mid = (low + high) // 2
        if theValues[mid] == target:
            return True
        elif theValues[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return False

def bubbleSort(theSeq):
    n = len(theSeq)
    steps = 0
    for num1 in range(n - 1):
        for num2 in range (n - num1 - 1):
            if theSeq[num2] > theSeq[num2 + 1]:
                tmp = theSeq[num2]
                theSeq[num2] = theSeq[num2 + 1]
                theSeq[num2 + 1] = tmp
              
            steps += 1
        steps += 1
    return (theSeq, steps)

def selectionSort(theSeq):
    n = len(theSeq)
    steps = 0
    for i in range(n - 1):
        smallNdx = i
        
        for j in range( i + 1, n):
            if theSeq[j] < theSeq[smallNdx]:
                smallNdx = j
                steps += 1
        if smallNdx != j:
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp
        steps += 1
    
    return (theSeq, steps)

def insertionSort(theSeq):
    
    n = len(theSeq)
    steps = 0
    
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
        steps += 1
    return (theSeq, steps)


def mergeSortedLists(listA, listB):
    newList = list()
    a = 0
    b = 0
    
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1
    
    while a < len(listA):
        newList.append(listA[a])
        a += 1
        
    while b < len(listB):
        newList.append(listB[b])
        b += 1
        
    return newList

 
def main():
    print()
    
    # Linear Search  and Sorted Linear Search Example
    valueList = [1, 9, 4, 2]
    linearSearchEx = linearSearch(valueList, 2)
    sortedLinearSearchEx =  sortedLinearSearch(valueList, 2)
    print('Linear Search:', linearSearchEx)
    print('Sorted Linear Search:', sortedLinearSearchEx)
    print('Linear Search & Sorted Linear Search Algorithm: O(n), O(n), O(n)')
    print()
    
    # Find the smallest integer Example
    valueList = [500, 200, 100, 600]
    findSmallestEx = findSmallest(valueList)
    print('Smallest value: ', findSmallestEx)
    print('findSmallest Algorithm: O(n), O(n), O(n)')
    print()
    
    # Binary Search Example
    valueList = [1, 4, 8, 123, 234, 567, 900]
    binarySearchEx = binarySearch(valueList, 567)
    print('Binary Search: ', binarySearchEx)
    print('Binary Search Algorithm: O(log_2 n)')
    print()
    
    # Bubble Sort Example
    valueList = [8, 5, 1, 4, 3, 2]
    bubbleSortEx = bubbleSort(valueList)
    print('Bubble Sort: ', bubbleSortEx[0])
    print('Steps Taken: ', bubbleSortEx[1])
    print('Bubble Sort Algorithm: O(n^2)')
    print()
    
    # Selection Sort Example
    valueList = [8, 5, 1, 4, 3, 2]
    selectionSortEx = selectionSort(valueList)
    print('Selection Sort: ', selectionSortEx[0])
    print('Steps Taken: ', selectionSortEx[1])  
    print('Selection Sort Algorithm: O(n^2)')
    print()
    
    # Insertion Sort Example
    valueList = [8, 5, 1, 4, 3, 2]
    insertionSortEx = insertionSort(valueList)
    print('Insertion Sort: ', insertionSortEx[0])
    print('Steps: ', insertionSortEx[1])    
    print('Insertion Sort Algorithm: O(n^2)')
    print()    
    
    # Merging Two sorted lists
    valueList1 = [3, 4, 7, 9, 12, 23]
    valueList2 = [1, 2, 6, 8, 10, 12, 25]
    print('Merging two lists:', valueList1, valueList2)
    print('Merged List', mergeSortedLists(valueList1, valueList2))
    print('Merge Lists Algorithm: O(n)')
    print()
    
    
main()