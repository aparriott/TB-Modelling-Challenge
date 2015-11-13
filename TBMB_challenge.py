#TB MODEL-BUILDING CHALLENGE
#Requires installation of math and csv modules

#Tasks 1 and 2: Calculate and record the status of one individual over 20 years

#Import random integer function
from random import randint

#Creating a function to stochastically assign status
def state_trans(state):
    random = randint(1, 100)
    if random == 1 and state == "NOTB":
        state = "LTBI"
    elif random == 1 and state == "LTBI":
        state = "ATB"
    elif state == "ATB":
        state = "LTBI"
    else:
        state = state
    return state

#Initialize a list for an individual with a year zero state of uninfected

state_list = ["NOTB"]

#Get state trasitions for 20 years and store in a list

for year in range(0, 21):
    state_in = state_list[year]
    state_out = state_trans(state_in)
    print "Year %d:" % (year) + state_out
    state_list.append(state_out)
    year += 1

#Task 3: Model a population of 1000 individuals over 20 years

#Create a list of initial states
pop_year = []

for x in range(10):
    pop_year.append("ATB")
for x in range(90):
    pop_year.append("LTBI")
for x in range(900):
    pop_year.append("NOTB")

print "Year 0: 900 unifected, 90 LTBI, 10 active TB"

#Import csv module to hold yearly outputs
import csv

#Loop over 20 years
for year in range(1,21):
    unifected = 0
    LTBI = 0
    active = 0
    #Loop over each individual
    for person in range(1000):
        #assign status and add to counts
        state_out = state_trans(pop_year[person])
        pop_year[person] = state_out
        if state_out == "NOTB":
            unifected += 1
        elif state_out == "LTBI":
            LTBI += 1
        else:
            active += 1
    #Print numbers in each state for each year to the console
    print "Year %d: %d uninfected, %d LTBI, %d active TB" %(year, unifected, LTBI, active) 
        

    
