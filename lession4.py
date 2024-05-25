# data_type.py of the file
import math
# String data type
# Literal assignment
first = 'Santosh'
last = 'Bujala'
print(type(first))
print(type(first) == str)
print(isinstance(first, str))

print("")

# construction function
pizza = str('cheese')
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

# concatenation
fullname = first + " " + last
print(fullname)
fullname += "!!!"
print(fullname)

# Casting a number to string
decade = str(1980)
print(type(decade))
print(decade)

statement = "I like music of " + decade + "s."
print(statement)

# Multiline statments
multiline = '''
Hi, how are doing       

Just checking?

            I hope everything good.

'''
print(multiline)
# Escaping special characters
sentences = 'I\'m back in few min\t or soon!\n\n\n\n Think once\\.'
print(sentences)

# String methods
print(first)
print(first.lower())
print(last.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += '                          '

multiline = '                          ' + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build Menu
title = "Menu".upper()
print(title.center(20, "="))
print("Coffe".ljust(15, '-') + "$2".rjust(4))
print("Milk".ljust(15, '-') + "$1".rjust(4))
print("Drink".ljust(15, '-') + "$5".rjust(4))

print("")

# String Index values
print(first[2])
print(first[-1])
print(first[1:-1])
print(first[1:])

print("")
# Some methods returns boolean values
print(first.startswith('S'))
print(first.endswith('R'))

print("")
# Boolean Data
myValue = True
secValue = bool(False)
print(type(myValue))
print(isinstance(secValue, bool))


print("")
# Interger type
myValue = 100
secValue = int(80)
print(type(myValue))
print(isinstance(secValue, int))

print("")
# Float type
gpa = 100.25
secFloat = float(80.36)
print(type(gpa))
print(isinstance(secFloat, float))

print("")
# Complex value
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

print("")
# Built-in functions of integer
print(abs(gpa))
print(gpa * -1)
print(round(gpa))
print(round(gpa, 1))

print("")
print(math.pi)
print(math.sqrt(64))
print(math.floor(gpa))
print(math.ceil(gpa))

print("")
# Casting string to integer
zipcode = "30097"
zipcode_value = int(zipcode)
print(type(zipcode_value))
