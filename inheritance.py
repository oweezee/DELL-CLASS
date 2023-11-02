#parent class
class Animal :
    def speak(self):
        print("Animal is Speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")
class Cat(Animal): # mention parent class
    def purr(self):
        print("Cat is purring")
d = Dog() #inheritance hlps reduce copying code by recalling a certain functiuon
d.bark()

c = Cat()
c.purr()