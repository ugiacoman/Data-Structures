# CS 241 Lab 1
# time2.py
# Modified by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#
# We can use a Time ADT to represent the time of day, for any 24-hour
# period, as the number of seconds that have elapsed since midnight. 
# Given the following list of operations, implement the Time ADT.


class Time:
    
    def __init__(self, hour, minutes, seconds):
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        
    def hour(self):
        return self.hour
    
    def minutes(self):
        return self.minutes
    
    def seconds(self):
        return self.seconds
    
    # Returns the number of seconds as a positive itneger between this time and
    # the otherTime.
    def numSeconds(self, otherTime): 
        
        if self.hour > otherTime.hour:
            hourToSeconds = 3600 * (self.hour - otherTime.hour)
        else:
            hourToSeconds = 3600 * (otherTime.hour - self.hour)
        
        
        if self.minutes > otherTime.minutes:
            minutesToSeconds = 60 * (self.minutes - otherTime.minutes)
        else:
            minutesToSeconds = 60 * (otherTime.minutes - self.minutes)
            
            
        if self.seconds > otherTime.seconds:
            seconds = (self.seconds - otherTime.seconds)
        else:
            seconds = (otherTime.seconds - self.seconds)
       
        calcTimeDiff = hourToSeconds + minutesToSeconds + seconds        
        timeDiff= "Time Difference: "+ str(calcTimeDiff) + " seconds."
        
        return timeDiff
    
    # Determines if this time is ante meridiem or before midday (at or before
    # 12'o'clock noon).
    def isAM(self):
        if self.hour >= 0 and self.hour < 12:
            amTest = "Your time is in the AM"
        else:
            amTest = "Your time is not in the AM, but PM"
            
        return amTest
    
    # Determines if this time is post meridiem or after midday (after
    # 12 o'clock noon).
    def isPM(self):
        
        if self.hour >= 12 and self.hour >= 23:
            pmTest = "Your time is in the PM"
        else:
            pmTest = "Your time is not in the PM, but AM"

        return pmTest 
    
    # Compares this time to the otherTime to determine their logical ordering.
    # This comparison can be done using any of the Python logical operators.
    def comparable(self,otherTime):
        
        if self.hour > otherTime.hour and \ 
                                     self.minutes > otherTime.minutes and \
                                     self.seconds > otherTime.seconds:
            compareTest = str(self.hour) + ":" + str(self.minutes) + ":" + \
                                     str(self.seconds)
            
            time =  str(otherTime.hour) + ":" + str(otherTime.minutes)\
                                     + ":" +str(otherTime.seconds)
            
            comparison = compareTest + " is before " + time 
        
        else:
            compareTest = str(otherTime.hour) + ":" + \
                                     str(otherTime.minutes) + ":" + \
                                     str(otherTime.seconds)
            
            time = str(self.hour) + ":" + str(self.minutes) + ":" \
                                     + str(self.seconds)
            comparison = compareTest + " is after " + time

        return comparison
    
    # Returns a string represeting the time in the 12-hour format hh:mm:ss.
    # Invoked by calling Python's str() constructor.
    def toString(self):
        amOrPm = ""
       
        if self.hour >= 0 and self.hour <= 11:
            amOrPm = "AM"

        elif self.hour >= 12 and self.hour <= 23:
            amOrPm = "PM"
            self.hour = (self.hour -12)
       
        timetoStr = str(self.hour) + ":" + str(self.minutes) +":"+ \
            str(self.seconds) + amOrPm

        return timetoStr
        
            
        
        
        