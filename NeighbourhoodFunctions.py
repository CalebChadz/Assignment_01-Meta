import random
import copy
from Rectangle import *

def FlipOne(current_solution_list, index):
    temp_solution_list = copy.deepcopy(current_solution_list)
    temp_solution_list[index].Rotate()
    return temp_solution_list

def MoveOne(current_solution_list):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    rand1 = random.randint(0,len(tmp_solution_list) - 1)
    rand2 = random.randint(0,len(tmp_solution_list) - 1)
    rect = tmp_solution_list.pop(rand1)
    tmp_solution_list.insert(rand2, rect)
    return tmp_solution_list

def MoveTenPercent(current_solution_list, rand_list):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    length = len(rand_list)
    for i in range(length):
        tmp = tmp_solution_list.pop(rand_list[i])
        tmp_solution_list.insert(0, tmp)
    return tmp_solution_list

def FlipTenPercent(current_solution_list, rand_list):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    for i in range(len(rand_list)):
        tmp_solution_list[rand_list[i]].Rotate()
    return tmp_solution_list
    
def genertateRandomList(current_solution_list):
    length = len(current_solution_list)
    rand_list = []
    for i in range(int(length * 0.2)):
        rand_list.append(random.randint(0, length -1))
    return rand_list


def NeighborhoodGenerator(num_neighborhood, current_solution_list):
    neighborhood = []
    if num_neighborhood == 4:
        for rect in range(len(current_solution_list)):
            neighborhood.append(FlipOne(current_solution_list, rect))
    elif num_neighborhood == 3:
        for rec in range(int(len(current_solution_list) * 0.5)):
            neighborhood.append(MoveOne(current_solution_list))
    elif num_neighborhood == 2:
            for rec in range(ilen(current_solution_list) * 0.1)):
                rand_list = genertateRandomList(current_nt(solution_list)
                neighborhood.append(MoveTenPercent(current_solution_list, rand_list))
    elif num_neighborhood == 1:
            for rec in range(int(len(current_solution_list) * 0.1)):
                rand_list = genertateRandomList(current_solution_list)
                neighborhood.append(FlipTenPercent(current_solution_list, rand_list))
    return neighborhood
