import csv
from graphics import *

# A rectangle object to represent the rectangles in out problem.
class Rect:
    def __init__(self, id, width, height, xpos, ypos):
        self.id = id
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
# Quickly print off this rectangles current values.
    def print(self):
        print("ID: " + str(self.id) + "\nDimensions: (" + str(self.width) + ", " + str(self.height) + ")" + "\nCoordinates: (" + str(self.xpos) + ", " + str(self.ypos) + ")")

# Function to read in a CSV file of rectangle dimensions to be stored as rectangle objects.
def get_rectangles(file_name):
    rectangles = []
    with open(file_name, 'r', encoding='utf-8-sig') as csv_file:
        reader = csv.reader(csv_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # add the new rectangle, make sure correct types eg integer.
                rectangles.append(Rect(int(row[0]), int(row[1]), int(row[2]), 0,0))
    return rectangles

#function to draw out the final solution to a window to be viewed.
def draw_solution(solution, solution_width, solution_height):
    win = GraphWin("Solution Window", solution_width, solution_height)
    # set background to black
    win.setBackground(color_rgb(150,200,210))
    # For each rectangle in the list
    for r in solution:
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
    return
