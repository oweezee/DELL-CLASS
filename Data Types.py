# data type tells you the type of data a particular value belongs to

number = -100  # integer
second = 56.78 #float has decimal number
text = "Halo There" #string
ispythoninteresting = True # boolean

# storing multiple values in a variable
cars = ["Toyota" ,"Nissan", "BMW", "Land Rover", 49] #list inaandikwa na hizi brackets
# tuple  values are ordered but cant be changed, list can be changed
fruits = ("banana", "oranges", "apples")
countries = {"Kenya", "Uganda", "Tanzania","Algeria" } # set - can be changed
details = {
    "firstname": "Owen",
    "Age" : 24 ,
    "Course" : "Web Dvpt",
    "Nationality" : "Kenyan"
} #dictionary displays keys and values or stores multiple elements in a single value
print(second)
print(text)
print(details["firstname"])
print(details["Age"])
print(cars)
print(countries)

#determine a datatype by using the type method
print(type(text))
print(type(countries))
print(type(details))

#typecasting - converting one data type to another
print(float(number)) # decimal
print(int(second)) #whhole number
print(ispythoninteresting)