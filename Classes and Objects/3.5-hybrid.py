# Base Class
class Person:
    def show_person(self):
        print("This is Person")


# Hierarchical Inheritance
class Student(Person):
    def show_student(self):
        print("This is Student")

class Teacher(Person):
    def show_teacher(self):
        print("This is Teacher")


# Multilevel Inheritance
class Monitor(Student):
    def show_monitor(self):
        print("This is Monitor")


# Multiple Inheritance (combining Student + Teacher)
class Assistant(Student, Teacher):
    def show_assistant(self):
        print("This is Assistant")


# -------- MAIN --------
print("\n--- Hybrid Inheritance Demonstration ---")

m = Monitor()
m.show_person()
m.show_student()
m.show_monitor()

a = Assistant()
a.show_person()
a.show_student()
a.show_teacher()
a.show_assistant()