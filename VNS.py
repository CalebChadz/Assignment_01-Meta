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
MAX_NEIGHBORHOOD = 3
given_solution_width = 0
best_solution_matrix = [ [0] * given_solution_width ]
best_solution_list = {}
current_neighbourhood = 1

def takesize(elm):
    return(elm.width * elm.height)

# Main method
def main():
    global best_solution_matrix
    global best_solution_list
    file_name = ''
    # Get the command line arguments, grab the csv File to read in Rectangles.
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        given_solution_width = int(sys.argv[2])
    # Parse in the csv to rectangle objects
    best_solution_list = GetRectangles(file_name)
    best_solution_list.sort(key=takesize)
    best_solution_list.reverse()
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    best_solution_matrix = CalculateSolutionMatrix(best_solution_list, given_solution_width, True)
    solution_height = len(best_solution_matrix)
    print("Initial solution height: " + str(solution_height))

    # Draw out the final solution
    DrawSolution(best_solution_list, given_solution_width, solution_height, scale)  
    best_solution_list, best_solution_matrix = BVNS(best_solution_list, best_solution_matrix, MAX_NEIGHBORHOOD, 60, given_solution_width)
    
    solution_height = len(best_solution_matrix)
    print("BVNS solution height: " + str(solution_height))
    DrawSolution(best_solution_list, given_solution_width, solution_height, scale)

main()