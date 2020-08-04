import csv
import sys
import pathlib
import time
from array import *
from Rectangle import *
from VNSHelpers import *
from NeighbourhoodFunctions import *
from graphics import *

# Global Variables
scale = 1
solution_width = 0
solution_matrix = [ [0] * solution_width ]
solution_rectangles = {}

# Main method
def main():
    global solution_matrix
    global solution_rectangles
    file_name = ''
    # Get the command line arguments, grap the csv File to read in Rectangles.
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        solution_width = int(sys.argv[2]) * scale
    # Parse in the csv to rectangle objects
    solution_rectangles = GetRectangles(file_name, scale)
    solution = Solution(solution_width)
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    solution_matrix = solution.GetSolution(solution_rectangles)
    solution_height = Solution.getHeight(solution_matrix)
    print("Initial solution height: " + str(solution_height / scale))
    #begin basic neighbourhood search

    # Draw out the final solution
    #DrawSolution(solution_rectangles, solution_width, solution_height)  
    # print(solution_matrix)

    new_solution = Shake(solution_rectangles, Neighbourhood(1))
    solution_matrix = solution.GetSolution(new_solution)
    solution_height = Solution.getHeight(solution_matrix)
    print("Shake solution height: " + str(solution_height / scale))
    #DrawSolution(new_solution, solution_width, solution_height)
    newer_solution = BestImprovement(new_solution, Neighbourhood(1), solution) 
    solution_matrix = solution.GetSolution(newer_solution)
    solution_height = Solution.getHeight(solution_matrix)
    print("Best improvement solution height: " + str(solution_height))
    DrawSolution(newer_solution, solution_width, solution_height)
    

main()

# Basic Variable Neighborhood Search strucure.
def BVNS(curr_solution, max_neighborhood, max_time):
    # get starting time
    start = time.time()
    curr_neighborhood = 1
    # begin algorithm execution, while there is time left.
    while ((time.time() - start) < max_time):
        curr_neighborhood = 1
        while(curr_neighborhood != max_neighborhood):
            neighbourhood = Neighbourhood(curr_neighbourhood)
            # Shake the solution
            new_solution = Shake(curr_solution, neighbourhood)
            # Best improvement the solution, local search
            newer_solution = BestImprovement(new_solution, neighbourhood) 
            # Change Neighborhoods.
            curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, newer_solution, curr_neighborhood)
    return curr_solution
