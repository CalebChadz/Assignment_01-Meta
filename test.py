import sys
from VNS import *

for i in range(2, 7):
    file_solution = open("solution_" + sys.argv[1].strip('.csv') + ".txt", "a")
    file_solution.write("BVNS " + str(i) + " " + test("B", i) + "\n")
    file_solution.write("VNDS " + str(i) + " " + test("V", i) + "\n")
    file_solution.write("RVNS " + str(i) + " " + test("R", i) + "\n")
    file_solution.write("GVNS " + str(i) + " " + test("G", i) + "\n")
file_solution.close()
