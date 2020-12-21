#Case 1

from source import System

trial1 = System(ReactorType='Batch', order=1, volume=100, flowrate=10, Cin=50, kVal=0.2, tBatch=40)
print(trial1.Cout_find())
