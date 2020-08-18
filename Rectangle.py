import csv
from graphics import *

def getByRectID(rect_List, _id):
    myRect = None
    for rect in rect_List:
        if rect.id == _id:
            myRect = rect
    return myRect

# funciton that decodes the list representation of boxes to a matrix representation and gives
# the rectangles coordinates on a plane.
def CalculateRectanglePositions(rectangle_list, given_width, initial):
    solution_matrix = [ [0] * given_width ]
    init_x = 0
    init_y = 0
    for rect in rectangle_list:
        if rect.width < rect.height and initial:
            rect.Rotate()
        # check the bottom of rectangle is not colliding with any other rectangle for all side length
        ypos = 0
        while (ypos < rect.height):
            if(len(solution_matrix) <= init_y + ypos):
                solution_matrix.append([0] * given_width)
            xpos = 0
            while (xpos < rect.width):
                check = solution_matrix[init_y + ypos][init_x + xpos]
                if (check != 0):
                    trec = getByRectID(rectangle_list, check)
                    xpos_skip = trec.xpos
                    width_skip = trec.width
                    init_x = width_skip + xpos_skip
                    xpos = 0
                    ypos = 0
                else:
                    xpos += 1
                    
                if((init_x + rect.width) > (given_width)):
                    init_x = 0
                    init_y += 1 
                    xpos = 0
                    ypos = 0
                    if(len(solution_matrix) - 1 < init_y + ypos):
                        solution_matrix.append([0] * given_width)
            ypos += 1
        #now we have a free space to draw the rect
        rect.xpos = init_x 
        rect.ypos = init_y
        # fill in its matrix space
        for x in range(rect.width):
            for y in range(rect.height):
                solution_matrix[rect.ypos + y][rect.xpos + x] = rect.id
        init_x = 0
        init_y = 0
    # length of matrics directly corresponds to the solution height
    return rectangle_list, solution_matrix

# function to get the height of solution
def getHeight(rectangle_list):
    height = 0
    for rect in rectangle_list:
        this_height = rect.ypos + rect.height
        if this_height > height:
            height = this_height
    return height


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
        self.rotated = not self.rotated

class Solution:
    def __init__(self, rectangle_list, given_width, initial):
        self.given_width = given_width
        self.rectangle_list, self.rectangle_matrix = CalculateRectanglePositions(rectangle_list, given_width, initial)
        self.height = getHeight(self.rectangle_list)
        
    # function to draw a solution
    def drawSolution(self, scale):
        solution_width = (self.given_width * scale) + 1
        solution_height =  (self.height * scale) + 1
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
