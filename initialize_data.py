import numpy as np
import pandas as pd
import re
import math

def parse_knapsack_data(filename, printed=False):
    """
        Parses knapsack data from a string and returns a tuple containing information about the knapsack problem.

    Args:
        data (str): A string containing knapsack problem data.

    Returns:
        Tuple[str, str, int, int, int, float, float, float, str, List[Tuple[float, float]], List[Tuple[int, int, int]]]:
            A tuple containing the following information:
            - Problem Name (str)
            - Knapsack Data Type (str)
            - Dimension (int)
            - Number of Items (int)
            - Capacity of Knapsack (int)
            - Min Speed (float)
            - Max Speed (float)
            - Renting Ratio (float)
            - Edge Weight Type (str)
            - Node Coordinates (List[Tuple[float, float]])
            - Item Data (List[Tuple[int, int, int]])
        """
    try:
        with open(filename, 'r') as file:
            data = file.read()
    except FileNotFoundError as e:
         raise FileNotFoundError("File not found")
    lines = data.split('\n')

    problem_name = lines[0].split(':')[1].strip()
    knapsack_data_type = lines[1].split(':')[1].strip()
    dimension = int(lines[2].split(':')[1].strip())
    num_items = int(lines[3].split(':')[1].strip())
    capacity_of_knapsack = int(lines[4].split(':')[1].strip())
    min_speed = float(lines[5].split(':')[1].strip())
    max_speed = float(lines[6].split(':')[1].strip())
    renting_ratio = float(lines[7].split(':')[1].strip())
    edge_weight_type = lines[8].split(':')[1].strip()

    locations = []
    profits = []
    weights = []
    assigned_node_numbers = []

    for index,line in enumerate(lines[10:]):

        if (line.split()[0]) == "ITEMS":
            items_data_location = index + 11
            break 
        index,x,y = line.split()
        index,x,y = int(index), int(x), int(y)
        locations.append([index,x,y])
    for index,line in enumerate(lines[items_data_location:]):
        split_line = line.split()
        if len(split_line) == 0:
            break
        index, profit, weight, assigned_node_number = line.split()
        index,profit,weight,assigned_node_number = int(index), int(profit), int(weight), int(assigned_node_number) - 1
        profits.append(profit)
        weights.append(weight)
        assigned_node_numbers.append(assigned_node_number)

    if print:
            print( f"Problem Name: {problem_name}\n" \
           f"Knapsack Data Type: {knapsack_data_type}\n" \
           f"Dimension: {dimension}\n" \
           f"Number of Items: {num_items}\n" \
           f"Capacity of Knapsack: {capacity_of_knapsack}\n" \
           f"Min Speed: {min_speed}\n" \
           f"Max Speed: {max_speed}\n" \
           f"Renting Ratio: {renting_ratio}\n" \
           f"Edge Weight Type: {edge_weight_type}\n" \
           f"Distances: {initial_city_matrix(locations,dimension)}\n" \
           f"Profits: {profits}\n" \
           f"Weights: {weights} \n" \
           f"Assigned Node Numbers: {assigned_node_numbers}\n" )


    return (
    problem_name,
    knapsack_data_type,
    dimension,
    num_items,
    capacity_of_knapsack,
    min_speed,
    max_speed,
    renting_ratio,
    edge_weight_type,
    initial_city_matrix(locations,dimension),
    profits,
    weights,
    assigned_node_numbers
)

def initial_city_matrix(NODE_COORD_SECTION,DIMENSION):

    CITY_MATRIX = [[0 for j in range(DIMENSION)] for i in range(DIMENSION)]

    for i in range(0, DIMENSION):

        for j in range(0, DIMENSION):
            if i == j:
                CITY_MATRIX[i][j] = 0
            elif i > j:
                CITY_MATRIX[i][j] = CITY_MATRIX[j][i]
            else:
                distance = (abs(NODE_COORD_SECTION[i][1] - NODE_COORD_SECTION[j][1]) ** 2 + \
                                    abs(NODE_COORD_SECTION[i][2] - NODE_COORD_SECTION[j][2]) ** 2) ** 0.5
                CITY_MATRIX[i][j] = math.ceil(distance)
    return CITY_MATRIX
