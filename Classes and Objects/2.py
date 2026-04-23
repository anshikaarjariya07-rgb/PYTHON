'''Add constructor in the above class to initialize student details of n students and implement following methods:
a)	Display() student details
b)	Find Marks_percentage() of each student
c)	Display result() [Note: if marks in each subject >40% than Pass else Fail]
d)	Write a Function to find average of the class.
'''
class Student:
    def __init__(self, name, sap_id, phy, chem, maths):
        self.name = name
        self.sap_id = sap_id
        self.marks = {
            'Physics': phy,
            'Chemistry': chem,
            'Maths': maths
        }

    # a) Display student details
    def display(self):
        print("\nStudent Details:")
        print("Name:", self.name)
        print("SAP ID:", self.sap_id)
        print("Marks:")
        for subject, marks in self.marks.items():
            print(subject + ":", marks)

    # b) Calculate percentage
    def marks_percentage(self):
        total = sum(self.marks.values())
        percentage = total / 3
        return percentage

    # c) Display result (Pass/Fail)
    def result(self):
        for marks in self.marks.values():
            if marks < 40:
                return "Fail"
        return "Pass"


# d) Function to find class average percentage
def class_average(students):
    total_percentage = 0
    for student in students:
        total_percentage += student.marks_percentage()
    return total_percentage / len(students)


# ---------------- MAIN PROGRAM ----------------

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}:")
    name = input("Enter student name: ")
    sap_id = input("Enter student SAP ID: ")
    phy = float(input("Enter Physics marks: "))
    chem = float(input("Enter Chemistry marks: "))
    maths = float(input("Enter Maths marks: "))

    s = Student(name, sap_id, phy, chem, maths)
    students.append(s)

# Display details, percentage, and result
print("\n--- All Student Details ---")
for student in students:
    student.display()
    print("Percentage:", student.marks_percentage())
    print("Result:", student.result())

# Class average
avg = class_average(students)
print("\nClass Average Percentage:", avg)