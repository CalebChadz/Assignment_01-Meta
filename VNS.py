import csv
import sys
from Rectangle import *
from graphics import *

# Global Variables
solution_height = 400

# Main method
def main():
    file_name = ''
    # Get the command line arguments, grap the csv File to read in Rectangles.
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        print(file_name)
    # Parse in the csv to rectangle objects
    rectangles = {}
    rectangles = get_rectangles(file_name)
    for rect in rectangles:
        rect.print()

    # Generate initial solution, represented as a list of boxes and thier coordinates.

    # Draw out the final solution
    draw_solution(rectangles, solution_height)  
main()