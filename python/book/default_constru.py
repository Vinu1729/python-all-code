class Student:
    def __init__(self):
        self.age=18
        self.gender="male"
        self.dept="computer engg"

    def update_value(self,a,g,d):
        self.age=a
        self.gender=g
        self.dept=d

    def show_values(self):
        print("age is ",self.age)
        print("gender is ",self.gender)
        print("department is ",self.dept)

s1=Student()
s2=Student()
print("default constructor is called")
s1.show_values()
print("defined values is showing")
s1.update_value(18,"female","IT")
print("values are updated as follow")
s1.show_values()
