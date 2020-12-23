# Mass Balance Equations in Environmental Engineering

## Description
This program will do two things: either help compare reactor types with varying volumes and/or flowrates, or tell you how long a reactor must go for in order to achieve a contamination removal goal. The three types of ideal reactor modelss are batch reactors, completely-mixed flow reactors (CMFR), and plug flow reactors (PFR). Since batch reactors have no flow, theta (hydraulic residence time), is replaced with simply a value of time where the contaminated water will exit the reactor. At the end of case one, the scenario in which one is comparing reactor types, percent removal will be displayed for different trials i.e. different reactors with varying parameters. Whichever reactor has the highest percent removal is the better option. At the end of case two, the scenario in which you are finding the time needed to achieve a percent removal or effluent concentration goal, the thetas and time values will be displayed, depending on reactor type. 

Assumptions: 
* All scenarios are steady state conditions, except those involving a batch reactor since there is no flow. 

Inputs: (Italicized are parameters 
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




