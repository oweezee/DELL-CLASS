# object has attributes and methods
# re-using code basically
class Student:
    name = "Joe"
    age = 23
    # creating a mthod, use def
    def study(self):
        print("Student is studying")

stu = Student() # creating an object
stu.study()
print(stu.name)