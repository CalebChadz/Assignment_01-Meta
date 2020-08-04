from NeighbourhoodFunctions import *
NEIGHBOURHOOD_SIZE = 30

class Solution:
    def __init__(self, max_width):
        self.width = max_width
        self.solution_matrix = []

    # funciton that decodes the list representation of boxes to a matrix representation and gives
    # the rectangles coordinates on a plane.
    def GetSolution(self, rectangle_list):
        solution_matrix = [ [0] * self.width ]
        init_x = 0
        init_y = 0
        for rect in rectangle_list:
            # always recalculate the starting height
            init_y = 0
            #check to see if this row is full, if yes start from left.
            if (init_x + rect.width) > (self.width-1):
                init_x = 0
            # check the bottom of rectangle is not colliding with any other rectangle for all side length
            ypos = 0
            while (ypos < rect.height):
                if(len(solution_matrix) - 1 < init_y + ypos):
                            solution_matrix.append([0] * self.width)
                xpos = 0
                while (xpos < rect.width):
                    if (solution_matrix[init_y + ypos][init_x + xpos] != 0):
                        init_y += 1
                        xpos = 0
                        ypos = 0
                        if(len(solution_matrix) - 1 < init_y):
                            solution_matrix.append([0] * self.width) 
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
        # length of matrics directly corresponds to the solution height
        self.solution_matrix = solution_matrix
        return solution_matrix 
    
    def getHeight(solution_matrix):
        return len(solution_matrix) - 1

# function to see if it is time to change neighborhoods based on given solutions.
def NeighborhoodChange(current_best, new_solution, curr_neighborhood):
    #current_best_value, = GetSolution(current_best)
    #new_solution_value, = GetSolution(new_solution)

    if (new_solution_value < current_best_value):
        curr_neighborhood = 1
        return new_solution, curr_neighborhood
    else:
        return current_best, (curr_neighborhood + 1)

#functions to be implemented:

# Shake, this will be the implementation of our neighborhood function to pull out a solution
# Shake(x,k) where x is current solition, k is current neighborhood. So based on current neighborhood and its
# neighborhood funciton, shake the solutiuon to a new solution.
def Shake(current_solution, current_neighbourhood):
    return current_neighbourhood.generateSolution(current_solution)

# BestImprovement, This will take the newly shaken solution and run Best improvement on all adjacent
# neighbors. In essence run a local search. Apply the current neighborhood function once again but this time
# on the new solution not on the current best solution, repeat for all neighbors and pick out the best
def BestImprovement(new_solution, current_neighbourhood, solution):
    current_solution = new_solution
    current_solution_matrix = solution.GetSolution(new_solution)
    current_solution_height = Solution.getHeight(current_solution_matrix)
    print(current_solution_height)
    best_solution = []
    best_solution_height = current_solution_height
    best_solution_matrix = current_solution_matrix
    for i in range(NEIGHBOURHOOD_SIZE):
        new_solution = current_neighbourhood.generateSolution(current_solution)
        new_solution_matrix = solution.GetSolution(new_solution)
        new_solution_height = Solution.getHeight(new_solution_matrix)
        if new_solution_height < best_solution_height:
            best_solution_height = new_solution_height
            best_solution = new_solution
            best_solution_matrix = new_solution_matrix
    print(Solution.getHeight(best_solution_matrix))
    if current_solution_height > best_solution_height:
        return best_solution
    else:
        return current_solution