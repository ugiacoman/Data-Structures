# CS 241 Lab 1
# fraction.py
# Modified by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
# 
# Greatest Common Multiple(GCM) function example found: http://bit.ly/1uGxocT
# Lowest Common Multiple(LCM) function example found:   http://bit.ly/1ol8Ce4
#
# Fraction ADT overloads the given Python Fraction class
# It also provides the ability to produce a string version of a fraction.


class Fraction:
     
     # GCM handler
     def gcf(self, x, y):
          
          while y > 0:
               x, y = y, x % y
               
          return x
     
     # LCM handler
     def lcm(x, y):
          
          self.lcm = (x * y) // self.gcf(x, y)
          
          return self.lcm       
     
     # Separates numerator from denominator, simplifies fraction and 
     # checks for divide by zero error
     def __init__(self, numerator, denominator):
          self.leFrac = [0, 0]
          
          assert denominator > 0
          self.leFrac[0] = numerator / self.gcf(numerator, denominator)
          self.leFrac[1] = denominator / self.gcf(numerator, denominator)
               
     # Overload: Adds and simplifies fraction
     def __add__(self, ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0] * (leLcm / self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * (leLcm / \
                                                  ComparisonFrac.leFrac[1])
          sum = firstNum + comparisonNum
          
          return Fraction(sum, leLcm)
     
     # Overload: Substracts and simplifies fraction
     def __sub__(self, ComparisonFrac):
          
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0] * (leLcm / self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * (leLcm / \
                                                  ComparisonFrac.leFrac[1])
          difference = firstNum - comparisonNum
          
          return Fraction(difference, leLcm)
     
     # Overload: Multiplies and simplifies fraction
     def __mul__(self, ComparisonFrac):
          newNum = self.leFrac[0] * ComparisonFrac.leFrac[0]
          newDenom = self.leFrac[1] * ComparisonFrac.leFrac[1]
          
          return Fraction(newNum,newDenom)
     
     # Overload: True Division
     def __truediv__(self,ComparisonFrac):
          newNum = self.leFrac[0] * ComparisonFrac.leFrac[1]
          newDenom = self.leFrac[1] * ComparisonFrac.leFrac[0]
          
          return Fraction(newNum,newDenom)    
     
     # Overload: Floor Division
     def __floordiv__(self,ComparisonFrac):
          newNum = self.leFrac[0] * ComparisonFrac.leFrac[1]
          newDenom = self.leFrac[1] * ComparisonFrac.leFrac[0]
          
          return newNum // newDenom
     
     # Overload: Comparison function seeking equality
     def __eq__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0] * (leLcm / self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * leLcm / \
                                                  ComparisonFrac.leFrac[1])
          return firstNum == comparisonNum
     
     # Overload: Comparison function seeking inequality 
     def __ne__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0]*(leLcm/self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * (leLcm / \
                                                  ComparisonFrac.leFrac[1])
          return firstNum != comparisonNum
     
     # Overload: Comparison function seeking less than 
     def __lt__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0] * (leLcm/self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * (leLcm / \
                                                  ComparisonFrac.leFrac[1])
          return firstNum < comparisonNum
     
     # Overload: Comparison function seeking less than or equal to
     def __le__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0] * (leLcm/self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0] * (leLcm / \
                                                  ComparisonFrac.leFrac[1])
          return firstNum <= comparisonNum 
     
     # Overload: Comparison function seeking greater than
     def __gt__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0]*(leLcm/self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0]*(leLcm/\
                                                  ComparisonFrac.leFrac[1])
          return firstNum > comparisonNum
     
     # Overload: Comparison function seeking greater than or equal to
     def __ge__(self,ComparisonFrac):
          leLcm = self.lcm(self.leFrac[1], ComparisonFrac.leFrac[1])
          firstNum = self.leFrac[0]*(leLcm/self.leFrac[1])
          comparisonNum = ComparisonFrac.leFrac[0]*(leLcm/\
                                                  ComparisonFrac.leFrac[1])
          return firstNum >= comparisonNum     
     
     # Support for toString Operation
     def __str__(self):
          if self.leFrac[0] == 0:
               return "0"
          
          elif self.leFrac[0] / self.leFrac[1] == 1:
               return "1"
          
          elif self.leFrac[1] == 1:
               return "%i" % (self.leFrac[0])
          
          else:
               return "%i/%i" % (self.leFrac[0], self.leFrac[1])