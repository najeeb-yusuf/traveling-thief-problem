class Solution:
    def __init__(self, route, profits, weights, locations, plan, capacity):
        self.route = route
        self.profits = profits
        self.weights = weights
        self.locations = locations
        self.packing_plan = plan
        self.capacity = capacity
        self.profit, self.time = self.calculate_fitness()

    def calculate_fitness(self):
        selected_items = [(self.profits[i], self.locations[i], self.weights[i]) for i in self.route if self.capacity >= self.weights[i] and self.packing_plan[i] == 1]
        total_profit = sum(item[0] for item in selected_items)
        total_time = sum(item[1] for item in selected_items)
        return total_profit, total_time

def dominates(solution1, solution2):
    """Check if solution1 dominates solution2."""
    return solution1.profit >= solution2.profit and solution1.time <= solution2.time

def update_best_non_dominating(current_best, new_solution):
    """Update the list of optimal non-dominated solutions."""
    updated_best = current_best.copy()

    is_dominated = False
    to_remove_indices = []

    for i, solution in enumerate(current_best):
        if dominates(new_solution, solution):
            to_remove_indices.append(i)
        elif dominates(solution, new_solution):
            is_dominated = True
            break

    if not is_dominated:
        # Replace the worst solution with a new one
        for index in to_remove_indices:
            updated_best[index] = new_solution

    return updated_best
  
    def identify_pareto_front(solutions):
    pareto_front = []

    for i, solution in enumerate(solutions):
        dominated = False
        for other_solution in solutions[:i] + solutions[i+1:]:
            if is_dominating(other_solution, solution):
                dominated = True
                break
        if not dominated:
            pareto_front.append(solution)

    return pareto_front
