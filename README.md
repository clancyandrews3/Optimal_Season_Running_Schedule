# Optimal Season Running Schedule

## Introduction


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As a competitive runner, I wish to optimize my weekly running schedule, allowing me to focus on training and reap the performance benefits. Being busy with work and school as a priority, I don't always have time to sit down and write up a weekly running schedule that will allow me to have the most performance boosting results. Especially when the results of a workout are not determined until after a fortnight.  

&nbsp;

## Background


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are many aspects that go into planning a training schedule for a week. For this instance, the only prior information necessary for us to optimize a week of training is the previous week's total mileage. It is recommended that the total weekly mileage for the current week is only a 10% increase from the previous week's total mileage, to prevent over training and injury. We use the term mileage to indicate the total distance ran during the week, but the units for this distance is in kilometers, since most competitive races are measured using the metric system.  



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;There are three different types of workouts. Aerobic workouts, which improve the efficiency of the body's cardiovascular system in terms of oxygen intake and internal transportation of oxygen, involve longer runs at an easier pace. Anaerobic workouts, which improve muscle strength and speed, involve short, interval speed workouts, i.e., sprinting. Threshold workouts, which improve lactate levels in the body and prevent the onset of fatigue, involve 3 to 15 kilometer runs with an average heart rate at 80% of the individual's maximum heart rate.



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It is typically advised that, of the total weekly mileage, between 60% to 80% should be done doing aerobic workouts. If this is the start of training, starting around 80% will allow an individual to develop an endurance "base". Once the base is built up, the threshold and anaerobic mileage can be increased to gain speed. The longest aerobic run of the week can only account for 30% of the total weekly mileage. Since long runs require more time to do, we want to set our longest run to be either on a Saturday or Sunday during the week. On the day after the long run, we can either do a shorter aerobic workout or have a recovery day. Threshold and anaerobic workouts should account for 10% to 20% of the weekly total mileage each. The longest threshold run of the week should only account for 10% of the total weekly mileage. At most 3 anaerobic workouts should be done during any one week and we cannot do two anaerobic workouts in a row. It is also important to train at least three times a week to see improvement and at most six times a week as to prevent injury. Only one workout of any type should be done per day.



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A typical season in track and field or cross country is around 4 months (3 months of normal season and 1 month of nationals in high school) with professional seasons lasting longer. For the average runner, it would be better to do a 4 month training plan so a break can be taken after the 4 months to prevent over training and burnout (as this frequently can happen). It would also be beneficial to taper near the end of the season to better get ready for any big races/competitions that are scheduled. Tapering is the reduction of mileage/running intensity and allows a runner to better prepare their body for competition via additional rest, nutrition, and fine tuning of running form. To start a taper, we can reduce the current mileage by 20% of the previous week's mileage. This will occur for the last 2 weeks of the season.  

&nbsp;

## Goal

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Our goal is to get as close to the target weekly mileage as we can. This will ensure that no overtraining will occur and we can still improve moving forward with training.

&nbsp;

## Objective Variables

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbspWe can account for each workout type's total kilometers ran for each day using the decision variables $x^t_{ij}$ where $i$ corresponds to the $`i`$th day of the $`t`$th week for $i = 1,2,3,4,5,6,7$ representing Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday, respectively; $j$ corresponds to the $`j`$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively; $t$ corresponds to the $`t`$th week where $t = 1,\ldots, 16$ for each week in the four month season. It may also be necessary to add binary decision variables $y^t_{ij}$ for running a $`j`$th workout type on the $`i`$th day of the $`t`$th week for $i = 1,2,3,4,5,6,7$ representing Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday, respectively, $j$ corresponding to the $j$th workout type for $j = 1,2,3$ representing aerobic, anaerobic, and threshold, respectively, and $t$ corresponding to the $t$th week where $t = 1,\ldots, 16$ for each week in the four month season. We will also have variables that are in place of constants that will be calculated after the user's input, or are dynamically determined by the stage in training. One such is $M^t$, representing the goal total mileage for week $t$. Another is $r^t_j$ representing the ratio a run can be of the total weekly mileage of week $t$ for workout type $j$. 

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
$$\delta^t = \left|\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}-M^t\right| \qquad \forall t = 1,\ldots ,16$$
which when linearized, result in the following constraints:
$$-\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}+\delta^t \le -M^t \qquad \forall t = 1,\ldots ,16$$
and
$$-\sum_{i = 1}^7\sum_{j=1}^3x^t_{ij}-\delta^t \le -M^t \qquad \forall t = 1,\ldots ,16.$$
These constraints allow us to relate the objective function to the difference of the total mileage ran for week $t$ and the goal total mileage of week $t$. In order for us to use $M^t$ to represent the $t$th week's goal total mileage, we must have a starting goal mileage for the season. Our current implementation gets the starting mileage in kilometers from the user before solving the mixed integer program. In our case, our starting mileage will be $20 \ km$. We then get the following constraints:
```math
$$
M^t = 
\begin{cases}
20 \ &\text{ if } \ t = 1 \\
\left|(1.1)M^{t-1}\right| &\text{ if }\ \forall t = 2,\ldots,14 \\
\end{cases}
$$
```

If $t = 15,16$, then we will change the $1.1$ value to $0.8$ to account for tapering at the end of the season. This allows us to set our current week's goal total mileage to a value as close to a 10% increase from the last weeks goal total mileage as possible and taper at the end. To use $r_j^t$ to represent the ratio a run can be of the total weekly mileage of week $t$ for workout type $j$, we have 
```math
$$
\begin{aligned}
r^t_1 &= 0.80 \qquad \forall t = 1, \ldots , 4 \\ 
r^t_1 &= 0.75 \qquad \forall t = 5, \ldots , 8 \\
r^t_1 &= 0.70 \qquad \forall t = 9, \ldots , 12 \\
r^t_1 &= 0.65 \qquad \forall t = 13, \ldots , 14 \\
r^t_1 &= 0.60 \qquad \forall t = 15, \ldots , 16.
\end{aligned}
$$
```
Both anaerobic and threshold workouts will have the same ratios between them, with 
```math
$$
\begin{aligned}
r^t_j &= 0.100 \qquad \forall t = 1, \ldots , 4   \qquad \forall j = 2,3  \\ 
r^t_j &= 0.125 \qquad \forall t = 5, \ldots , 8   \qquad \forall j = 2,3   \\
r^t_j &= 0.150 \qquad \forall t = 9, \ldots , 12  \qquad \forall j = 2,3  \\
r^t_j &= 0.175 \qquad \forall t = 13, \ldots , 14 \qquad \forall j = 2,3   \\
r^t_j &= 0.200 \qquad \forall t = 15, \ldots , 16 \qquad \forall j = 2,3  .
\end{aligned}
$$
```
Using those ratios will allow us to update the ratio of each workout type as we gear towards more speed at the end of the season.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We can now construct the constraints for each running type. We can start with aerobic workouts. Our first constraint is that the total aerobic mileage per week has to be as close to $r^t_1$ percent of the total mileage for week $t$. In this case, $r^1_1 = 0.80$ and will decrease to $r^{16}_1 = 0.60$ step-wise over the 16 weeks as stated above. We get the following constraints to represent this:
```math
$$
\begin{aligned}
-\sum_{i = 1}^7x^t_{i1}-\alpha^t &\le -(r^t_1)M^t  \qquad \forall t = 1,\ldots ,16\\
-\sum_{i = 1}^7x^t_{i1}+\alpha^t &\le -(r^t_1)M^t  \qquad \forall t = 1,\ldots ,16\\
\end{aligned}
$$
```
where
$$\alpha^t = \left|\sum_{i = 1}^7x^t_{i1}-(r^t_1)M^t\right| \qquad \forall t = 1,\ldots ,16.$$
We also have the constraint where the longest aerobic run of the week cannot exceed 30% of the total weekly mileage:
$$x_{i1}^t - (0.3)M^ty^t_{i1} \le 0 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1, \ldots, 7.$$
With these constraints, we can build an endurance base as well as strength for longer runs, further preventing injury.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The constraints for anaerobic workouts are a bit different than for the aerobic workouts. We are only allowed to do at most 3 anaerobic workouts a week. We have the following constraint to limit us to that:
$$\sum_{i=1}^7y_{i2}^t \le 3 \qquad \forall t = 1,\ldots ,16.$$
Taking the sum of anaerobic runs for each day of week $t$ and restricting it to be less than or equal to 3 is how we can successfully limit the total weekly anaerobic runs. We are not allowed to do two consecutive anaerobic workouts, resulting in the constraint
$$y^t_{i2}+y^t_{(i+1)2} \le 1 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1, \ldots , 7.$$
The total anaerobic mileage must be around 10% of the total weekly mileage at the start of the season and will end at 20% near the end of the season. We have
$$\beta^t =\left|\sum_{i=1}^7x^t_{i2}-(r^t_2)M^t\right| \qquad \forall t = 1,\ldots ,16$$
which results in
$$-\sum_{i=1}^7x^t_{i2}+\beta^t \le-(r^t_2)M^t \qquad \forall t = 1,\ldots ,16$$
and
$$-\sum_{i=1}^7x^t_{i2}-\beta^t \le -(r^t_2)M^t \qquad \forall t = 1,\ldots ,16.$$
Lastly, the longest anaerobic workout session cannot be longer than 10% of the total goal weekly mileage. We have
$$x^t_{i2} - (0.1)M^ty^t_{i2} \le 0 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1, \ldots , 7.$$
With these constraints in place, we will be able to get faster while not sacrificing our endurance base in the process.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For threshold workouts, we have a couple different set of constraints. First, any threshold run we do must be at most 15 kilometers long. We get the following constraint to represent this:
$$x^t_{i3} -15y^t_{i3} \le 0 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1, \ldots, 7.$$
We also have that the total threshold mileage must be at around 10% of the total weekly mileage goal for each week $t$ and will increase to 20% by the end of the season. We then have
$$\gamma^t =\left|\sum_{i=1}^7x^t_{i3}-(r^t_3)M^t\right| \qquad \forall t = 1,\ldots ,16$$
which results in
$$-\sum_{i=1}^7x^t_{i3}+\gamma^t \le-(r^t_3)M^t \qquad \forall t = 1,\ldots ,16$$
and
$$-\sum_{i=1}^7x^t_{i3}-\gamma^t \le -(r^t_3)M^t \qquad \forall t = 1,\ldots ,16.$$
Lastly, similar to the aerobic constraint for maximum distance a run can be based on weekly mileage, the longest threshold run cannot exceed 10% of the total weekly mileage. By setting the constraint where the threshold mileage for any day $i$ of week $t$ to be less than or equal to 20% of the corresponding goal weekly mileage $M^t$, we get
$$x^t_{i3} - (0.2)M^ty^t_{i3} \le 0 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1, \ldots , 7.$$
Having these constraints will allow us to increase our tolerance to the onset of fatigue while running, and assist in our body's ability to combine our endurance and speed for competition.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the rest of the constraints, we have
$$3\le\sum_{i=1}^7\sum_{j=1}^3y_{ij}^t \le 6 \qquad \forall t = 1,\ldots ,16$$
so we run at least 3 times a week and at most 6 times a week. There is also the constraint that stops us from doing more than one run a day:
$$\sum_{j=1}^3y_{ij}^t \le 1 \qquad \forall t = 1,\ldots ,16 \qquad \forall i = 1,\ldots, 7.$$

&nbsp;

## Results

&nbsp;

### Interpreting Clean Results

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The results presented in the clean output style will make it more easy to understand what is going on. Each week will present each day's workout type and number of kilometers to run. That way there is no difficulty in interpretation, allowing you to focus on training.

&nbsp;

### Interpreting Raw Results

&nbsp;

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The results for the non-clean output style can be a bit confusing, so it would be preferred to use the clean output style for a more user friendly method. To better understand the output from the solution of the mixed integer program, the output vector $x^*$ will be as follows:
```math
$$ x^* = \begin{bmatrix}x^1_{11} & x^1_{12} & x^1_{13} & x^1_{21} & \cdots & y^1_{11} & y^1_{12} & y^1_{13} & y^1_{21} & \cdots & \alpha^1 & \cdots & \alpha^{16}& \beta^1 & \cdots & \beta^{16}& \gamma^1 & \cdots & \gamma^{16} & \delta^1 & \cdots & \delta^{16}\end{bmatrix} $$
```
There are a total of $736$ components to the $x^*$ vector. The first $336$ components are the $x^t_{ij}$ values. They are presented as each workout type for each day of the first week, then the three workout types for the second day of the first week, and so on through all 112 days of the 16 week season. The second group of $336$ components ($337 - 672$) are the $y^t_{ij}$ values. The are presented in the same way that the $x^t_{ij}$ components are. Components $673 - 688, 689 - 704, 705 - 720$ are the dependent variables $\alpha, \ \beta, \ \gamma$, used to linearize the functions that get the aerobic, anaerobic, and threshold weekly totals as close to their respective ratios of total goal weekly mileage. The last set of components ($721-736$) are the values of $\delta^t$. The $\delta$ values are utilized in linearizing the objective function, allowing us to solve the problem as a linear program.

&nbsp;

## Progress


The project is completed as of version 1.

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

After running the program, the output will display the current feasibility of the linear program. Assuming it is feasible, you should get an optimal point $`x^*`$ and an optimal objective value $`z^*`$. If the output for $`x^*`$ and $`z^*`$ is `None`, then the linear program is either infeasible or unbounded, and there is no solution.
