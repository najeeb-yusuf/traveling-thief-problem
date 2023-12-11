# README: Traveling Thief Problem (TTP) with Genetic Algorithm and Ant Colony Optimal

 

# Overview

The purpose of this project is to address TTP issues. We implemented two separate algorithms: the ACO as well as the GA algorithm to compare the results.

 

# Prerequisites

\- Python 3. 11;

\- Required Python libraries: ‘numpy’, ‘re’, ‘os’ 'random' and 'time'. 

 

## Usage

1. Clone or download the program files to your local machine.

2. Examples of data files include the following files. We control the use of a single or specified data file to perform experiments by adding comment symbols.

   ![image-20231211173101579](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211173101579.png)

​                               

3. Regarding the ACO algorithm, we can modify the number of ants and the maximum number of iterations(AntColonyOptimization.py) to determine the termination condition.

   ![image-20231211173557261](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211173557261.png)

4. Regarding the GA algorithm, we can improve the efficiency of the operation for different data files by modifying the number of populations, the tournament selection size, and the maximum number of iterations(GeneticAlgorithm.py).

   ![image-20231211173620299](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211173620299.png)

5. Control the execution of different algorithms by annotating or releasing the corresponding algorithm execution statements(Runner.py).

   ![image-20231211173753811](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211173753811.png)

6. The results are saved to the appropriate data file according to the contest criteria. and stored in a folder named results. Like this: 

   ![image-20231211174146158](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211174146158.png)

   

# Parameters

ACO Algorithm:

- num_ants: The number of ants.

- alpha: The hyper parameter of the pheromone matrix

- beta: The hyper parameter of the heuristic matrix

- evaporation_rate: the rate of evaporation

- max_iterations: The number of generations for the algorithm to run

GA Algorithm:

- ‘Pop_size’: Initial population size.

- ‘Tour_size’: Tournament selection sample size.

- ‘Termination_Criterion’: The number of generations for the algorithm to run.

By modifying the variable values above, different data experiments have been conducted.

 

## Program Components

- readTxtFile: Read the data from the data file

- getDistanceMatrix: Initialize the distance matrix

- getDistance: Get the distance values between cities from the distance matrix

- getItemMatrix: Items are filtered by localsearch, generating the weight of the item as well as a profit matrix. Filter items by setting a queue on the ratio of weight to profit.

- ACO:

  - generate_Heuristic_Matrix: Initializing the heuristic matrix using the distance
  - initialize_pheromones: Initializing the pheromones matrix 
  - update_flags: Optimise the list of flags for pickup scenarios to ensure that the pack weight limit is met before calculating fitness
  - solve: ACO algorithm implementation

- GA:

  - initialize_population: Generating the initial population
  - initialize_flag: Generating the initial flag list
  - update_flags: Optimize the list of flags for pickup scenarios to ensure that the pack weight limit is met before calculating fitness
  - tournament_selection: Generation of parent samples by tournament selection strategy
  - order_crossover: Crossover the path
  - crossover_flag: Crossover the list of flag
  - inversion_mutation: Reverse mutation of paths and the list of flag
  - repalcement: Renewal of populations.

- Non-Dominate Set:

  add & get_relation: Used to check the generated results and generate non-dominated sets

- write_solutions: Data is stored according to the requirements of the competition and saved to the appropriate data file.

- print_solutions: Print the final generated solution

   

## Output

- The program will display the path found, the picking scheme, its time, profit and execution time.

- The results will be saved in a text file named "team_name_problem_name.x" or"team_name_problem_name.f"

  - "team_name_problem_name.f": Save time and profit

  - "team_name_problem_name.x": Save paths and item picking scheme

    Like this:

    ![image-20231211184309665](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211184309665.png)

    ![image-20231211184326050](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211184326050.png)

 

## Example

If don't need the set the parameters that you want, just run the python file(Runner.py)

![image-20231211184811563](C:\Users\hang1\AppData\Roaming\Typora\typora-user-images\image-20231211184811563.png)



 

## Authors

\- Nature Inspired Computation - GROUP N

- WILKINSON, Charlie
- RAHATAL, Ritesh Sunil

- JIN, Hongjin

- WANG, Peitao

- YUSUF, Najeeb

- LIU, Sihang

 

## Acknowledgments

\- The program is based on the concept of Genetic Algorithm, Ant Colony Optimal and the Traveling Thief Problem.

 