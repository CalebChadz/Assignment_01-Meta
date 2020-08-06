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
    if not current_solution_list[index].rotated:
        current_solution_list[index].rotated = True
    else:
        current_solution_list[index].rotated = False
    return current_solution_list

def MoveOne(current_solution_list, index, indexx):
    rect = current_solution_list.pop(index)
    current_solution_list.insert(indexx, rect)
    return current_solution_list

def NeighborhoodGenerator(num_neighborhood, current_solution_list):
    neighborhood = []
    if num_neighborhood == 1:
        for rect in range(len(current_solution_list)):
            neighborhood.append(FlipOne(current_solution_list, rect))
    elif num_neighborhood == 2:
        for rec in range(len(current_solution_list)):
            recc = 0
            neighborhood.append(MoveOne(current_solution_list, rec, recc))
    return neighborhood
