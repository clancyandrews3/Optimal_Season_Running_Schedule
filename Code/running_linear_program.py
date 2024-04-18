############################
# Optimal Season Running Schedule
# 
#
# Last Modified: April 18, 2024
# Author: Clancy Andrews
# Github: https://github.com/clancyandrews3/Optimal_Season_Running_Schedule
############################


import scipy.optimize as opt
import numpy as np


def get_starting_mileage():
    """Gets and returns starting mileage from user"""
    
    try:
        start_mileage = int(input("\nEnter the starting mileage for training: "))
    except:
        ValueError("Value needs to be a number.")
    
    return start_mileage


def output_results(results):
    """Output the results in a user friendly way"""
    
    for x_i in results:
        pass



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
    M_t = [0 for i in range(16)]
    d = [0 for i in range(16)]
    isint = x_i + y_i + M_t+d

    #Calculate results


    #Output results
    