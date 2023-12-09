import random

import numpy as np
from NonDominatedSet import NonDominatedSet


class AntColonyOptimization:

    def __init__(self, problem, num_ants=10, alpha=1.0, beta=2.0, evaporation_rate=0.5, max_iterations=10):
        self.problem = problem
        self.num_ants = num_ants
        self.alpha = alpha
        self.beta = beta
        self.evaporation_rate = evaporation_rate
        self.max_iterations = max_iterations
        self.pheromone_matrix = self.initialize_pheromones()

    def initialize_pheromones(self):
        return np.ones((self.problem.numOfCities, self.problem.numOfCities))

    def generate_Heuristic_Matrix(self):
        heuristicMatrix = np.zeros((self.problem.numOfCities, self.problem.numOfCities))
        for i in range(self.problem.numOfCities):
            for j in range(self.problem.numOfCities):
                if i != j:
                    if self.problem.distanceMatrix[i][j] != 0:
                        heuristicMatrix[i][j] = round(1 / self.problem.distanceMatrix[i][j], 4)
                else:
                    heuristicMatrix[i][j] = 0

        # for i in range(self.problem.numOfCities):
        #     for j in range(self.problem.numOfCities):
        #         if j != 0:
        #             if self.problem.distanceMatrix[i][j] != 0:
        #                 heuristicMatrix[i][j] = round(heuristicMatrix[i][j] * (self.problem.itemMatrix[j][1]/self.problem.itemMatrix[j][0]), 4)
        #         else:
        #             heuristicMatrix[i][j] = 0

        return heuristicMatrix

    def update_flags(self, z):
        total_weight = 0
        for i in range(len(z)):
            if z[i]:
                total_weight += self.problem.itemMatrix[i][0]
        while total_weight > self.problem.maxWeight:
            index = random.randint(0, self.problem.numOfCities - 1)
            if z[index]:
                total_weight -= self.problem.itemMatrix[index][0]
                z[index] = 0
        return z

    def solve(self):
        nds = NonDominatedSet()
        print(self.problem.itemMatrix)
        heu_matrix = self.generate_Heuristic_Matrix()
        for iteration in range(self.max_iterations):
            ant_tours = []
            for ant in range(self.num_ants):
                tour = []
                current_city = 0
                for _ in range(self.problem.numOfCities):
                    tour.append(current_city)
                    numerators = []
                    probabilities = []
                    sum_numerator = 0
                    sum_cumulative_pro = 0
                    cumulative_pros = []
                    for city in range(self.problem.numOfCities):
                        if city not in tour:
                            pheromone_factor = self.pheromone_matrix[current_city, city] ** self.alpha
                            heuristic_factor = heu_matrix[current_city, city] ** self.beta
                            numerator = pheromone_factor * heuristic_factor
                            numerators.append((city, numerator))
                            sum_numerator += numerator
                    for i in numerators:
                        if sum_numerator != 0:
                            probability = i[1] / sum_numerator
                            probabilities.append((i[0], probability))
                    for i in probabilities:
                        sum_cumulative_pro += i[1]
                        cumulative_pros.append((i[0], sum_cumulative_pro))
                    random_value = random.uniform(0, 1)
                    for i in cumulative_pros:
                        if i[1] > random_value:
                            current_city = i[0]
                            break
                ant_tours.append(tour)
            for i in range(self.problem.numOfCities):
                for j in range(self.problem.numOfCities):
                    self.pheromone_matrix[i][j] *= 1 - self.evaporation_rate

            for path in ant_tours:
                flag = random.choices([0, 1], weights=[0.3, 0.7], k=self.problem.numOfCities)
                # flag = [random.choice([0, 1]) for _ in range(self.problem.numOfCities)]
                z = self.update_flags(flag)
                solution = self.problem.fitnessFunction(path, z)
                delta = (1 / solution.time) * solution.profit
                for i in path:
                    self.pheromone_matrix[i - 1][i] += delta
                print(solution.path)
                print(solution.objectives)
                nds.add(solution)
                # for _ in range(100):
                #     flag = random.choices([0, 1], weights=[0.2, 0.8], k=self.problem.numOfCities)
                #     # flag = [random.choice([0, 1]) for _ in range(self.problem.numOfCities)]
                #     z = self.update_flags(flag)
                #     solution = self.problem.fitnessFunction(path, z)
                #     print(solution.objectives)
                #     nds.add(solution)

        return nds.entries
