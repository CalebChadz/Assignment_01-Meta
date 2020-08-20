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
#MAX_NEIGHBORHOOD = 3
MAX_TIME = 0
given_solution_width = 0
current_neighbourhood = 1
initial_solution = None

def takesize(elm):
    return(elm.width * elm.height)

# Main method
#def main():
def test(variant, MAX_NEIGHBORHOOD):
    global best_solution_list
    file_name = ''
    # Get the command line arguments, grab the csv File to read in Rectangles.
    if len(sys.argv) == 4:
        file_name = sys.argv[1]
        given_solution_width = int(sys.argv[2])
        scale = int(sys.argv[3])
        #variant = sys.argv[4]
    # Parse in the csv to rectangle objects
    best_solution_list = GetRectangles(file_name)
    best_solution_list.sort(key=takesize)
    best_solution_list.reverse()
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    initial_solution = Solution(best_solution_list, given_solution_width, True)
    print ("Initial Solution Height: " + str(initial_solution.height))
    #initial_solution.drawSolution(scale)
    
    # BVNS tim
    start = time.time()
    if variant == "B":
        searched_solution = BVNS(initial_solution, MAX_NEIGHBORHOOD, MAX_TIME)
    if variant == "V":
        searched_solution = VNDS(initial_solution, MAX_NEIGHBORHOOD, MAX_TIME)
    if variant == "R":
        searched_solution = RVNS(initial_solution, MAX_NEIGHBORHOOD, 60)
    if variant == "G":
        searched_solution = GVNS(initial_solution, MAX_NEIGHBORHOOD, MAX_TIME)
    print("Final found solution height: " + str(searched_solution.height) + " Found in time: " + str(time.time() - start))
    #searched_solution.drawSolution(scale)
    return (str(searched_solution.height) + " " + str(time.time() - start))
#main()
