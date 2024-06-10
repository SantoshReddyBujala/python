from functools import reduce
def square(num): return num * num
# lambda num: num * num


print(square(3))


def addTwo(num): return num + 5
# lambda num: num + 5


print(addTwo(5))


def sum_Two(a, b): return a+b
# lambda a, b: a + b


print(sum_Two(18, 16))

################################


def funtionBuilder(x):
    return lambda num: num + x


addTen = funtionBuilder(10)
addTwenty = funtionBuilder(20)

print(addTen(8))
print(addTwenty(8))

#########################

numbers = [3, 7, 10, 11, 15, 20, 21, 25, 40, 60]

squared_numbers = map(lambda num: num * num, numbers)

print(list(squared_numbers))

##########################

odd_numbers = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_numbers))

##########################


total = reduce(lambda acc, curr: acc + curr, numbers)

print(total)

print(sum(numbers))

totals = reduce(lambda acc, curr: acc + curr, numbers, 31)

print(totals)

print(sum(numbers, 39))

names = ['Santosh', 'Reddy', 'Bujala']

totalStringCount = reduce(lambda acc, curr: acc + len(curr), names, 0)
print(totalStringCount)
