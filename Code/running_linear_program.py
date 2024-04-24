############################
# Optimal Season Running Schedule
# 
#
# Last Modified: April 21, 2024
# Author: Clancy Andrews
# Github: https://github.com/clancyandrews3/Optimal_Season_Running_Schedule
############################


import scipy.optimize as opt
import numpy as np


def get_starting_mileage():
    """Gets and returns starting mileage from user"""
    
    while True:
        try:
            start_mileage = int(input("\nEnter the starting mileage for training: "))
            break
        except ValueError:
            print("Value needs to be a number.")
    
    return start_mileage


def output_results(results):
    """Output the results in a user friendly way"""

    #Index for results vector
    x_index = (0,335)
    y_index = (336,671)
    delta_index = (672,687)

    #Variables needed for output
    week = 1
    days = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    workout_type = []
    current_day = []
    distance = []

    #Iterate over results vector and get schedule information; print for user
    for i in range(0,336,3):

        #Print week results and update week to next week
        if i % 7 == 0:
            print("")
            week += 1
            print("\n\n")

            #Reset lists for next week
            workout_type = []
            current_day = []
            distance = []

        #Set current day from dictionary
        current_day.append(days[(i%7)+1])

        #Check if run aerobic on day i
        if results[i+y_index[0]] == 1:
            workout_type.append("Aerobic Workout")
            distance.append(results[i])

        #Check if run anerobic on day i
        elif results[(i+1)+y_index[0]] == 1:
            workout_type.append("Anerobic Workout")
            distance.append(results[(i+1)])

        #Check if run threshold on day i
        elif results[(i+2)+y_index[0]] == 1:
            workout_type.append("Threshold Workout")
            distance.append(results[(i+2)])

        



if __name__=="__main__":

    dim = 704 #Depends on how many objective variables are in the program

    #Get starting milage
    mileage = get_starting_mileage()
    print(f"\nStarting Mileage (km): {mileage}\n\n")
    

    #Objective function
    c = np.concatenate((np.zeros((dim-16)),np.ones((16))))

    #Inequality and equality constraints
    A = np.array([[]])
    Ae = np.array([[]])

    #Constraint values
    b = np.array([])
    be = np.array([])

    #Determine bounds
    bounds = ()

    #Specify integer variables
    x_i = [0 for i in range(336)]
    y_i = [1 for i in range(336)]
    M_t = [0 for i in range(16)] # REMOVE
    d = [0 for i in range(16)]
    isint = x_i + y_i + M_t + d

    #Calculate results


    #Output results
    