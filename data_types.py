# string data type

# lietral assignment
first = "nash"
last = "hash"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# constructor function
# pizza = str("ham")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# concatenation
# fullname = first + " " + last
# print(fullname)

# Casting number to a string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like roxk music from the " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just joking. 

                    hahahahhahaha?

'''

print(multiline)

# Escaping special charcters
sentence = 'I\'m back ar work! \tHey! \n\n Where\'s this at\\located? '
print(sentence)

#String Methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("hahahahhahaha?", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                        "
multiline = "                   " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$1".rjust(4))
print("Cheese".ljust(16, ".") + "$1".rjust(4))

print("")
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some method return boolean data
print(first.startswith("n"))
print(first.startswith("N"))
print(first.endswith("h"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numric data type
price = 100
best_price =int(90)
print(type(price))
print(isinstance(best_price, int))

#float type
gpa = 3.29
y = float(1.13)
print(type(gpa))

#complex type
comp_value =5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to number
zipcode = "56799"
zip_value = int(zipcode)
print(type(zipcode))
print(type(zip_value))

#Error if you attempt to cast incorrect data
# zip_valye = int("katm")

