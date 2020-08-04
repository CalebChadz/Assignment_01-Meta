import random
from Rectangle import *

class Neighbourhood:
    def __init__(self, neighbourhoodIndex):
        self.index = neighbourhoodIndex

    def FlipHalf(self, rectangle_list):
        for rectangle in rectangle_list:
            isFlipped = random.choice([True, False])
            if isFlipped:
                rectangle.Rotate()
        return rectangle_list
    
    def generateSolution(self, rectangle_list):
        if self.index == 1:
            self.FlipHalf(rectangle_list)
        return rectangle_list