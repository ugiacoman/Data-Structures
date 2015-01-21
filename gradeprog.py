# CS 241 Lab 4
# gradeprog.py 
#
# Created by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
# Sort outs a bunch of student records from a text file and outputs
# the sorted results to a new text 

file.

''' Provides operations to open/data file and fetch data from file.'''
class FileReader:
    

    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputFile = None
    
    ''' Opens data file'''
    def open(self):
        self._inputFile = open(self._inputSrc, 'r')

    ''' Closes data file'''    
    def close(self):
        self._inputFile.close()
        self._inputFile = None
    
    '''Fetches all raw, unsorted data, storing them in a list'''
    def fetchAll(self):
        theRecords = list()
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
        return theRecords
    
    ''' Extracts the following student record fom the file '''
    def fetchRecord(self):
        line = self._inputFile.readline()
        if line == "":
            return None
        
        student =  StudentRecord()
        studentInfo = tuple(filter(None, line.split()))
        
        student.name = studentInfo[0].lower()
        student.grade =  int(studentInfo[1])
        return student

'''Initializes storage units'''    
class StudentRecord:
    def __init(self):
        self.name = None
        self.grade = 0    
    
'''Sorts raw data by Alphabetical Order and returns as list'''
def sortByAlphabet(studentList):
    n = len(studentList)
    
    for i in range(n - 1):
        for j in range(-i + n - 1):
            while (studentList[j].name > studentList[j + 1].name):
               
                tmp = studentList[j]
                studentList[j] = studentList[j + 1]
                studentList[j + 1] = tmp
                while j != 0:
                    j -= 1
                
    return studentList
    
'''Sorts raw data by Grade and returns as list'''    
def sortByGrade(studentList):
    n = len(studentList)
    
    for i in range(n - 1):
        for j in range(-i + n - 1):
            while (studentList[j].grade < studentList[j + 1].grade):
                tmp = studentList[j]
                studentList[j] = studentList[j + 1]
                studentList[j + 1] = tmp
                while j != 0:
                    j -= 1
                
    return studentList

''' Writes StudentList to new text file called 'procgrade.txt' '''        
def myWriter(studentList, sortType):
    procgrade = open('procgrade.txt', 'a')
    
    if sortType == 1:
        procgrade.write('Student records in alphabetic order:\n\n')
        for item in studentList:
            procgrade.write("%-15s   %-5s\n" % (item.name, item.grade))
        procgrade.write('\n')    
    if sortType == 2:
        procgrade.write('Student records by letter grades:\n\n')
        for student in studentList:
            if int(student.grade) >= 90:
                procgrade.write("%-15s   %-15s   %s\n" % \
                                (student.name, student.grade, 'A'))
            elif int(student.grade) >= 80:
                procgrade.write("%-15s   %-15s   %s\n" % \
                                (student.name, student.grade, 'B'))  
            elif int(student.grade) >= 70:
                procgrade.write("%-15s   %-15s   %s\n" % \
                                (student.name, student.grade, 'C'))  
            elif int(student.grade) >= 60:
                procgrade.write("%-15s   %-15s   %s\n" % \
                                (student.name, student.grade, 'D'))
            else:
                procgrade.write("%-15s   %-15s   %s\n" % \
                                (student.name, student.grade, 'F'))            

# Input file name    
FILE = "rawgrade.txt"

'''Main function, prints two lists: sortbyGradeList and sortByAlphabetList'''
def main():
    
    reader = FileReader(FILE)
    reader.open()
    studentList = reader.fetchAll()
    
    procgrade = open('procgrade.txt', 'w')
    # Alphabet List
    sortByAlphabet(studentList)
    myWriter(studentList, 1)
    
    # Grades List
    sortByGrade(studentList)
    myWriter(studentList, 2)
    
    reader.close()
    
main()