from aco import cities_stolen, ant_colony_optimization
from initialize_data import parse_knapsack_data
from local_search import local_search


def main():
    problem_name,knapsack_data_type,dimension,num_items, \
    capacity_of_knapsack,min_speed,max_speed,renting_ratio,\
    edge_weight_type,distances,profits,weights,assigned_node_numbers = parse_knapsack_data("./resources/a280-n279.txt")
    sample_knapsack = local_search(profits,weights,capacity_of_knapsack,n=10000,discretion=0.1, initial_solution_type='intuitive')
    stolen = cities_stolen(sample_knapsack,assigned_node_numbers)
    print(ant_colony_optimization(distances,cities_stolen=stolen,weights=weights, problem_details=[capacity_of_knapsack,max_speed,min_speed]))



if __name__ == "__main__":
    main()