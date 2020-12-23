#Case 1

from source import System
from source import System2

# 'trial1' and 'trial2,' compare two different reactor models using the System class.
trial1 = System(ReactorType='Batch', order=1, volume=100, flowrate=10, Cin=50, kVal=0.2, tBatch=40)
print('Percent removal for first trial: ', trial1.pRemoval_find())

trial2 = System(ReactorType='PFR', order=1, volume=100, flowrate=10, Cin=50, kVal=0.2)
print('Percent removal for second trial: ',trial2.pRemoval_find())

comparison = compSystem(results)

# S2trial uses the System2 class to determine the time needed to achieve given removal goal
# or outlet concentration goal.
S2trial = System2(ReactorType = 'PFR', order = 1, Cin = 130, kVal = 0.3, removalGoal = 99) 
print('Time needed to achieve goal: ', round(S2trial.tNeeded_find()), 'minutes')
