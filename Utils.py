import os
import random
import re


from TravelingThiefProblem import TravelingThiefProblem as Problem



def readTxtFile(filename):
    problem = Problem()
    file_path = os.path.join("resources", filename + '.txt')
    with open(file_path, 'r') as file:
        for line in file:
            if 'PROBLEM NAME' in line:
                problem.name = filename
                # print(problem.name)
            elif 'KNAPSACK DATA TYPE' in line:
                pass
            elif 'DIMENSION' in line:
                problem.numOfCities = int(line.split(':')[1].strip())
                # print(problem.numOfCities)
            elif 'NUMBER OF ITEMS' in line:
                problem.numOfItem = int(line.split(':')[1].strip())
                # print(problem.numOfItem)
            elif 'CAPACITY OF KNAPSACK' in line:
                problem.maxWeight = int(line.split(':')[1].strip())
                # print(problem.maxWeight)
            elif 'MIN SPEED' in line:
                problem.minSpeed = float(line.split(':')[1].strip())
                # print(problem.minSpeed)
            elif 'MAX SPEED' in line:
                problem.maxSpeed = float(line.split(':')[1].strip())
                # print(problem.maxSpeed)
            elif 'RENTING RATIO' in line:
                problem.R = float(line.split(':')[1].strip())
                # print(problem.R)
            elif 'EDGE_WEIGHT_TYPE' in line:
                pass
            elif 'NODE_COORD_SECTION' in line:
                problem.coordinates = []
                for i in range(problem.numOfCities):
                    line = file.readline()
                    a = re.split(r'\s+', line.strip())
                    x_coord = int(a[1])
                    y_coord = int(a[2])
                    problem.coordinates.append((x_coord, y_coord))
                # print(problem.coordinates)
            elif 'ITEMS SECTION' in line:
                # problem.cityOfItem = []
                problem.weight = [[] for _ in range(problem.numOfCities)]
                problem.profit = [[] for _ in range(problem.numOfCities)]
                for i in range(int(problem.numOfItem / (problem.numOfCities - 1))):
                    for j in range(problem.numOfCities - 1):
                        line = file.readline()
                        a = re.split(r'\s+', line.strip())
                        profit = float(a[1])
                        weight = float(a[2])
                        city_index = int(a[3].strip()) - 1
                        problem.weight[city_index].append(weight)
                        problem.profit[city_index].append(profit)
                print(problem.profit)
                print(problem.weight)
                # for city_index, (weights, profits) in enumerate(zip(problem.weight, problem.profit), start=1):
                #     print(f"City {city_index} Items:")
                #     for item_index, (w, p) in enumerate(zip(weights, profits), start=1):
                #         print(f"  Item {item_index}: Profit={p}, Weight={w}")
    file.close()
    problem.getDistanceMatrix()
    problem.getItemMatrix()
    print(problem.distanceMatrix)
    return problem


def write_solutions(output_folder, team_name, problem_name, solutions):
    number_of_solutions = len(solutions)
    if number_of_solutions > 1:  # Replace 1 with the actual limit from Competition.numberOfSolutions
        print(f"WARNING: Finally the competition allows only 1 solution to be submitted. "
              f"Your algorithm found {number_of_solutions} solutions.")

    with open(os.path.join(output_folder, f"{team_name}_{problem_name}.x"), 'w') as var_bw, \
            open(os.path.join(output_folder, f"{team_name}_{problem_name}.f"), 'w') as obj_bw:

        for solution in solutions:
            # add one to the index of each city to match the index of the input format
            mod_tour = [city + 1 for city in solution.path]

            # write the variables
            var_bw.write(" ".join(map(str, mod_tour)) + "\n")
            var_bw.write(" ".join(map(lambda b: "1" if b else "0", solution.z)) + "\n\n")

            # write into the objective file
            obj_bw.write(f"{solution.time:.16f} {solution.profit:.16f}\n")


def print_solutions(solutions, print_variable):
    print(f"Number of non-dominated solutions: {len(solutions)}")

    for solution in solutions:
        if print_variable:
            print(" ".join(map(str, solution.path)), end=" , ")
            print(" ".join(map(lambda b: "1" if b else "0", solution.z)), end=" ")

        print(f"{solution.time:.2f} {solution.profit:.2f}")


Instances = [
    # a280_n279_bounded-strongly-corr_01.ttp
    # "a280-n279",
    # # a280_n1395_uncorr-similar-weights_05.ttp
    "a280-n1395",
    # # a280_n2790_uncorr_10.ttp
    # "a280-n2790",
    # # fnl4461_n4460_bounded-strongly-corr_01.ttp
    # "fnl4461-n4460",
    # # fnl4461_n22300_uncorr-similar-weights_05.ttp
    # "fnl4461-n22300",
    # # fnl4461_n44600_uncorr_10.ttp
    # "fnl4461-n44600",
    # # pla33810_n33809_bounded-strongly-corr_01.ttp
    # "pla33810-n33809",
    # # pla33810_n169045_uncorr-similar-weights_05.ttp
    # "pla33810-n169045",
    # # pla33810_n338090_uncorr_10.ttp
    # "pla33810-n338090"
]

if __name__ == '__main__':
    for instance in Instances:
        problem = readTxtFile(instance)
        # print(problem.distanceMatrix)
        # print(problem.getDistance(3, 2))
        # print(problem.getDistance(1, 280))
        # print(problem.itemMatrix)
        # print(len(problem.itemMatrix))
        path = random.sample(range(1, problem.numOfCities), problem.numOfCities - 1)
        # # Insert city 1 into the first position of the list
        path = [0] + path
        print(path)
        # # 需要修改
        # # z = [random.choice([0, 1]) for _ in range(problem.numOfCities)]
        z = random.choices([0, 1], weights=[0.8, 0.2], k=problem.numOfCities)
        solution = problem.fitnessFunction(path, z)
        print(solution.time, solution.profit)
        print(solution.objectives)
        print(solution.path)
        print(solution.z)
        print(solution.single_objective)
