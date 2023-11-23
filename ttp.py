import sys
import numpy as np
import pandas as pd
import random
import os
import math
import csv


LEAST_SOLUTIONS = []
CITY_DATA = []
KNAPSACK_CAPACITY = 0
ITEMS_DATA = []
NUMBER_OF_ITEMS = 0
MIN_SPEED = 0.0
MAX_SPEED = 0.0


def main():
    pass


def initial_data(filepath:str) -> None:
    """
    Takes as input a filename, reads the data from the file and updates the global variables
        CITY_DATA = []
        KNAPSACK_CAPACITY = 0
        ITEMS_DATA = []
        NUMBER_OF_ITEMS = 0
        MIN_SPEED = 0.0
        MAX_SPEED = 0.0
    with the values from the file

    input = filepath
    output = None
    """
    with open(filepath) as f:
        pass

def fitness(solution) -> (float,float,float):
    """
    Fitness function takes a solution and returns its fitness as a tuple(time,profit)

    input = 
    """
    return time,profit

def update_solutions(new_solution:):
    """
    If new_solution is better than any solution in LEAST_SOLUTIONS then replace the worst one.

    input: new_solution
    output: None
    """
def calculate_speed():
    pass

def calculate_time():
    pass

def get_distance(cityA:int,cityB:int) -> int:
    """
    Given two cities, return their distance from the CITY_DATA
    """
    pass

def get_item_value(city_index,item_index):
    """
    Given an item and a city, return the value of the item using ITEM_DATA
    """

def get_item_weight(city_index,item_index):
    pass


def is_valid_solution(solution):
    """
    Takes as input the solution and r
    """
    pass


def algorithm():
    



if __name__ == "__main__":
    main()