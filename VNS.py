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
scale = 2
MAX_NEIGHBORHOOD = 4
MAX_TIME = 120
given_solution_width = 0
current_neighbourhood = 1
initial_solution = None

def takesize(elm):
    return(elm.width * elm.height)

# Main method
def main():
    global best_solution_list
    file_name = ''
    # Get the command line arguments, grab the csv File to read in Rectangles.
    if len(sys.argv) == 4:
        file_name = sys.argv[1]
        given_solution_width = int(sys.argv[2])
        scale = int(sys.argv[3])
    # Parse in the csv to rectangle objects
    best_solution_list = GetRectangles(file_name)
    best_solution_list.sort(key=takesize)
    best_solution_list.reverse()
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    initial_solution = Solution(best_solution_list, given_solution_width, True)
    print ("Initial Solution Height: " + str(initial_solution.height))
    initial_solution.drawSolution(scale)
    
    # BVNS time
    searched_solution = BVNS(initial_solution, MAX_NEIGHBORHOOD, MAX_TIME)
    print("Final found solution height: " + str(searched_solution.height))
    searched_solution.drawSolution(scale)
main()