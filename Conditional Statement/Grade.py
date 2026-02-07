# Student Details
name = "Rohit Sharma"
roll_no = "R17234512"
sapid = "50005673"
sem = "1"
course = "B.Tech. CSE AI&ML"

# Subject Marks
pds = int(input("Enter marks for PDS: "))
python = int(input("Enter marks for Python: "))
chemistry = int(input("Enter marks for Chemistry: "))
english = int(input("Enter marks for English: "))
physics = int(input("Enter marks for Physics: "))

# Calculations
total_marks = pds + python + chemistry + english + physics
percentage = (total_marks / 500) * 100
cgpa = percentage / 10

# Grade Assignment
if cgpa <= 3.4:
    grade = "F"
elif cgpa <= 5.0:
    grade = "C+"
elif cgpa <= 6.0:
    grade = "B"
elif cgpa <= 7.0:
    grade = "B+"
elif cgpa <= 8.0:
    grade = "A"
elif cgpa <= 9.0:
    grade = "A+"
else:
    grade = "O (Outstanding)"

# Output Grade Sheet
print("\n----------- GRADE SHEET -----------")
print(f"Name: {name}")
print(f"Roll Number: {roll_no}\t\tSAPID: {sapid}")
print(f"Sem: {sem}\t\t\tCourse: {course}\n")

print("Subject Name\tMarks")
print(f"PDS\t\t{pds}")
print(f"Python\t\t{python}")
print(f"Chemistry\t{chemistry}")
print(f"English\t\t{english}")
print(f"Physics\t\t{physics}")

print(f"\nPercentage: {percentage:.0f}%")
print(f"CGPA: {cgpa:.1f}")
print(f"Grade: {grade}")
