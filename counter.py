# CS 241 Lab 1
# counter.py
# Modified by: Ulises Giacoman (703)-678-6244 ugiacoman@email.wm.edu
#                 
# This program functions in the following manner: 
# A click counter is a small hand-held device that contains a push button
# and a count display. To increment the counter, the button is pushed and the
# new count shows in the display. Clicker counters also contain a button that
# can be pressed to reset the counter to zero.

class Counter:
    
    def __init__(self):
        self.numberOfClicks = (0)
    
    # Will increment the counter by 1
    def push(self):
        self.numberOfClicks += 1
    
    # Will reset the counter to 0
    def reset(self):
        self.numberOfClicks = 0

    # Brings counter down by 1
    def down(self):
        if self.numberOfClicks != 0:
            self.numberOfClicks -= 1
            
    # Retrieves number of clicks on counter
    def get(self):
        return self.numberOfClicks