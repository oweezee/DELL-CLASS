# while loop continues until a condition is met
number = 20
while number <=25:
    print(number)
    number += 1

#decreasing value
a =10
while a >=1: #condition
    print(a)
    a-=1

#for loop  bring values in a given squence or print a given range of values
languages =["Python", "PHP", "Kotlin", "C++"]
#print(languages)
for lang in languages: # x ama lang does the same thing, inbuilt
    print(lang)

# Range
for x in range (10): # only prints upto 9
    print(x)
    #to give a starting point
for b in range (15, 20): #15 ndio SP,
    print(b)

for c in range (4, 30, 2): # increase values
     print(c)