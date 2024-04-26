############################
# Optimal Season Running Schedule
# 
#
# Last Modified: April 25, 2024
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

        
def print_matrix(A):
    for i in A:
        print(i)


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




    #Starting with linearizing the objective function
    x = [-1, -1, -1] * 7
    d = np.concatenate((np.zeros(0), np.array([1]), np.zeros(15)))

    first_row = np.concatenate((np.zeros(0), x, np.zeros(dim - 37), d))
    A = np.array([first_row])
    b = [-M[0]]
    
    for t in range(1,16):
        x = [-1, -1, -1] * 7
        d = np.concatenate((np.zeros(t), np.array([1]), np.zeros(15 - t)))

        new_row = np.concatenate((np.zeros(t * 21), x, np.zeros((dim - 37) - (21 * t)), d))
        A = np.vstack([A, new_row])
        b.append(-M[t])
        

    for t in range(16):
        x = [-1, -1, -1] * 7
        d = np.concatenate((np.zeros(t), np.array([-1]), np.zeros(15 - t)))

        new_row = np.concatenate((np.zeros(t * 21), x, np.zeros((dim - 37) - (21 * t)), d))
        A = np.vstack([A, new_row])
        b.append(-M[t])




    ############### Start Aerobic Constraints #################

    #Total weekly aerobic mileage 0.8-0.6 of total weekly mileage
    for t in range(16):

        x = [-1,0,0]*7
        d = np.concatenate((np.zeros(t),np.array([1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336),d,np.zeros(48)))
        
        A = np.vstack([A,new_row])
        b.append(-round((aerobic_mileage_ratio[t]*M[t]),1))
        
    for t in range(16):
        x = [-1,0,0]*7
        d = np.concatenate((np.zeros(t),np.array([-1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336),d,np.zeros(48)))

        A = np.vstack([A,new_row])
        b.append(-round((aerobic_mileage_ratio[t]*M[t]),1))



    #Longest aerobic run no longer than 30% total goal mileage
    for t in range(16*7):
        next_row = np.concatenate((np.zeros(3*t),np.array([1]),np.zeros(336-(3*t)-1),np.zeros(dim-336)))

        A = np.vstack([A,next_row])

    for t in range(16):
        for _ in range(7):
            b.append(0.3*M[t])

    

    #Aerobic runs must be at most twice the total goal mileage
    for t in range(16):
        for _ in range(7):
            x = [1,0,0]
            y = [-2*M[t],0,0]
            next_row = np.concatenate((np.zeros(3*t),x,np.zeros(336-3-(3*t)),np.zeros(3*t),y,np.zeros(336-3-(3*t)),np.zeros(64)))

            A = np.vstack([A,next_row])
            b.append(0)

    ############### End Aerobic Constraints ####################




    ############### Start Anerobic Constraints #################

    #Total weekly anerobic mileage 0.1-0.2 of total weekly mileage
    for t in range(16):

        x = [0,-1,0]*7
        d = np.concatenate((np.zeros(t),np.array([1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336+16),d,np.zeros(32)))
        
        A = np.vstack([A,new_row])
        b.append(-round((anerobic_threshold_mileage_ratio[t]*M[t]),1))
        
    for t in range(16):
        x = [0,-1,0]*7
        d = np.concatenate((np.zeros(t),np.array([-1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336+16),d,np.zeros(32)))

        A = np.vstack([A,new_row])
        b.append(-round((anerobic_threshold_mileage_ratio[t]*M[t]),1))



    #Only 3 anerobic workouts a week
    for t in range(16):
        y = [0,1,0]*7

        next_row = np.concatenate((np.zeros(336),np.zeros(21*t),y,np.zeros(336-(21*t)-21),np.zeros(64)))
        A = np.vstack([A,next_row])
        b.append(3)



    #Cannot do two consecutive anerobic workouts
    for t in range(16*7):
        next_row = np.concatenate((np.zeros(336),np.zeros(t),np.array([1,1]),np.zeros(336-t-2),np.zeros(64)))

        A = np.vstack([A,next_row])
        b.append(1)

    #Anerobic runs must be at most 10 kilometers total
    for t in range(16*7):
        x = [0,1,0]
        y = [0,-10,0]
        next_row = np.concatenate((np.zeros(3*t),x,np.zeros(336-3-(3*t)),np.zeros(3*t),y,np.zeros(336-3-(3*t)),np.zeros(64)))

        A = np.vstack([A,next_row])
        b.append(0)

    ############### End Anerobic Constraints ###################




    ############### Start Threshold Constraints ################

    #Total weekly aerobic mileage 0.8-0.6 of total weekly mileage
    for t in range(16):

        x = [0,0,-1]*7
        d = np.concatenate((np.zeros(t),np.array([1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336+32),d,np.zeros(16)))
        
        A = np.vstack([A,new_row])
        b.append(-round((anerobic_threshold_mileage_ratio[t]*M[t]),1))
        
    for t in range(16):
        x = [0,0,-1]*7
        d = np.concatenate((np.zeros(t),np.array([-1]),np.zeros(15-t)))

        new_row = np.concatenate((np.zeros(t*21), x, np.zeros(315-(21*t)),np.zeros(336+32),d,np.zeros(16)))

        A = np.vstack([A,new_row])
        b.append(-round((anerobic_threshold_mileage_ratio[t]*M[t]),1))



    #Longest threshold run no longer than 10% total goal mileage
    for t in range(16*7):
        next_row = np.concatenate((np.zeros(3*t+2),np.array([1]),np.zeros(336-(3*t)-1-2),np.zeros(dim-336)))
        print(next_row)

        A = np.vstack([A,next_row])

    for t in range(16):
        for _ in range(7):
            b.append(0.1*M[t])


    
    #Threshold runs must be at most 15 kilometers
    for t in range(16*7):
        x = [0,0,1]
        y = [0,0,-15]
        next_row = np.concatenate((np.zeros(3*t),x,np.zeros(336-3-(3*t)),np.zeros(3*t),y,np.zeros(336-3-(3*t)),np.zeros(64)))

        A = np.vstack([A,next_row])
        b.append(0)

    ############### End Threshold Constraints ##################




    ############### Start General Constraints ##################

    #Between 3 and 6 runs per week
    for t in range(16):
        y = [1]*21
        next_row = np.concatenate((np.zeros(336+(21*t)),y,np.zeros(dim-336-21-(21*t))))
        A = np.vstack([A,next_row])
        b.append(6)

    for t in range(16):
        y = [-1]*21
        next_row = np.concatenate((np.zeros(336+(21*t)),y,np.zeros(dim-336-21-(21*t))))
        A = np.vstack([A,next_row])
        b.append(-3)



    #Only one run a day
    for t in range(16*7):
        y = [1,1,1]
        next_row = np.concatenate((np.zeros(336+(3*t)),y,np.zeros(397-(3*t))))
        A = np.vstack([A,next_row])
        b.append(1)

    ############### End General Constraints ####################

    


    #Objective function
    c = np.concatenate((np.zeros((dim-16)),np.ones((16))))



    #Determine bounds
    bounds = [(0,np.inf) for _ in range(336)]
    bounds.extend((0,1) for _ in range(336))
    bounds.extend((0,np.inf) for _ in range(64))



    #Specify integer variables
    x_i = [0 for i in range(336)]
    y_i = [1 for i in range(336)]
    alpha = [0 for i in range(16)]
    beta = [0 for i in range(16)]
    gamma = [0 for i in range(16)]
    delta = [0 for i in range(16)]
    isint = x_i + y_i + alpha + beta + gamma + delta



    #Calculate results
    results=opt.linprog(c,A,b,None,None,bounds,integrality = isint)


    print(A.shape)
    #Output results
    print(f"Optimal Objective Value (z): {results['fun']}")
    print(f"Optimal Decision Variable Vector (x): {results['x']}\n\n")