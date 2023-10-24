class Person:
    def __init__(self, name, age, gender): # init n constructor ya kuinput
        self.name = name
        self.age = age
        self.gender = gender
    def detail(self):
        print(self.name, "Is Studying")
p = Person("Joe",34, "Male")
p.detail()
