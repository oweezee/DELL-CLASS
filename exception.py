try:
    print(x) # no assigned vallue for x

except:
    print("404 Not Found") #message to shw instead of error
finally:
    print("Success") #ikiwa na error, anything in except block is printed as finally block with the message