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

def SwapOne(current_solution_list, index, indexx):
    rect1 = current_solution_list.pop(index)
    rect2 = current_solution_list.pop(indexx)
    current_solution_list.insert(indexx, rect1)
    if not current_solution_list[indexx].swapped:
        current_solution_list[indexx].swapped = True
    else:
        current_solution_list[indexx].swapped = False
    current_solution_list.insert(index, rect2)
    if not current_solution_list[index].swapped:
        current_solution_list[index].swapped = True
    else:
        current_solution_list[index].swapped = False
    return current_solution_list

def MoveOne(current_solution_list, index, indexx):
    rect = current_solution_list.pop(index)
    current_solution_list.insert(indexx, rect)
    if not current_solution_list[index].moved:
        current_solution_list[index].moved = True
    else:
        current_solution_list[index].moved = False
    return current_solution_list

def NeighborhoodGenerator(num_neighborhood, current_solution_list):
    neighborhood = []
    if num_neighborhood == 1:
        for rect in range(len(current_solution_list)):
            neighborhood.append(FlipOne(current_solution_list, rect))
    elif num_neighborhood == 2:
        for rec in range(len(current_solution_list) - 1):
            recc = 0
            neighborhood.append(MoveOne(current_solution_list, rec, recc))
    elif num_neighborhood == 3:
        for rec in range(len(current_solution_list) - 1):
            for recc in range(rec + 1, len(current_solution_list) - 1):
                neighborhood.append(SwapOne(current_solution_list, rec, recc))
    return neighborhood
