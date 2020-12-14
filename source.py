#IMPORTS
import pandas as pd
import numpy as np

# TASK ONE
SecondaryStandards = [0.2, 250, 1, 2, 0.5, 0.3, 0.05, 0.1, 250, 500, 5]
index = [1,2,3,4,5,6,7,8,9,10,11]
df = pd.DataFrame({
    
  "Contaminant": ["Alluminum", "Chloride", "Copper", "Fluoride", "Foaming Agents", "Iron", "Manganese", "Silver", "Sulfate", "Total Dissolved Solids", "Zinc"],
  "Secondary Standard (mg/L)": SecondaryStandards},
   index)
df

# INPUTS
# Contaminant
# Qin = flowrate at inlet 
# Cin = concentration of contaminant at inlet
# OUTPUTS
# Cout = concentration at outlet (from the dataframe i.e. it is the tolerable limit)
# Qout = total flowrate at outlet
# Qadded = that needs to be added 

Cout = input("Enter your NSDWR contaminant row number below: " )
Qin = input("Enter the flowrate at the inlet of contaminated body of water below in liters per minute: " )
Cin = input("Enter the concentration of contaminant at inlet in mg/L: ")
# Converting strings into integers
newQin=int (Qin)
newCin=int (Cin)
newCout=(SecondaryStandards[int(Cout)-1])

newQout = (newQin*newCin)/newCout
newQadded = newQout - newQin

print('Total flowrate at outlet: ', newQout) 
print('Just the flowrate of pure water that needs to be added: ', newQadded)

# TASK TWO

# INPUTS
# V = volume of reservoir/body of water in cucbic meters
# Qpumped = Flowrate of clean water to be pumped into reservoir to flush out contaminant (meters cubed per hour)
# EffluentConc = percentage of contaminant that will remain (i.e. if 95 percent removal, then 5 percent remains)
# OUTPUTS
# Td = hydraulic detention time (hr)
# t = required flushing time (hr)
# V = volume of flushing water (meters cubed)

# Initializing input values
V = 10000
Qpumped = 300
EffluentConc = 0.05

# Calculations; equations derived from mass balance equations by hand
Td = V/Qpumped
t = -1*Td*np.log(EffluentConc) #np.log is natural log (i.e. ln)
V = Qpumped*Td

# Results
print('Hydraulic detention time in hours:', round(Td))
print('Required flushing time in hours:', round(t))
print('Volume of flushing water in cubic meters:', round(V))
