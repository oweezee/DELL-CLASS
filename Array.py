# similar to a list

Courses = ["MIT", "Cyber Scurity", "Data Science"] #special brackets

print(Courses)

print(Courses[1])# index position to print out one elelment in an array
print(Courses[2])# index position to print out one elelment in an array

#looping through ana array- without speial brackets
for Course in Courses:
    print(Course)

    #adding an eelelment in an array
Courses.append("Android Development")
print(Courses)

#removing ana element in an array
Courses.remove("MIT")
print(Courses)