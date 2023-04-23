# File handling - Sorting GWA
# Phoebe Rhone L. Gangoso | BSCPE 1-4

# open students_gwa file
with open("students_gwa.txt") as input_file:
    # initialize gwa and student name using lowest possible gwa and student name
    highest_gwa = 5.0
    highest_gwa_student = ""
    # read students_gwa file per line and split the student's name and gwa
    for line in input_file:
        name, gwa_str = line.strip().split(" - ")
        # if gwa < lowest possible grade, get highest gwa and name
        gwa = float(gwa_str)
        if gwa < highest_gwa:
            highest_gwa = gwa
            highest_gwa_student = name
    # print the name with highest gwa
    print(highest_gwa)
    print(highest_gwa_student)

# Print contents in the file
with open("students_gwa.txt") as input_file:
    print("\nStudents' GWA:")
    for line in input_file:
        print(line.strip())