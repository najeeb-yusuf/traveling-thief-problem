import math
import numpy as np
import random

DIMENSION = 0
NUMBER_OF_ITEMS = 0
KNAPSACK_CAPACITY = 0
MIN_SPEED = 0.0
MAX_SPEED = 0.0
RENTING_RATIO = 0.0
CITY_MATRIX = []
ITEMS_SECTION = []
choose_items_combination = []
choose_weight_combination = []
choose_profit_combination = []

def initial_data(filepath: str) -> None:
    global DIMENSION, NUMBER_OF_ITEMS, KNAPSACK_CAPACITY, MIN_SPEED, MAX_SPEED, RENTING_RATIO, ITEMS_SECTION

    NODE_COORD_SECTION = []
    ITEMS_SECTION = []

    try:
        with open(filepath, 'r') as file:
            lines = file.readlines()

            CITY_BOOL = False

            ITEM_BOOL = False
            for line in lines:
                # 去除开头和结尾的空白字符
                line = line.strip()

                # 将节点坐标添加到二维数组
                if CITY_BOOL:
                    if line.startswith("ITEMS SECTION"):
                        CITY_BOOL = False
                    else:
                        parts = line.split()
                        NODE_COORD_SECTION.append([int(parts[0]), int(parts[1]), int(parts[2])])
                        continue

                if ITEM_BOOL:
                    parts = line.split()
                    if len(parts) == 4:
                        ITEMS_SECTION.append([int(parts[0]), int(parts[1]), int(parts[2]), int(parts[3])])
                        continue

                # 根据关键词来解析文件内容
                if line.startswith("DIMENSION"):
                    DIMENSION = int(line.split(":")[1].strip())
                elif line.startswith("NUMBER OF ITEMS"):
                    NUMBER_OF_ITEMS = int(line.split(":")[1].strip())
                elif line.startswith("CAPACITY OF KNAPSACK"):
                    KNAPSACK_CAPACITY = int(line.split(":")[1].strip())
                elif line.startswith("MIN SPEED"):
                    MIN_SPEED = float(line.split(":")[1].strip())
                elif line.startswith("MAX SPEED"):
                    MAX_SPEED = float(line.split(":")[1].strip())
                elif line.startswith("RENTING RATIO"):
                    RENTING_RATIO = float(line.split(":")[1].strip())
                elif line.startswith("NODE_COORD_SECTION"):
                    CITY_BOOL = True
                elif line.startswith("ITEMS SECTION"):
                    ITEM_BOOL = True

        initial_city_matrix(NODE_COORD_SECTION)

    except FileNotFoundError:
        print(f"文件 '{filepath}' 未找到.")
    except Exception as e:
        print(f"发生错误: {e}")

def initial_city_matrix(NODE_COORD_SECTION):

    global CITY_MATRIX
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

def get_city_distance(city_index_a, city_index_b):

    if city_index_a > DIMENSION or city_index_b > DIMENSION:
        print("index out of range!!!")
        return 0
    return CITY_MATRIX[city_index_a - 1][city_index_b - 1]

# KNP EA solution
def initialize_population(population_size, num_items, max_weight):
    population = []
    while len(population) < population_size:
        individual = np.random.choice([0, 1], size=num_items)
        total_weight = np.sum(np.array(ITEMS_SECTION)[:, 2] * individual)
        if total_weight <= max_weight:
            population.append(individual)
    return population

def calculate_fitness(individual, items):
    total_weight = np.sum(np.array(items)[:, 2] * individual)
    total_profit = np.sum(np.array(items)[:, 1] * individual)

    return total_profit, total_weight

def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2

def mutate(individual, mutation_rate):
    mutated = individual.copy()
    for i in range(len(mutated)):
        if random.uniform(0, 1) < mutation_rate:
            mutated[i] = 1 - mutated[i]
    return mutated

def genetic_algorithm(items, max_weight, population_size=50, max_generation=100, mutation_rate=0.1, top_items=10):
    num_items = len(items)
    population = initialize_population(population_size, num_items, max_weight)

    for generation in range(max_generation):
        population = sorted(population, key=lambda x: calculate_fitness(x, items), reverse=True)
        parents = population[:2]
        offspring = []

        for i in range(0, population_size - 1, 2):
            parent1, parent2 = random.choices(parents, k=2)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1, mutation_rate)
            child2 = mutate(child2, mutation_rate)
            offspring.extend([child1, child2])

        # 更新后的 offspring 保持总重量不超过 max_weight，替换 population 中适应度更低的个体
        for ind in offspring:
            total_weight_offspring = np.sum(np.array(items)[:, 2] * ind)
            fitness_offspring = calculate_fitness(ind, items)[0]

            min_fitness_index = min(range(population_size),
                                    key=lambda x: calculate_fitness(population[x], items)[0])
            if total_weight_offspring <= max_weight and fitness_offspring > \
                    calculate_fitness(population[min_fitness_index], items)[0]:
                population[min_fitness_index] = ind

        # 选择总重量不超过 max_weight 的物品
        best_solutions = sorted(population, key=lambda x: calculate_fitness(x, items), reverse=True)[
                         :top_items]

    return best_solutions

def get_items_list():
    global choose_items_combination, choose_weight_combination, choose_profit_combination

    items = np.array(ITEMS_SECTION)
    selected_items = genetic_algorithm(items, KNAPSACK_CAPACITY)

    choose_items_combination = [[]] * len(selected_items)
    choose_weight_combination = [[]] * len(selected_items)
    choose_profit_combination = [0] * len(selected_items)

    for i in range(0, len(selected_items)):

        temp_city_list = [0] * (DIMENSION - 1)
        temp_item_weight_list = [0] * (DIMENSION - 1)
        total_profit = 0
        for j in range(0, NUMBER_OF_ITEMS):

            if selected_items[i][j] == 1:
                city_index = ITEMS_SECTION[j][3]
                temp_city_list[city_index - 2] = 1

                item_weight = ITEMS_SECTION[j][2]
                item_profit = ITEMS_SECTION[j][1]
                total_profit += item_profit
                temp_item_weight_list[city_index - 2] += item_weight

        choose_items_combination[i] = temp_city_list
        choose_weight_combination[i] = temp_item_weight_list
        choose_profit_combination[i] = total_profit

file_path = './a280-n1395.txt'
initial_data(file_path)

print("DIMENSION:", DIMENSION)
print("NUMBER_OF_ITEMS:", NUMBER_OF_ITEMS)
print("KNAPSACK_CAPACITY:", KNAPSACK_CAPACITY)
print("MIN_SPEED:", MIN_SPEED)
print("MAX_SPEED:", MAX_SPEED)
print("RENTING_RATIO:", RENTING_RATIO)
print(CITY_MATRIX)
print(get_city_distance(1, 3))
print(ITEMS_SECTION)

get_items_list()
print("Combination of solutions for theft after EA：", choose_items_combination)
print("The backpack weight of each scheme in each city in the combination plan：", choose_weight_combination)
print("The profit of each option in the combination plan：", choose_profit_combination)


