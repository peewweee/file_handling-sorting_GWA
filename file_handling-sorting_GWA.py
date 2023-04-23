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

print("\033[0;35m Student with the highest GWA:")
# print the name with highest gwa
print("\033[0;34m Student Name:", highest_gwa_student)
print("\033[0;34m GWA:", highest_gwa)

print("")
# Print contents in the file
with open("students_gwa.txt") as input_file:
    print("\033[0;32m {:<30}{:<30}".format("Student Name", "GWA"))
    for line in input_file:
        student_name, student_gwa = line.strip().split(" - ")
        name_column = student_name
        gwa_column = student_gwa
        print("\033[0;37m {:<30}{:<30}".format(name_column, gwa_column))