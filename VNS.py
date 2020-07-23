import csv
import sys
import Rectangle

# Main method
file_name = ''
# get the command line arguments
if len(sys.argv) == 2:
    file_name = sys.argv[1]
    print(file_name)
# parse in the csv to rectangle objects
rectangles = {}
rectangles = Rectangle.get_rectangles(file_name)
for rect in rectangles:
    rect.print()
