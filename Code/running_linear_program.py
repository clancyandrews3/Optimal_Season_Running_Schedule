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

    dim = 736 #Depends on how many objective variables are in the program

    #Get starting milage
    mileage = get_starting_mileage()
    print(f"\nStarting Mileage (km): {mileage}\n\n")
    



    #Determine goal weekly mileage for each week in the season
    M = [mileage]
    for t in range(13):
        next_week = round(1.1*M[t],1) #10% increase from previous week
        M.append(next_week)

    for t in range(2):
        next_week = round(0.8*M[-1],1) # Last 2 week are 20% fewer kilometers
        M.append(next_week)




    #Set up the weekly ratios of mileage for the season for each workout type
    aerobic_mileage_ratio = []
    anerobic_threshold_mileage_ratio = []
    for t in range(16):
        if t in range(4):
            aerobic_mileage_ratio.append(0.8)
            anerobic_threshold_mileage_ratio.append(0.2*0.5)
        elif t in range(4,8):
            aerobic_mileage_ratio.append(0.75)
            anerobic_threshold_mileage_ratio.append(0.25*0.5)
        elif t in range(8,12):
            aerobic_mileage_ratio.append(0.7)
            anerobic_threshold_mileage_ratio.append(0.3*0.5)
        elif t in range(12,14):
            aerobic_mileage_ratio.append(0.65)
            anerobic_threshold_mileage_ratio.append(0.35*0.5)
        else:
            aerobic_mileage_ratio.append(0.6)
            anerobic_threshold_mileage_ratio.append(0.4*0.5)




    #Inequality and equality constraints stored here
    A = np.array([[]])
    Ae = None




    ############### Start Aerobic Constraints #################

    #Total weekly aerobic mileage 0.8-0.6 of total weekly mileage
    for t in range(16):
        x = [-1,0,0]*7
        d = np.concatenate((np.zeros(t),np.array([1]),np.zeros(15-t)))
        
        





    ############### End Aerobic Constraints ####################


    ############### Start Anerobic Constraints #################







    ############### End Anerobic Constraints ###################


    ############### Start Threshold Constraints ################







    ############### End Threshold Constraints ##################


    ############### Start General Constraints ##################







    ############### End General Constraints ####################



    #Objective function
    c = np.concatenate((np.zeros((dim-16)),np.ones((16))))

    #Constraint values
    b = np.array([])
    be = None

    #Determine bounds
    bounds = ()

    #Specify integer variables
    x_i = [0 for i in range(336)]
    y_i = [1 for i in range(336)]
    alpha = [0 for i in range(16)]
    beta = [0 for i in range(16)]
    gamma = [0 for i in range(16)]
    delta = [0 for i in range(16)]
    isint = x_i + y_i + alpha + beta + gamma + delta

    #Calculate results


    #Output results
    