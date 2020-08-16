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
        self.rotated = False
        self.swapped = False
        self.moved = False
# Quickly print off this rectangles current values.
    def Print(self):
        print("ID: " + str(self.id) + "\nDimensions: (" + str(self.width) + ", " + str(self.height) + ")" + "\nCoordinates: (" + str(self.xpos) + ", " + str(self.ypos) + ")")
# Rotate the rectangle by switching width and height
    def Rotate(self):
        width = self.width
        self.width = self.height
        self.height = width
# Function to read in a CSV file of rectangle dimensions to be stored as rectangle objects.
def GetRectangles(file_name):
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
def DrawSolution(solution, solution_width, solution_height, scale):
    solution_width = solution_width * scale
    solution_height = solution_height * scale
    win = GraphWin("Solution Window", solution_width, solution_height + 100)
    # set background to black
    win.setBackground(color_rgb(150,200,210))
    # For each rectangle in the list
    for r in solution:
        rHeight = r.height * scale
        rWidth = r.width * scale
        rX = r.xpos * scale
        rY = r.ypos * scale
        #get the position of this rectangle and create a drawable.
        pt1 = Point(rX, rY)
        pt2 = Point((rX + rWidth), (rY + rHeight))
        rect_draw  = Rectangle(pt1, pt2)
        # set the outline color
        if r.rotated:
            rect_draw.setFill(color_rgb(0,255,0))
        elif r.moved:
            rect_draw.setFill(color_rgb(0,0,255))
        elif r.moved and r.rotated:
            rect_draw.setFill(color_rgb(0,255,255))
        else:
            rect_draw.setFill(color_rgb(199,0,57))
        # draw it to the window
        rect_draw.draw(win)
    # wait for a click then close the program
    win.getMouse()
    win.close()
    return
