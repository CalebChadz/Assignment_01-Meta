from GetSolution import *
MAX_WIDTH = 400
def NeighborhoodChange(current_best, new_solution, curr_neighborhood):
    current_best_value, = get_solution(current_best)
    new_solution_value, = get_solution(new_solution)

    if (new_solution_value < current_best_value):
        curr_neighborhood = 1
        return new_solution, curr_neighborhood
    else:
        return current_best, (curr_neighborhood + 1)