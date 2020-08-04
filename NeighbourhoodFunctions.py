import random
from Rectangle import *

def FlipHalf(rectangle_list):
    for rectangle in rectangle_list:
        isFlipped = random.choice([True, False])
        if isFlipped:
            rectangle.Rotate()
    return rectangle_list

def FlipOne(current_solution_list, index):
    current_solution_list[index].Rotate()
    return current_solution_list

def MoveOne(current_solution_list, index):
    random_index = random.randint(0, len(current_solution_list) - 1)
    rect = current_solution_list.pop(index)
    current_solution_list.insert(random_index, rect)
    return current_solution_list

def NeighborhoodGenerator(num_neighborhood, current_solution_list):
    neighborhood = []
    if num_neighborhood == 2:
        for rect in range(len(current_solution_list)):
            neighborhood.append(FlipOne(current_solution_list, rect))
    elif num_neighborhood == 1:
        for rec in range(len(current_solution_list)):
            neighborhood.append(MoveOne(current_solution_list, rec))
    return neighborhood
