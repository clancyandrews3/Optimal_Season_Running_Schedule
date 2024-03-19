# Optimal Season Running Schedule

<hr>

## Introduction


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As a competitive runner, I wish to optimize my weekly running schedule, allowing me to focus on training and reap the performance benefits. Being busy with work and school as a priority, I don't always have time to sit down and write up a weekly running schedule that will allow me to have the most performance boosting results. Especially when the results of a workout are not determined until after a fortnight.  

&nbsp;

## Background


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are many aspects that go into planning a training schedule for a week. For this instance, the only prior information necessary for us to optimize a week of training is the previous week's total mileage. It is recommended that the total weekly mileage for the current week is only a 10% increase from the previous week's total mileage, to prevent over training and injury. We use the term mileage to indicate the total distance ran during the week, but the units for this distance is in meters, since most competitive races are measured using the metric system.  



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are three different types of workouts. Aerobic workouts, which improve the efficiency of the body's cardiovascular system in terms of oxygen intake and internal transportation of oxygen, involve longer runs at an easier pace. Anaerobic workouts, which improve muscle strength and speed, involve short, interval speed workouts, i.e., sprinting. Threshold workouts, which improve lactate levels in the body and prevent the onset of fatigue, involve 3 to 15 kilometer runs with an average heart rate at 80% of the individual's maximum heart rate.



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is typically advised that, of the total weekly mileage, 70% should be done doing aerobic workouts. Threshold workouts should account for 15% of the weekly total mileage and anaerobic workouts 15% of the total weekly mileage. It is also worth noting that the longest aerobic run of the week can only account for 30% of the total weekly mileage. The longest threshold run of the week should only account for 10% of the total weekly mileage. It is also important to train at least three times a week to see improvement and at most six times a week as to prevent injury.  

&nbsp;

## Goal

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our goal is to get as close to the target weekly mileage as we can. We can account for each workout type's total kilometers ran for each day using the decision variables $x_{ij}$ where $i$ corresponds to the $`i`$th day of the week for $i = 1,2,3,4,5,6,7$ representing Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively; $j$ corresponds to the $`j`$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively. It may also be necessary to add binary decision variables $y_{ij}$ for running a $`j`$th workout type on the $`i`$th day of the week for $i = 1,2,3,4,5,6,7$ representing Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively, and $j$ corresponding to the $`j`$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively.  

&nbsp;

## Progress


The project is currently in the modeling phase.

[] Model Objective Function
[] Model Independent/Dependent Variables
[] Model Constraints
[] Model Program in Python

&nbsp;

## Running the Code                                 <!-- May need to add installing spipy via pip3 -->

Contained in the `Code` folder is a python file used to solve the linear program. You can run the program in a few different ways.

&nbsp;

### Terminal

Going to the directory of the python file in a local terminal, you can run the following line to execute it:
```
python3 running_linear_program.py
```
and the code will be run.

&nbsp;

### IDE

In an IDE of your choice, you can run the program using the run functionality of the IDE, given that you have selected the appropriate interpreter.

&nbsp;

## Results

After running the program, the output will display the current feasibility of the linear program. Assuming it is feasible, you should get an optimal point $`x^*`$ and an optimal objective value $`z^*`$ . If the output for $`x^*`$ and $`z^*`$ is `None`, then the linear program is either infeasible or unbounded, and there is no solution.
