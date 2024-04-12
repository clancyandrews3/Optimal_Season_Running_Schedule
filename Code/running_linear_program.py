############################
# Optimal Season Running Schedule
# 
#
# Last Modified: April 11, 2024
# Author: Clancy Andrews
# Github: https://github.com/clancyandrews3/Optimal_Season_Running_Schedule
############################


import scipy.optimize as opt
import numpy as np


def get_starting_mileage():
    """Gets and returns starting mileage from user"""
    
    try:
        start_mileage = int(input("Enter the starting mileage for training: "))
    except:
        ValueError("Value needs to be a number.")
    
    return start_mileage


def output_results(results):
    """Output the results in a user friendly way"""
    
    for x_i in results:
        pass



if __name__=="__main__":

    #Get starting milage
    mileage = get_starting_mileage()
    print(mileage)
    
    #Objective function
    c = np.array([])

    #Inequality and equality constraints
    A = np.array([[]])
    Ae = np.array([[]])

    #Constraint values
    b = np.array([])
    be = np.array([])

    #Determine bounds
    bounds = ()

    #Specify integer variables
    isint = []