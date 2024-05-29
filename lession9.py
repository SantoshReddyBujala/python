def hello():
    print("Hello!")


hello()


def hello_world():
    print("Hello World!")


hello_world()


def sum(num1, num2):
    print(num1+num2)


sum(1, 5)
sum(15, 55)
sum(100, 200)


def sub(num1, num2):
    if (type(num1) is not int or type(num2) is not int):
        return 0
    elif num1 < num2:
        return "Minus value"
    return num1-num2


subtraction = sub(10, 5)
print(subtraction)
print(sub(20, 'c'))
print(sub(2, 10))


def sumDefault(n1=0, n2=0):
    if (type(n1) is not int or type(n2) is not int):
        return 0
    return n1+n2


print(sumDefault())
print(sumDefault(1))
print(sumDefault(1, 2))


def multiple_args(*args):
    print(args)
    print(type(args))
    for name in args:
        print(name)


multiple_args('Santosh', 'Reddy', 'Bujala')


def multi_name_args(**kwargs):
    print(kwargs)
    print(type(kwargs))


multi_name_args(fistname='Santosh Reddy', lastname='Bujala')
