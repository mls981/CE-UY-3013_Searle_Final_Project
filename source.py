# IMPORTS

import math 

# NOTES FOR USER

# There are two classes for two seperate cases. 'System' and 'System2'
# are for cases one and two respectively. In case one, either time is given
# or theta can be found depending on reactor type; used to find best reactor
# type based on highest percent removal. Case two is the inverse of case one.
# In case two, either percent removal is given or just Cout
# (concentration of contaminant at outlet); used to find theta (hydraulic
# residence time) or t(time in batch reactor) to meet removal/concentration
# goal. 

# Valid reactor types are plug-flow reactors (enter PFR), completely-
# mixed flow reactors (enter CMFR), and batch reactors (enter Batch).  

# Order can be zero, first, or second. (Enter 0, 1, or 2).

# For 'System,' volume is in cubic meters and flowrate can be in cubic meters
# per hour or per minute. 
# For 'System2,' the time value presented will be in minutes. Also, if you are
# evaluating a batch reactor, still enter 0 for flowrate. 

# Always keep order, Cin (concentration at inlet), and kVal (factor to determine
# decay rate) the same when comparing reactor models since these are dependent 
# on the species/contaminat. 

class System:
    """
    Case 1: either time is given or theta can be found depending on reactor
    type; used to find best reactor type based on highest percent removal
    """

    def __init__(self, ReactorType, order, volume, flowrate, Cin, kVal,
                 tBatch=None):
        self.reactor = ReactorType
        self.order = order
        self.V = volume
        self.Q = flowrate
        self.Cin = Cin
        self.kVal = kVal
        self.tBatch = tBatch


    def Theta_find(self):
        if self.reactor == 'Batch':
            Theta = self.tBatch
        else:
            Theta = self.V / self.Q

        return Theta

    def Cout_find(self):
        Theta = self.Theta_find()

        if self.reactor == 'PFR':  # PFR nested if statements

            if self.order == 0:
                self.Cout = self.Cin - (self.kVal * Theta)
            if self.order == 1:
                self.Cout = self.Cin * math.exp(-self.kVal * Theta)
            if self.order == 2:
                self.Cout = self.Cin / (1 + self.kVal * Theta * self.Cin)
        if self.reactor == 'CMFR':  # CMFR nested if statements
            print("b")
            if self.order == 0:
                self.Cout = self.Cin - (self.kVal * Theta)
            if self.order == 1:
                self.Cout = self.Cin(1 + self.kVal * Theta)
            if self.order == 2:
                self.Cout = (-1 + math.sqrt(1 + 4 * self.kVal * Theta * self.Cin)) / (2 * self.kVal * Theta)
        if self.reactor == 'Batch':  # Batch reactor nested if statements

            if self.order == 0:
                self.Cout = self.Cin - (self.kVal * Theta)

            elif self.order == 1:
                self.Cout = self.Cin * math.exp(-self.kVal * Theta)
            if self.order == 2:
                self.Cout = self.Cin / (1 + self.kVal * Theta * self.Cin)


        return self.Cout
    def pRemoval_find(self):
        return round(100 * (1 - (self.Cout_find() / self.Cin)))

    
class System2:
    """
    Case 2: the inverse of Case 1: either percent removal is given or just Cout
    (concentration of contaminant at outlet); used to find theta (hydraulic
    residence time) or t(time in batch reactor) to meet removal/concentration
    goal.
    """
    def __init__(self, ReactorType, order, Cin, kVal, removalGoal, CoutGoal=1):
        self.reactor = ReactorType
        self.order = order
        self.removalGoal = removalGoal
        self.CoutGoal = CoutGoal
        self.Cin = Cin
        self.kVal = kVal
  
    def conv_rg_to_CoutGoal(self, removalGoal, Cin):
        if self.removalGoal != None:
            return ((100-self.removalGoal)/100)*self.Cin
    
    def tNeeded_find(self): 
        if self.reactor == 'PFR' or 'Batch': # PFR/Batch nested if statements
            if self.order == 0:
                tNeeded = (1/self.kVal)*(self.Cin-self.CoutGoal)
            if self.order == 1:
                tNeeded = (1/self.kVal)*(math.log(self.Cin/self.CoutGoal))
            if self.order == 2:
                tNeeded = (1/(self.kVal*self.Cin))*((self.Cin/self.CoutGoal)-1)
        elif self.reactor == 'CMFR': # CMFR nested if statements
            if self.order == 0:
                tNeeded = (self.CoutGoal/self.kVal)*((self.Cin/self.CoutGoal)-1)
            if self.order == 1:
                tNeeded = (1/self.kVal)*((self.Cin/self.CoutGoal)-1)
            if self.order == 2:
                tNeeded = (1/(self.kVal*self.CoutGoal))*((self.Cin/self.CoutGoal)-1)
                
        return tNeeded
