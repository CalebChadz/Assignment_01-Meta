import csv
import sys
from array import *
from Rectangle import *
from graphics import *

# Global Variables
MAX_WIDTH = 400
CURR_HEIGHT = 0
solution_height = 400
solution_matrix = [ [0] * MAX_WIDTH for i in range(1)]

def initial_solution(rectangle_list):
        init_x = 0
        init_y = 0
        global CURR_HEIGHT
        global solution_matrix
        for rect in rectangle_list:
            # always recalculate the starting height
            init_y = 0
            #check to see if this row is full, if yes start from left.
            if (init_x + rect.width) > (MAX_WIDTH - 1):
                init_x = 0
            #move up to the first free height
            while(solution_matrix[init_y][init_x] != 0):
                init_y += 1
                if(CURR_HEIGHT < init_y):
                    solution_matrix[init_y] = [0] * MAX_WIDTH 
                    CURR_HEIGHT += 1
            #now check the right side of rectangle isnt colliding
            init_x = init_x + rect.width
            while(solution_matrix[init_y][init_x - 1] != 0):
                init_y += 1
                if(CURR_HEIGHT < init_y):
                    solution_matrix[init_y] = [0] * MAX_WIDTH 
                    CURR_HEIGHT += 1
            #now we have a free space to draw the rect
            rect.xpos = init_x - rect.width
            rect.ypos = init_y
            # fill in its matrix space
            print("Rectangle " + str(rect.id) + "\n Coordinates: (" + str(rect.xpos) + ", " + str(rect.ypos) + ")")
            print(solution_matrix)
            for x in range(rect.width):
                print("Checking at x position:  " + str(x))
                for y in range(rect.height):
                    print("checking at y position: " + str(y))
                    if (rect.ypos + y) > CURR_HEIGHT:
                        CURR_HEIGHT += 1
                        solution_matrix.append([0] * MAX_WIDTH) 
                        print(solution_matrix)
                    solution_matrix[rect.ypos + y][rect.xpos + x] = rect.id
        return

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
        
    CURR_HEIGHT = initial_solution(rectangles)
    print(solution_matrix)
    # Draw out the final solution
    draw_solution(rectangles, solution_height)  
main()