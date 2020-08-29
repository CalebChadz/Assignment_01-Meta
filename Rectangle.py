#Caleb_1328518_Priyank_1297953
import csv
import numba as nb
import numpy as np
from graphics import *

def getByRectID(rect_List, _id):
    myRect = None
    for rect in rect_List:
        if rect.id == _id:
            myRect = rect
    return myRect

@nb.jit(nopython=True)
def check(rectHeight, rectWidth, rectId, given_width, solution_matrix):
    solution_row = np.array([[0] * given_width])
    init_x = 0
    init_y = 0
    rectXpos = 0
    rectYpos = 0
    ypos = 0
    while (ypos < rectHeight):
        if(len(solution_matrix) <= init_y + ypos):
            solution_matrix = np.vstack((solution_matrix, solution_row))
        xpos = 0
        while (xpos < rectWidth):
            check = solution_matrix[init_y + ypos][init_x + xpos]
            if (check != 0):
                init_x += 1
                xpos = 0
                ypos = 0
            else:
                xpos += 1
                
            if((init_x + rectWidth) > (given_width)):
                init_x = 0
                init_y += 1 
                xpos = 0
                ypos = 0
                if(len(solution_matrix) <= init_y + ypos):
                    solution_matrix = np.vstack((solution_matrix, solution_row))
        ypos += 1
    #now we have a free space to draw the rect
    rectXpos = init_x 
    rectYpos = init_y
    # fill in its matrix space
    for x in range(rectWidth):
        for y in range(rectHeight):
            solution_matrix[rectYpos + y][rectXpos + x] = rectId
    init_x = 0
    init_y = 0
    return rectXpos, rectYpos, solution_matrix

@nb.jit(nopython=True)
def getValue(solution_matrix, given_width):
    length = len(solution_matrix)
    value = 0
    rows = 0
    for y in range(length):
        for x in range(given_width):
            if solution_matrix[y][x] == 0:
                value += 1
    if value == given_width:
        value = 0
        for i in range(given_width):
            if not solution_matrix[length - 1][i] == 0:
                value += 1
        return value
    else:
        rows = (value / given_width)
        value = 0
        for r in range(rows):
            for c in range(given_width):
                if not solution_matrix[(length - r)-1][c] == 0:
                    value += 1
    return value

# funciton that decodes the list representation of boxes to a matrix representation and gives
# the rectangles coordinates on a plane.
def CalculateRectanglePositions(rectangle_list, given_width, initial):
    #print("Start")
    #start = time.time()
    solution_matrix = np.array([ [0] * given_width ])
    init_x = 0
    init_y = 0
    for rect in rectangle_list:
        rect.xpos, rect.ypos, solution_matrix = check(rect.height, rect.width, rect.id, given_width, solution_matrix)
    value = getValue(solution_matrix, given_width)
    #print("Time: " + str(time.time() - start))
    return rectangle_list, value, len(solution_matrix)


# A rectangle object to represent the rectangles in out problem.
class Rect:
    def __init__(self, id, width, height, xpos, ypos):
        self.id = id
        self.width = width
        self.height = height
        self.xpos = xpos
        self.ypos = ypos
        self.rotated = False
# Quickly print off this rectangles current values.
    def Print(self):
        return ("\nID: " + str(self.id) + "\nDimensions: (" + str(self.width) + ", " + str(self.height) + ")" + "\nCoordinates: (" + str(self.xpos) + ", " + str(self.ypos) + ")")
# Rotate the rectangle by switching width and height
    def Rotate(self):
        width = self.width
        self.width = self.height
        self.height = width
        self.rotated = not self.rotated

class Solution:
    def __init__(self, rectangle_list, given_width, initial):
        self.given_width = given_width
        self.rectangle_list, self.height, self.drawHeight = CalculateRectanglePositions(rectangle_list, given_width, initial)
        
    # function to draw a solution
    def drawSolution(self, scale):
        solution_width = (self.given_width * scale) + 1
        solution_height =  (self.drawHeight * scale) + 1
        win = GraphWin("Solution Window", solution_width, solution_height) 
        # set background to black
        win.setBackground(color_rgb(150,200,210))
        for r in self.rectangle_list:
            rHeight = r.height * scale
            rWidth = r.width * scale
            rX = r.xpos * scale
            rY = r.ypos * scale
            #get the position of this rectangle and create a drawable.
            pt1 = Point(rX, rY)
            pt2 = Point((rX + rWidth), (rY + rHeight))
            pt3 = Point(rX + 7, rY + 5)
            rect_draw  = Rectangle(pt1, pt2)
            message = Text(pt3, str(r.id))
            message.setSize(10)
            # set the outline color
            if r.rotated:
                rect_draw.setFill(color_rgb(0,255,0))
            else:
                rect_draw.setFill(color_rgb(199,0,57))
            # draw it to the window
            rect_draw.draw(win)
            message.draw(win)
        # wait for a click then close the program
        win.getMouse()
        win.close()
        return


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
