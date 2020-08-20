from VNS import *

for i in range(2, 7):
    file_solution = open("solution_M1a.txt", "w")
    file_solution.write("BVNS " + str(i) + " " + test("B", i))
    file_solution.write("VNDS " + str(i) + " " + test("V", i))
    file_solution.write("RVNS " + str(i) + " " + test("R", i))
    file_solution.write("GVNS " + str(i) + " " + test("G", i))
file_solution.close()
