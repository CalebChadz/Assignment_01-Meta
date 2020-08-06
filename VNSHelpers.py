from NeighbourhoodFunctions import *
from Rectangle import *
import random

# funciton that decodes the list representation of boxes to a matrix representation and gives
# the rectangles coordinates on a plane.
def CalculateSolutionMatrix(rectangle_list, given_width, initial):
    solution_matrix = [ [0] * given_width ]
    init_x = 0
    init_y = 0
    for rect in rectangle_list:
        if rect.width < rect.height and initial:
            rect.Rotate()
        # check the bottom of rectangle is not colliding with any other rectangle for all side length
        ypos = 0
        while (ypos < rect.height):
            if(len(solution_matrix) <= init_y + ypos):
                        solution_matrix.append([0] * given_width)
            xpos = 0
            while (xpos < rect.width):
                if (solution_matrix[init_y + ypos][init_x + xpos] != 0):
                    init_x += 1
                    xpos = 0
                    ypos = 0
                else:
                    xpos += 1
                    
                if((init_x + rect.width) > (given_width)):
                    init_x = 0
                    init_y += 1 
                    xpos = 0
                    ypos = 0
                    if(len(solution_matrix) - 1 < init_y + ypos):
                        solution_matrix.append([0] * given_width)
            ypos += 1
        #now we have a free space to draw the rect
        rect.xpos = init_x 
        rect.ypos = init_y
        # fill in its matrix space
        for x in range(rect.width):
            for y in range(rect.height):
                solution_matrix[rect.ypos + y][rect.xpos + x] = rect.id
        init_x = 0
        init_y = 0
    # length of matrics directly corresponds to the solution height
    return solution_matrix

# function to see if it is time to change neighborhoods based on given solutions.
def NeighborhoodChange(current_best_list, current_best_matrix, new_list, new_matrix, curr_neighborhood):
    if (len(new_matrix) < len(current_best_matrix)):
        curr_neighborhood = 1
        return new_list, new_matrix, curr_neighborhood
    else:
        curr_neighborhood += 1 
        return current_best_list, current_best_matrix, curr_neighborhood

#functions to be implemented:

# Shake, this will be the implementation of our neighborhood function to pull out a solution
# Shake(x,k) where x is current solition, k is current neighborhood. So based on current neighborhood and its
# neighborhood funciton, shake the solutiuon to a new solution.
def Shake(current_solution_list, current_neighbourhood):
    if current_neighbourhood == 1:
        rand = random.randint(0, len(current_solution_list) - 1)
        current_solution_list = FlipOne(current_solution_list, rand)
    elif current_neighbourhood == 2:
        rand = random.randint(0, len(current_solution_list) - 1)
        randd = random.randint(0, len(current_solution_list) - 1)
        current_neighbourhood = MoveOne(current_solution_list, rand, randd)
    return current_solution_list

# BestImprovement, This will take the newly shaken solution and run Best improvement on all adjacent
# neighbors. In essence run a local search. Apply the current neighborhood function once again but this time
# on the new solution not on the current best solution, repeat for all neighbors and pick out the best
def BestImprovement(new_solution_list, new_solution_matrix, current_neighbourhood, given_width):
    
    current_solution_list = new_solution_list
    current_solution_matrix = new_solution_matrix
    found_new = True

    while found_new:
        found_new = False
        neighbors = NeighborhoodGenerator(current_neighbourhood, current_solution_list)
        for neighbor_list in neighbors:
            neighbor_matrix = CalculateSolutionMatrix(neighbor_list, given_width, False)
            if len(neighbor_matrix) < len(current_solution_matrix):
                current_solution_matrix = neighbor_matrix
                current_solution_list = neighbor_list
                found_new = True
    return current_solution_list, current_solution_matrix

# BVNS framework
# Basic Variable Neighborhood Search strucure.
def BVNS(curr_solution, curr_matrix, max_neighborhood, max_time, given_width):
    curr_solution_list = curr_solution
    curr_solution_matrix = curr_matrix
    # get starting time
    start = time.time()
    curr_neighborhood = 1
    # begin algorithm execution, while there is time left.
    while ((time.time() - start) < max_time):
        curr_neighborhood = 1
        while(curr_neighborhood != max_neighborhood):
            # Shake the solution
            new_solution_list = Shake(curr_solution_list, curr_neighborhood)
            new_solution_matrix = CalculateSolutionMatrix(new_solution_list, given_width, False)
            new_solution_height = len(new_solution_matrix)
            #print("Shaken solution height: " + str(new_solution_height))
            #DrawSolution(new_solution_list, given_width, new_solution_height)
            
            # Best improvement the solution, local search
            newer_solution_list, newer_solution_matrix = BestImprovement(new_solution_list, new_solution_matrix, curr_neighborhood, given_width)
            newer_solution_height = len(newer_solution_matrix)
            #print("Best Improvement solution height: " + str(newer_solution_height))
            #DrawSolution(new_solution_list, given_width, new_solution_height)
            
            # Change Neighborhoods.
            curr_solution_list, curr_solution_matrix, curr_neighborhood = NeighborhoodChange(curr_solution_list, curr_solution_matrix, newer_solution_list, newer_solution_matrix, curr_neighborhood)
            print("Current Best solution height: " + str(len(curr_solution_matrix)))
    
    return curr_solution_list, curr_solution_matrix
