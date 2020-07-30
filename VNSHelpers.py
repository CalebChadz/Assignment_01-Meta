def GetSolution(rectangle_list, max_width):
    solution_matrix = [ [0] * max_width ]
    init_x = 0
    init_y = 0
    for rect in rectangle_list:
        # always recalculate the starting height
        init_y = 0
        #check to see if this row is full, if yes start from left.
        if (init_x + rect.width) > (max_width-1):
            init_x = 0
        # check the bottom of rectangle is not colliding with any other rectangle for all side length
        ypos = 0
        while (ypos < rect.height):
            if(len(solution_matrix) - 1 < init_y + ypos):
                        solution_matrix.append([0] * max_width)
            xpos = 0
            while (xpos < rect.width):
                if (solution_matrix[init_y + ypos][init_x + xpos] != 0):
                    init_y += 1
                    xpos = 0
                    ypos = 0
                    if(len(solution_matrix) - 1 < init_y):
                        solution_matrix.append([0] * max_width) 
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
    return (len(solution_matrix) - 1), solution_matrix 

def NeighborhoodChange(current_best, new_solution, curr_neighborhood):
    current_best_value, = GetSolution(current_best)
    new_solution_value, = GetSolution(new_solution)

    if (new_solution_value < current_best_value):
        curr_neighborhood = 1
        return new_solution, curr_neighborhood
    else:
        return current_best, (curr_neighborhood + 1)