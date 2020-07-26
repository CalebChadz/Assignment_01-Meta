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
    win = GraphWin("Solution Window", 400, solution_height)
    # set background to black
    win.setBackground(color_rgb(150,200,210))
    # For each rectangle in the list
    for r in rectangles:
        #get the position of this rectangle and create a drawable.
        pt1 = Point(r.xpos, r.ypos)
        pt2 = Point((r.xpos + r.width), (r.ypos + r.height))
        rect_draw  = Rectangle(pt1, pt2)
        # set the outline color
        rect_draw.setFill(color_rgb(199,0,57))
        # draw it to the window
        rect_draw.draw(win)
    # wait for a click then close the program
    win.getMouse()
    win.close()
main()


