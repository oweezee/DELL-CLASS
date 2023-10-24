#poly many, morphism ni form, so many classes having same methods but output ni different
class Shape:
    def  draw(self):
        print("Drawing a shape")

class Rectangle:
    def draw(self):
        print("Drawing a Rectangle")

class Circle:
    def draw(self):
        print("Drawing a Circle")

r = Rectangle()
r.draw()

c = Circle()
c.draw()

