import csv
import sys
import pathlib
import time
from array import *
from Rectangle import *
from VNSHelpers import *
from graphics import *

# Global Variables
scale = 4
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
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    solution_height, solution_matrix = GetSolution(solution_rectangles, solution_width)
    print("initial solution height: " + str(solution_height / scale))
    #begin basic neighbourhood search

    # Draw out the final solution
    DrawSolution(solution_rectangles, solution_width, solution_height)  
    # print(solution_matrix)
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
            # Shake the solution
            new_solution = Shake(curr_solution, curr_neighborhood)
            # Best improvement the solution, local search
            newer_solution = BestImprovement(new_solution) 
            # Change Neighborhoods.
            curr_solution, curr_neighborhood = NeighborhoodChange(curr_solution, newer_solution, curr_neighborhood)
    return curr_solution
