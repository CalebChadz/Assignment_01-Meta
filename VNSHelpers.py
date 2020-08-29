#Caleb_1328518_Priyank_1297953

from NeighbourhoodFunctions import *
from Rectangle import *
import random
import copy
      
# function to see if it is time to change neighborhoods based on given solutions.
def NeighborhoodChange(current_best_solution, newer_solution, curr_neighborhood):
    if newer_solution.height < current_best_solution.height:
        curr_neighborhood = 1
        return newer_solution, curr_neighborhood
    elif newer_solution.height == current_best_solution.height:
        curr_neighborhood += 1
        return newer_solution, curr_neighborhood
    else:
        curr_neighborhood += 1 
        return current_best_solution, curr_neighborhood

#functions to be implemented:

# Shake, this will be the implementation of our neighborhood function to pull out a solution
# Shake(x,k) where x is current solition, k is current neighborhood. So based on current neighborhood and its
# neighborhood funciton, shake the solutiuon to a new solution.
def Shake(current_solution_list, current_neighbourhood):
    tmp_solution_list = copy.deepcopy(current_solution_list)
    if current_neighbourhood == 1:
        rand = random.randint(0, len(tmp_solution_list) - 1)
        tmp_solution_list = FlipOne(tmp_solution_list, rand)
        #print("Shake Function FlipOne")
    elif current_neighbourhood == 3:
        tmp_solution_list = MoveOne(tmp_solution_list, random.randint(0,len(tmp_solution_list) -1))
        #print("Shake Function MoveOne")
    elif current_neighbourhood == 4:
        rand_list = []
        length = len(tmp_solution_list)
        for i in range(int(length * 0.1)):
            rand_list.append(random.randint(0, length -1))
        tmp_solution_list = MoveTenPercent(tmp_solution_list, rand_list)
        #print("Shake Function MoveTenPercent")
    elif current_neighbourhood == 2:
        rand_list = []
        length = len(tmp_solution_list)
        for i in range(int(length * 0.1)):
            rand_list.append(random.randint(0, length -1))
        tmp_solution_list = FlipTenPercent(tmp_solution_list, rand_list) 
        #print("Shake Function FlipTenPercent")
    return tmp_solution_list

# BestImprovement, This will take the newly shaken solution and run Best improvement on all adjacent
# neighbors. In essence run a local search. Apply the current neighborhood function once again but this time
# on the new solution not on the current best solution, repeat for all neighbors and pick out the best
def BestImprovement(new_solution, current_neighbourhood):
    current_solution = copy.deepcopy(new_solution)
    found_new = True

    while found_new:
        found_new = False
        neighbors = NeighborhoodGenerator(current_neighbourhood, current_solution.rectangle_list)
        for neighbor_list in neighbors:
            neighbor_solution = Solution(neighbor_list, new_solution.given_width, False)
            if neighbor_solution.height < current_solution.height:
                current_solution = neighbor_solution
                found_new = True
    return current_solution

# FirstImprovement, This will take the newly shaken solution and run First improvement on all adjacent
# neighbors. In essence run a local search. Apply the current neighborhood function once again but this time
# on the new solution not on the current best solution, repeat for all neighbors and pick out the first solution
# that makes an improvement.
def FirstImprovement(new_solution, current_neighbourhood):
    current_solution = copy.deepcopy(new_solution)
    found_new = True

    while found_new:
        found_new = False
        neighbors = NeighborhoodGenerator(current_neighbourhood, current_solution.rectangle_list)
        for neighbor_list in neighbors:
            neighbor_solution = Solution(neighbor_list, new_solution.given_width, False)
            if neighbor_solution.height < current_solution.height:
                current_solution = neighbor_solution
                found_new = True
                return current_solution
        return current_solution

def VND(solution, max_neighborhood):
    curr_solution = copy.deepcopy(solution)
    curr_neighborhood = 1
    while curr_neighborhood <= max_neighborhood:
        neighbors = NeighborhoodGenerator(curr_neighborhood, curr_solution.rectangle_list)
        best_neighbor = Solution(neighbors[0], solution.given_width, False)
        for neighbor_list in neighbors:
            neighbor_solution = Solution(neighbor_list, solution.given_width, False)
            if neighbor_solution.height <= best_neighbor.height:
                best_neighbor = neighbor_solution
        curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, best_neighbor, curr_neighborhood)
        print("Current Best VND session height: " + str(curr_solution.drawHeight) + " Value Metric: " + str(curr_solution.height))
        if curr_solution.height == 0:
            return curr_solution
    return curr_solution

#RVNS framework
#Reduced Variable Neighborhood Search Structure
def RVNS(solution, max_neighborhood, max_time):
    curr_solution = copy.deepcopy(solution)
    # get starting time
    start = time.time()
    # begin algorithm execution, while there is time left.
    while ((time.time() - start) < max_time):
        curr_neighborhood = 1
        while(curr_neighborhood <= max_neighborhood):
        # Shake the solution
            new_solution_list = Shake(curr_solution.rectangle_list, curr_neighborhood)
            new_solution = Solution(new_solution_list, solution.given_width, False)
            new_solution_height = new_solution.drawHeight
            print("Shaken solution height: " + str(new_solution_height))
        
            # Change Neighborhoods.
            curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, new_solution, curr_neighborhood)
            print("Current Best solution height: " + str(curr_solution.drawHeight) + " Value Metric: " + str(curr_solution.height))
            if curr_solution.height == 0:
                return curr_solution
    return curr_solution

# BVNS framework
# Basic Variable Neighborhood Search strucure.
def BVNS(solution, max_neighborhood, max_time):
    curr_solution = copy.deepcopy(solution)
    currBestHeight = solution.drawHeight
    timey = None
    # get starting time
    start = 100
    # begin algorithm execution, while there is time left.
    while (start > 0):
        start -= 1
        curr_neighborhood = 1
        while(curr_neighborhood <= max_neighborhood):
            # Shake the solution
            new_solution_list = Shake(curr_solution.rectangle_list, curr_neighborhood)
            new_solution = Solution(new_solution_list, solution.given_width, False)
            new_solution_height = new_solution.drawHeight
            #print("Shaken solution height: " + str(new_solution_height))
            # new_solution.drawSolution(10)

            # Best improvement the solution, local search
            newer_solution = BestImprovement(new_solution, curr_neighborhood)
            newer_solution_height = newer_solution.drawHeight
            #print("Best Improvement solution height: " + str(newer_solution_height))
            # newer_solution.drawSolution(10)

            # Change Neighborhoods.
            curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, newer_solution, curr_neighborhood)
            print(str(start) + " Current Best solution height: " + str(curr_solution.drawHeight) + " Value Metric: " + str(curr_solution.height))
            if curr_solution.height == 0:
                return curr_solution
        
    return curr_solution

def GVNS(solution, max_neighborhood, max_time):
    curr_solution = copy.deepcopy(solution)
    # get starting time
    start = time.time()
    # begin algorithm execution, while there is time left.
    while ((time.time() - start) < max_time):
        curr_neighborhood = 1
        while(curr_neighborhood <= max_neighborhood):
            # Shake the solution
            new_solution_list = Shake(curr_solution.rectangle_list, curr_neighborhood)
            new_solution = Solution(new_solution_list, solution.given_width, False)
            new_solution_height = new_solution.drawHeight
            print("Shaken solution height: " + str(new_solution_height))
            # new_solution.drawSolution(10)

            # Best improvement the solution, local search
            newer_solution = VND(new_solution, max_neighborhood)
            newer_solution_height = newer_solution.drawHeight
            print("VND solution height: " + str(newer_solution_height))
            # newer_solution.drawSolution(10)

            # Change Neighborhoods.
            curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, newer_solution, curr_neighborhood)
            print("Current Best solution height: " + str(curr_solution.drawHeight) + " Value Metric: " + str(curr_solution.height))
            if curr_solution.height == 0:
                return curr_solution
    return curr_solution