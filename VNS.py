import csv
import sys
import pathlib
from array import *
from Rectangle import *
from graphics import *
from GetSolution import *

# Global Variables
scale = 2
solution_width = 400 * scale
solution_matrix = [ [0] * solution_width ]
solution_rectangles = {}

# Main method
def main():
    global solution_matrix
    global solution_rectangles
    file_name = ''
    # Get the command line arguments, grap the csv File to read in Rectangles.
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    # Parse in the csv to rectangle objects
    solution_rectangles = get_rectangles(file_name)
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    solution_height, solution_matrix = get_solution(solution_rectangles, solution_width)
    print("initial solution height: " + str(solution_height / scale))
    #begin basic neighbourhood search

    # Draw out the final solution
    draw_solution(solution_rectangles, solution_width, solution_height)  
    # print(solution_matrix)


main()