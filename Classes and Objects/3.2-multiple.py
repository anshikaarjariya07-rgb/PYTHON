class Father:
    def skill_father(self):
        print("Father: Driving")

class Mother:
    def skill_mother(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    def skill_child(self):
        print("Child: Coding")

obj = Child()
obj.skill_father()
obj.skill_mother()
obj.skill_child()