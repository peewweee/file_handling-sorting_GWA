# File handling - Sorting GWA
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# open students_gwa file
with open("students_gwa.txt") as input_file:
    # initialize gwa and student name using lowest possible gwa and student name
    # read students_gwa file per line and split the student's name and gwa
    for line in input_file:
        name, gwa_str = line.strip().split(" - ")
        print("Name:", name, "has a GWA of:", gwa_str)
        # if gwa < lowest possible grade, get highest gwa and name

    # print the name with highest gwa
