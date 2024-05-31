name = "Santosh"  # global scope


def greeting():
    color = 'Green'  # local scope
    print(name)
    print(color)


greeting()
# print(color) we can't access local scope variable
print("")


def greeting_param(name):
    print(name)  # it will take param value instated of global variable value


greeting_param('Reddy')
print("")


def another():
    greeting_param('Santosh Bujala')


another()

print("")


def nested():
    color = "Orange"

    def inner(name):
        nonlocal color  # In function when we use defined variable to modify we will use nonlocal keyword
        color = "blue"
        print(color)
        print(name)

    inner('Bujala')


nested()

# global key word

print("")
count = 1


def globalKey():
    # count = 2
    # count += 1 you can not modify global variable value
    global count  # we need to use global count and modify into saperate lines
    count += 1
    print(count)


globalKey()
