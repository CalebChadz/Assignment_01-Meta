import csv
import sys
import Rectangle

# Function for reading in a CSV file and translatng to Rectangle objects
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
                rectangles.append(Rectangle(row[0], row[1], row[2], 0,0))
    return rectangles

# Main method
file_name = ''
# get the command line arguments
if len(sys.argv) == 2:
    file_name = sys.argv[1]
    print(file_name)
# parse in the csv to rectangle objects
rectangles = {}
rectangles = get_rectangles(file_name)
for rect in rectangles:
    rect.print()


