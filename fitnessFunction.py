import math
"""
The function builds in, the path is determined, and then a list of item pickup flags is randomly generated 
to determine whether or not items need to be picked up to reach the city, 
and which items to pick up. And includes speed updates, and time and profit calculations. 
Subsequent changes can be adjusted according to the needs of changes


"""

def calculate_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0]) ** 2 + (city2[1] - city1[1]) ** 2)


def update_speed(u_weight):
    return velocity_max - (u_weight / Q) * (velocity_max - velocity_min)


def fitness_function(c_path, distance, p_flag, c_flag, c_weight, c_profit):
    total_weight = 0
    total_time = 0
    total_profit = 0
    for i in range(len(c_path) - 1):
        city_start = c_path[i] - 1
        city_end = c_path[i + 1] - 1
        speed = update_speed(total_weight)
        if p_flag[city_end - 1]:
            flag = c_flag[city_end - 1]
            for j in range(len(flag)):
                if flag[j]:
                    total_weight += c_weight[city_end - 1][j]
                    total_profit += c_profit[city_end - 1][j]
        # if the maximum capacity constraint is reached, Adding a penalty mechanism
        if total_weight > Q:
            total_time = float('inf')
            total_profit = -float('inf')
            break
        total_time += distance[city_start][city_end] / speed
    if total_weight <= Q:
        speed = update_speed(total_weight)
        total_time += distance[city_start][city_end] / speed
    # The fitness value can be calculated based on the set time and profit weights.
    # We can add two parameters
    # fitness_value = alpha * total_time + beta * total_profit
    # fitness_value = round(fitness_value, 3)
    objects = [round(total_time, 3), total_profit]
    # return total_weight, fitness_value, objects
    return total_time, total_profit, objects


# RENTING RATIO
R = 5.1
alpha = 0.4
beta = 0.6
path = [1, 3, 2, 4]
velocity_max = 0.8
velocity_min = 0.1
# maximal weight of the knapsack
Q = 30
path_flag = [1, 0, 1]
city_flag = [[1, 1, 0], [0, 0, 1], [0, 1, 0]]
weight = [[2, 3, 5], [3, 1, 5], [5, 11, 2]]
profit = [[20, 32, 45], [13, 21, 5], [57, 15, 26]]
distance_matrix = [[0, 30, 20, 15], [52, 0, 21, 23], [45, 32, 0, 21], [15, 65, 16, 0]]
solution = [[20, 57], [85, 64], [48, 85]]
knapsack, value, p_object = fitness_function(path, distance_matrix, path_flag, city_flag, weight, profit)
print(knapsack)
print(value)
print(p_object)


