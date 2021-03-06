#Caleb_1328518_Priyank_1297953

import random
import copy
from Rectangle import *

def takesize(elm):
    return(elm.height)

# gets the given index into the solution list, pops it out and re inserts it to a r
def FlipOne(current_solution_list, index):
    temp_solution_list = copy.deepcopy(current_solution_list)
    temp_solution_list[index].Rotate()
    temp_solution_list.sort(key=takesize)
    temp_solution_list.reverse()
    return temp_solution_list

# pops a rectangle forom the list at index, and re inserts it at a rondom posiotion
def MoveOne(current_solution_list, index):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    length = len(tmp_solution_list) - 1
    rand2 = random.randint(0,length)
    rect = tmp_solution_list.pop(index)
    tmp_solution_list.insert(rand2, rect)
    return tmp_solution_list

# Move but for ten rectangles rather than 1
def MoveTenPercent(current_solution_list, rand_list):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    length = len(rand_list)
    for i in range(length):
        tmp = tmp_solution_list.pop(rand_list[i])
        tmp_solution_list.insert(0, tmp)
    return tmp_solution_list

# Flip but for ten percent of the solution list rather than one rectangle
def FlipTenPercent(current_solution_list, rand_list):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    for i in range(len(rand_list)):
        tmp_solution_list[rand_list[i]].Rotate()
    tmp_solution_list.sort(key=takesize)
    tmp_solution_list.reverse()
    return tmp_solution_list

# helps to generate a list of random indexes to use flipTen or MoveTen on
def genertateRandomList(current_solution_list):
    length = len(current_solution_list)
    rand_list = []
    for i in range(int(length * 0.08)):
        rand_list.append(random.randint(0, length -1))
    return rand_list

# Used to generate full neighbourhoods for Best improvement or First Improvement.
def NeighborhoodGenerator(num_neighborhood, current_solution_list):
    neighborhood = []
    if num_neighborhood == 1:
        for rect in range(len(current_solution_list)):
            neighborhood.append(FlipOne(current_solution_list, rect))
    elif num_neighborhood == 3:
        for rec in range(int(len(current_solution_list) * 0.5)):
            neighborhood.append(MoveOne(current_solution_list, rec))
    elif num_neighborhood == 4:
        for rec in range(int(len(current_solution_list) * 0.1)):
            rand_list = genertateRandomList(current_solution_list)
            neighborhood.append(MoveTenPercent(current_solution_list, rand_list))
    elif num_neighborhood == 2:
        for rec in range(int(len(current_solution_list) * 0.2)):
            rand_list = genertateRandomList(current_solution_list)
            neighborhood.append(FlipTenPercent(current_solution_list, rand_list))
    return neighborhood
