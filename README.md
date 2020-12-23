# Mass Balance Equations in Environmental Engineering

## Description
This program will do two things: either help compare reactor types with varying volumes and/or flowrates, or tell you how long a reactor must go for in order to achieve a contamination removal goal. The three types of ideal reactor modelss are batch reactors, completely-mixed flow reactors (CMFR), and plug flow reactors (PFR). Since batch reactors have no flow, theta (hydraulic residence time), is replaced with simply a value of time where the contaminated water will exit the reactor. At the end of case one, the scenario in which one is comparing reactor types, percent removal will be displayed for different trials i.e. different reactors with varying parameters. Whichever reactor has the highest percent removal is the better option. At the end of case two, the scenario in which you are finding the time needed to achieve a percent removal or effluent concentration goal, the thetas and time values will be displayed, depending on reactor type. 

Assumptions: 
* All scenarios are steady state conditions, except those involving a batch reactor since there is no flow. 

Inputs: 
* Reactor type: batch, CMFR, or PFR.
* Order: zero, first, or second. While you can have functions (for decay rate) of higher order than the second, it is rare and therefore not used in this program.
* Concentration at inlet: in mg/L : parts per million (PPM) which is a typical unit for contaminants and species
* Volume: in cubic meters
* Flow rate: in cubic meters per minute or per hour (whichever is used will be the same unit of time for hydraulic residence time which is found in the program in order to find concentration at the outlet)
* k: the factor used to determine decay rate (found through experimentation, units can vary)
* time for batch reactor: since hydraulic residence time does not apply, a value of time is used to find the concentration at the outlet for a batch reactor
* Removal goal: case two scenarios you are either given a percent removal goal or a concentration at outlet goal
* Concentration at outlet goal: used in case two scenarios (see above bullet point)

Outputs:
* Percent removal
* Which reactor is a better option based on two trial runs
* Time needed to meet contamination removal goal

## Setup
To use program, copy source.py and test.py into same IDE (Integrated Development Environment) such as spyder, and run.
Or, one can download the repository, open and activate a virtual environment in local directory, and then run the code. 
See code below for additional help.
```
$ python3 -m venv venv
```
Activate it using:
```
For Linux/Mac OS:
$ source venv/bin/activate

For Windows:
> venv\Scripts\activate
```

## How To Use
Since there are two types of problems typically asked i.e. the two cases, one example of each will be shown. It is important to note that the program can be used as a design tool and can easily be played with by entering different inputs to determine desired volumes, ideal flowrates, and most efficient systems based on fast they can remove contaminants. The examples below are more textbook like examples of how the program can be applied. 

## Example 1 (Case One)
*Problem: Given Contaminant A (Cin of 50 mg/L, k of 0.2, and first order decay) would a batch reactor sitting for 40 minutes, be better or worse than a plug flow reactor of the same volume (100 cubic meters) with a flow rate of 10 cubic meters per minute?

* Solution: Since we are being asked to compare reactors, this is a case one problem. All the needed parameters are given and therefore plugged into the class 'System' as shown below. 

```
trial1 = System(ReactorType='Batch', order=1, volume=100, flowrate=10, Cin=50, kVal=0.2, tBatch=40)
trial2 = System(ReactorType='PFR', order=1, volume=100, flowrate=10, Cin=50, kVal=0.2)
```
These two different sets of parameters are used to find their own percent removal rates and then appended to a list where another function determines which one is the better reactor model depending on which has the higer percent removal. In this case the results are shown below:

```
Trial 1 is a more efficient reactor model.
```
Trial 1 had a 100 percent removal while Trial 2 only had an 86 percent removal.

## Example 2 (Case Two)
*Problem: Given Contaminant B (first order decay, k of 0.3, Cin of 130 mg/L), how long will it take a plug flow reactor to remove 99 percent of the contaminant (in minutes)?

* Solution: We know this problem is a case two scenario since a value of time needs to be found. Therefore System2 is used and the user enters the given values into the program as can be seen below.

```
S2trial1 = System2(ReactorType = 'PFR', order = 1, Cin = 130, kVal = 0.3, removalGoal = 99) 
```
This results in the output below.
```
Time needed to achieve goal:  16 minutes
```
Note that, case two problems typically give a percent removal goal (usually very high and in the 90s range) or a goal for the concentration in the effluent (typically very small and less than one). The above example uses a percent removal goal since this is most common but does work for concentration goals as well. If using a concentration goal simply set removalGoal equal to zero and then enter your CoutGoal as prompted. 


