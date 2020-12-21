#IMPORTS
import math 


class System:
    """
    Two cases:
    Case 1: either time is given or theta can be found depending on reactor
    type; used to find best reactor type based on highest percent removal
    Case 2: the inverse of Case 1: either percent removal is given or just Cout
    (concentration of contaminant at outlet); used to find theta (hydraulic
    residence time) or t(time in batch reactor) to meet removal/concentration
    goal

    Valid reactor types are plug-flow reactors (enter PFR), completely-
    mixed flow reactors (enter CMFR), and batch reactors (enter Batch).
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
                Cout = self.Cin - (self.kVal * Theta)
            if self.order == 1:
                Cout = self.Cin(1 + self.kVal * Theta)
            if self.order == 2:
                Cout = (-1 + math.sqrt(1 + 4 * self.kVal * Theta * self.Cin)) / (2 * self.kVal * Theta)
        if self.reactor == 'Batch':  # Batch reactor nested if statements

            if self.order == 0:
                Cout = self.Cin - (self.kVal * Theta)

            elif self.order == 1:
                Cout = self.Cin * math.exp(-self.kVal * Theta)
            if self.order == 2:
                Cout = self.Cin / (1 + self.kVal * Theta * self.Cin)


        return Cout
    
    def pRemoval_find(self):
        return round(100 * (1 - (self.Cout_find() / self.Cin)))

