import numpy as np
import random
import math

def local_search(profits, weights, capacity,n=100000, discretion=0.5, annealing_prob=0, initial_solution_type='intuitive'):
    """
    NOTE: An assumption is made that the list of profits and weights correspond to thesame items. That is, profits[0] and weights[0] refer to the profits
    and weights for item 0

    NOTE: Our local search might work better with the ACO if we provide information about which cities we're visiting first. This
    allows us improve the probability of picking items towards the end of our route. Although this may be detrimental to the knapsack problem in seclusion,
    it might provide better pareto optimal solutions.

    Local search algorithm to be used to calculate the best combination of items to take in order to maximise the 
    weight of the bag without exceeding the capacity.

    Two heuristics are employed in selecting the initial solution:

    a.    A heuristic is used to choose items with the greatest profit/weight ration. This is because items that weigh less and
        have higher profits allow us to pick more items. This is implemented as a kind of tournament solution because even items with low profit to weight ratio are desirable.
        The logic is explained as follows:
        - The ratio of profits to weights is calculated for the items
        - The probability distribution is then calculated by dividing the array with the sum of the ratios
        * In order to use this as a probability of selecting an item then we need to scale it up
            ** We can do this by using a multiplier
            ** The multiplier has to be a value that will lead to us selecting the closest weight to the capacity of the knapsack
            ** This means that we need to have an approximate idea of how many items we need to pick from the knapsack
            ** We can get this by dividing the knapsack capacity by the average weight of the objects
            ** We want to start with a half filled knapsack so that we can consistently improve so we divide the multiplier by 2

    b.    A second heuristic is chosen to ensure that we have a nice selection of items and not just huge items being selected, this heuristic is called discretion.
        If the weight of the object is larger than the knapsack capacity * discretion, then don't pick it.
    

    Inputs:
    n: number of iterations to run
    profits: list of profits for the items
    weights: list of weights for the items
    capacity: capacity of knapsack
    discretion: the probability that controls whether or not we carry really heavy items from the onset
    initial_solution_type: the logic described above gives us an intuitively good initial solution, we can also initialize a random solution
    """
    w = np.array(weights)
    p = np.array(profits)
    ratio = np.array(p) / np.array(w)
    total_ratio = ratio.sum()
    prob_distribution = ratio/total_ratio
    multiplier = capacity / (w.mean())
    probabilities = prob_distribution * multiplier
    def initialize_solution():
        """ 
        This subfunction initializes a solution

        - Intuitive uses information about the ratio of profit/weight while random randomly picks items to be selected
        """
        solution = []
        if initial_solution_type == 'intuitive':
            for index,i in enumerate(probabilities):
                print("Probablities: ", probabilities)
                random_float = random.random()
                if i <= random_float:
                    if weights[index] < capacity * discretion:
                        solution.append(1)
                    else:
                        solution.append(0)
                else:
                    solution.append(0)
        elif initial_solution_type == 'random':
            
            # define a threshold for the random items picked. The higher the threshold the higher the number of items picked
            threshold = 0.4
            solution_fitness = -math.inf
            # execute while the fitness of the solution is infinity. This ensures that we only consider valid solutions
            while solution_fitness == -math.inf:
                print("Stuck here")
                for i in range(len(weights)):
                    random_float = random.random()
                    if random_float > threshold:
                        solution.append(1)
                    else:
                        solution.append(0)
                solution_fitness = fitness(solution)[0]        
        else:
            raise TypeError(f"Invalid argument: {initial_solution_type}")
        return solution
    
    def generate_neighbor(solution):
        # print("Solution is:", solution)
        # flip the bit at a random index
        index = random.randint(0,len(solution)-1)
        solution[index] = 1 if not solution[index] else 0
        new_solution = solution
        # if the new solution is infeasible, fix it and flip a different bit
        while fitness(new_solution)[0] == -math.inf:
            solution[index] = 0
            index = random.randint(0,len(solution)-1)
            new_solution[index] = 1
        # return the neighbor
        return new_solution
    
    def fitness(solution):
        # Return the profit and weight of a solution. Return neg infinity if the solution is infeasible(weight is too high)
        total_profit = 0
        total_weight = 0
        for weight,profit,picked in zip(weights,profits,solution):
            if picked:
                total_profit += profit
                total_weight += weight
        if total_weight > capacity:
            return [-math.inf,total_weight]
        return [total_profit,total_weight]

    solution = initialize_solution()
    for i in range(n):
        print(f"Local search iteration {i}")
        new_solution = generate_neighbor(solution)
        fitness_new = fitness(new_solution)
        fitness_curr = fitness(solution)
        if fitness_new[0] > fitness_curr[0] and fitness_new[1] != -math.inf:
            solution = new_solution
    print(f"Total weight of knapsack: {fitness(solution)} / {capacity}")
    return solution





