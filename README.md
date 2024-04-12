# Optimal Season Running Schedule

## Introduction


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As a competitive runner, I wish to optimize my weekly running schedule, allowing me to focus on training and reap the performance benefits. Being busy with work and school as a priority, I don't always have time to sit down and write up a weekly running schedule that will allow me to have the most performance boosting results. Especially when the results of a workout are not determined until after a fortnight.  

&nbsp;

## Background


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are many aspects that go into planning a training schedule for a week. For this instance, the only prior information necessary for us to optimize a week of training is the previous week's total mileage. It is recommended that the total weekly mileage for the current week is only a 10% increase from the previous week's total mileage, to prevent over training and injury. We use the term mileage to indicate the total distance ran during the week, but the units for this distance is in meters, since most competitive races are measured using the metric system.  



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are three different types of workouts. Aerobic workouts, which improve the efficiency of the body's cardiovascular system in terms of oxygen intake and internal transportation of oxygen, involve longer runs at an easier pace. Anaerobic workouts, which improve muscle strength and speed, involve short, interval speed workouts, i.e., sprinting. Threshold workouts, which improve lactate levels in the body and prevent the onset of fatigue, involve 3 to 15 kilometer runs with an average heart rate at 80% of the individual's maximum heart rate.



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is typically advised that, of the total weekly mileage, 70% should be done doing aerobic workouts. Threshold workouts should account for 15% of the weekly total mileage and anaerobic workouts 15% of the total weekly mileage. It is also worth noting that the longest aerobic run of the week can only account for 30% of the total weekly mileage. The longest threshold run of the week should only account for 10% of the total weekly mileage. It is also important to train at least three times a week to see improvement and at most six times a week as to prevent injury.  

&nbsp;

## Goal

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our goal is to get as close to the target weekly mileage as we can. This will ensure that no overtraining will occur and we can still improve moving forward with training.

&nbsp;

## Objective Variables

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We can account for each workout type's total kilometers ran for each day using the decision variables $x^t_{ij}$ where $i$ corresponds to the $i$th day of the $t$th week for $i = 1,2,3,4,5,6,7$ representing Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively; $j$ corresponds to the $j$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively; $t$ corresponds to the $t$th week where $t = 1,\ldots, 16$ for each week in the four month season. It may also be necessary to add binary decision variables $y^t_{ij}$ for running a $j$th workout type on the $i$th day of the $t$th week for $i = 1,2,3,4,5,6,7$ representing Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, and Saturday, respectively, $j$ corresponding to the $j$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively, and $t$ corresponding to the $t$th week where $t = 1,\ldots, 16$ for each week in the four month season. We will also have dependent variables $M^t$ representing the goal total mileage for week $t$. 

&nbsp;

## Objective Function

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Given our objective variables above, we can formulate the objective function as follows:

$$\min \ z = \sum_{t=1}^{16}\delta^t$$

where 

$$\delta^t = \left|\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}-M^t\right|.$$ 

The goal of the objective function is to minimize the difference of the total mileage ran for week $t$ and the goal total mileage of week $t$. Therefore, each week will be as close to the goal mileage as possible.

&nbsp;

## Constraints

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We can model the different constraints stated in the background section using the objective variables. We can start my relating the dependent variables stated above to the independent variables. For the $\delta^t$ values, we have
$$\delta^t = \left|\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}-M^t\right|$$
which when linearized, result in the following constraints:
$$-\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}+\delta^t \le -M^t$$
and
$$-\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}-\delta^t \le -M^t.$$
These constraints allow us to relate the objective function to the difference of the total mileage ran for week $t$ and the goal total mileage of week $t$. In order for us to use $M^t$ to represent the $'t'$th week's goal total mileage, we must have a starting goal mileage for the season. Our current implementation gets the starting mileage in kilometers from the user before solving the linear program. In our case, our starting mileage will be $20 \ km$. We then get the following constraints:
```math
$$
M^t = 
\begin{cases}
20 \ &\text{ if } \ t = 1 \\
\left|(1.1)M^{t-1}\right| \ &\text{ otherwise}
\end{cases}
```

$$
This allows us to set our current week's goal total mileage to a value as close to a $10\%$ increase from the last weeks goal total mileage as possible.

&nbsp;

## Results

&nbsp;

### Interpreting Results

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The results will generally be output in a more user friendly matter. To better understand the output from the solution of the linear program, the output vector $x^*$ will be as follows:
```math
$$ x^* = \begin{bmatrix}x^1_{11} & x^1_{12} & x^1_{13} & x^1_{21} & x^1_{22} & x^1_{23} & x^1_{31} & \cdots & y^1_{11} & y^1_{12} & y^1_{13} & y^1_{21} & \cdots & M^1 & M^2 & \cdots & M^{16} & \delta^1 & \delta^2 & \cdots & \delta^{16}\end{bmatrix} $$
```
There are a total of $704$ components to the $x^*$ vector. The first $336$ components are the $x^t_{ij}$ values. They are presented as each workout type for each day of the first week, then the three workout types for the second day of the first week, and so on through all 112 days of the 16 week season. The second group of $336$ components ($337 - 672$) are the $y^t_{ij}$ values. The are presented in the same way that the $x^t_{ij}$ components are. Components $673 - 688$ are the goal total weekly mileage values for each of the 16 weeks. The last set of components ($689-704$) are the values of $\delta^t$. The $\delta$ values are utilized in linearizing the objective function, allowing us to solve the problem as a linear program.

&nbsp;

## Progress


The project is currently in the modeling phase.

- [x] Model Independent/Dependent Variables
- [x] Model Objective Function
- [x] Model Output
- [ ] Model Constraints

&nbsp;

## Running the Code

Contained in the `Code` folder is a python file (`.py`) used to solve the linear program. You can run the program in a few different ways. You will first want to make sure that the dependencies are installed before hand. For this program, `numpy` and `scipy` libraries are utilized. You can install them using the command line:

```
pip3 install numpy
pip3 install scipy
```
Once those packages are installed, you will be able to execute the program.

&nbsp;

### Execution via Terminal

Going to the directory of the python file in a local terminal, you can run the following line to execute it:
```
python3 running_linear_program.py
```
and the code will be run. The output of the program will be displayed in the terminal.

&nbsp;

### Execution via IDE

In an IDE of your choice, you can run the program using the run functionality of the IDE, given that you have selected the appropriate interpreter. Once the program is executed, you will be displayed the result in the console.

&nbsp;

## Output

After running the program, the output will display the current feasibility of the linear program. Assuming it is feasible, you should get an optimal point $'x^*'$ and an optimal objective value $'z^*'$. If the output for $'x^*'$ and $'z^*'$ is `None`, then the linear program is either infeasible or unbounded, and there is no solution.
