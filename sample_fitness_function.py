route = [3,2,1,4]
item_profits = [4,12,5,6,2,1]
item_weights = [6,9,1,3,1,2]
item_locations = [1,2,1,3,4,4]
packing_plan = [1,0,0,1,1,0]
bag_capacity = 20

def fitness_function(route,profits,weights,locations,plan,capacity):
    total_profit = 20
    total_time = 30
    return total_profit,total_time

fitness_function(route,item_profits,item_weights,item_locations,packing_plan,bag_capacity)
