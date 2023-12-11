import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
from time import perf_counter




def distance(point1, point2,distances):
    # print(point1,point2)
    return distances[point1][point2]

def update_speed(curr_weight, capacity,velocity_max, velocity_min):
    if curr_weight < capacity:
        return velocity_max - (curr_weight / capacity) * (velocity_max - velocity_min)
    else:
        return velocity_min


def cities_stolen(knapsack, assigned_nodes):
    print("KNAPSACK ", knapsack)
    print("ASsigned nodes ", assigned_nodes)
    if len(knapsack) != len(assigned_nodes):
        raise ValueError("Knapsack and assigned nodes must be of same length§")
    cities = {}
    item = 0
    for stolen,city in zip(knapsack,assigned_nodes):
        if stolen:
            if city in cities.keys():
                cities[city].append(item)
            else:
                cities[city] = [item]
        item += 1
    return cities


def time(point1, point2,curr_weight,capacity,velocity_max, velocity_min, distances):
    new_speed = update_speed(curr_weight,capacity,velocity_max, velocity_min)
    time = distance(point1,point2,distances) / new_speed
    if time == 0:
        time += 1
    return 20

def update_current_weight(current_weight, curr_city, cities_stolen,weights):
    items_stolen = cities_stolen.get(curr_city)
    if items_stolen:
        for item in items_stolen:
            current_weight += weights[item]
    return current_weight


def ant_colony_optimization(points, cities_stolen, weights, problem_details,n_ants=10, n_iterations=1000, alpha=1, beta=2, evaporation_rate=0.5, Q=1):
    '''

    Parameters
    ------------
    points: list
        list of cities

    n_ants: int
        Number of ants included in colony

    n_iterations: int
        Number of iterations to run

    alpha: float
        weight on pheromones - higher emphasizes importance of pheromones
       
    beta: float
        weight on heuristic (distance, cost) - higher increase reliance of this info on ant decision making
        

    evaperation rate: float
        rate of pheromone evaporation

    Q: Float
        Amount of pheromone deposited - higher the Q, more substantial increase in pheromone levels on nodes visited

    cities_stolen: Dict
        Dictionary showing which items were stolen at each city

    Returns
    --------
    '''

    capacity,velocity_min,velocity_max = problem_details
    n_points = len(points)
    pheromone = np.ones((n_points, n_points))  # Inital array of pheromones - all set as one
    best_path = None
    best_path_time = np.inf                  
    
    for iteration in range(n_iterations):
        print(f"Iteration {iteration}")
        paths = []
        path_times = []
        start_time = perf_counter()
        for ant in range(n_ants):
            visited = [False]*n_points
            current_point = 0    # Set initial point as a city 1
            visited[current_point] = True                   # Visited city tracker
            path = [current_point]
            path_time = 0
            current_weight = 0
            while False in visited:        # Check all cities
                unvisited = np.where(np.logical_not(visited))[0]      # Unvisted city array
                probabilities = np.zeros(len(unvisited))              # Empty probability list of traversing to each unvisited city
                
                # Calculate the probabilites of traveling to each city
                for i, unvisited_point in enumerate(unvisited):

                    probabilities[i] = pheromone[current_point, unvisited_point]**alpha / \
                        time(current_point, unvisited_point, \
                                update_current_weight(current_weight,current_point,cities_stolen,weights),capacity, velocity_max,velocity_min, distances=points)**beta
                    # Transition rule
                probabilities /= np.sum(probabilities)
                next_point = np.random.choice(unvisited, p=probabilities) # Randomly select next city using the probabilities
                path.append(next_point)
                path_time += time(current_point, next_point,update_current_weight(current_weight,current_point,cities_stolen,weights),capacity, velocity_max,velocity_min, distances=points)
                visited[next_point] = True
                current_point = next_point
            
            # Return to start city
            path.append(path[0])
            path_time += time(path[0],path[-1],update_current_weight(current_weight,current_point,cities_stolen,weights),capacity, velocity_max,velocity_min , distances=points)
            paths.append(path)
            path_times.append(path_time)
            
            # Update best path 
            if path_time < best_path_time:
                best_path = path
                best_path_time = path_time
        end_time = perf_counter
        
        pheromone *= evaporation_rate    # Update current pheromones
        
        # Calculate new pheromomnes
        for path, path_time in zip(paths, path_times): 
            for i in range(n_points-1):
                pheromone[path[i], path[i+1]] += Q/path_time  # Update pheromones on each city to city path
            pheromone[path[-1], path[0]] += Q/path_time       # Update pheromones on each city to city path
     
    return best_path, best_path_time
