import csv
import sys
import pathlib
from array import *
from Rectangle import *
from graphics import *

# Global Variables
MAX_WIDTH = 400
solution_width = 400
solution_matrix = [ [0] * MAX_WIDTH for i in range(1)]

def initial_solution(rectangle_list):
        init_x = 0
        init_y = 0
        global solution_matrix
        for rect in rectangle_list:
            # always recalculate the starting height
            init_y = 0
            #check to see if this row is full, if yes start from left.
            if (init_x + rect.width) > (MAX_WIDTH-1):
                init_x = 0
            # check the bottom of rectangle is not colliding with any other rectangle for all side length
            ypos = 0
            while (ypos < rect.height):
                if(len(solution_matrix) - 1 < init_y + ypos):
                            solution_matrix.append([0] * MAX_WIDTH)
                xpos = 0
                while (xpos < rect.width):
                    if (solution_matrix[init_y + ypos][init_x + xpos] != 0):
                        init_y += 1
                        xpos = 0
                        ypos = 0
                        if(len(solution_matrix) - 1 < init_y):
                            solution_matrix.append([0] * MAX_WIDTH) 
                    else:
                        xpos += 1
                ypos += 1
            #now we have a free space to draw the rect
            rect.xpos = init_x 
            rect.ypos = init_y
            # fill in its matrix space
            for x in range(rect.width):
                for y in range(rect.height):
                    solution_matrix[rect.ypos + y][rect.xpos + x] = rect.id
            init_x += rect.width
        return len(solution_matrix) - 1

# Main method
def main():
    file_name = ''
    # Get the command line arguments, grap the csv File to read in Rectangles.
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
    # Parse in the csv to rectangle objects
    rectangles = {}
    rectangles = get_rectangles(file_name)
    # Generate initial solution, represented as a list of boxes and thier coordinates.
    solution_height = initial_solution(rectangles)
    print("solution height: " + str(solution_height))
    # Draw out the final solution
    draw_solution(rectangles, solution_width, solution_height)  
    # print(solution_matrix)
main()