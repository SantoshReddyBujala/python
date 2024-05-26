users = ["Santosh", "Reddy", "Bujala"]
data = ["Santosh", 38, True]
empty_list = []
print("Bujala" in empty_list)

print("")
print(users[0])

print("")
print(users[-1])

print("")
print(users.index('Reddy'))

print("")
print(users[0:2])

print("")
print(users[1:])

print("")
print(len(data))

print("")
users.append('Swetha')
print(users)

print("")
users += ['Reddy', 'Gangireddy']
print(users)

print("")
users.extend(['Manvith', 'Reddy', 'Bujala'])
print(users)

# print("")
# users.extend(data)
# print(users)

print("")
users.insert(0, 'Manmadh')
print(users)

print("")
users[2:2] = ['San', 'Man']
print(users)

print("")
users[1:3] = ['Re', 'Ddy']
print(users)

print("")
users.remove('Reddy')
print(users)

print("")
print(users.pop())
print(users)

print("")
del users[0]
print(users)

print("")
# del data
data.clear()
print(data)

print("")
users.sort()
print(users)

print("")
users[1:2] = ['pad']
users.sort()
print(users)

print("")
users.sort(key=str.lower)
print(users)

print("")
num = [3, 56, 32, 43, 5]
num.reverse()
print(num)

print("")
num.sort()
print(num)


print("")
num.sort(reverse=True)
# num.reverse()
print(num)

print("")
print(sorted(num, reverse=True))

print("")
numCopy = num.copy()
print(numCopy)

print("")
numList = list(numCopy)
print(numList)

print("")
numNewCopy = num[:]
print(numNewCopy)

print("")
print(num)

print("")
print(type(num))

print("")
mylist = list([1, 'San', True])
print(mylist)

# Tuples
print("")
myTuple = tuple((1, 'San', True))
anotherTuple = (1, 23, 34, 58, 23)
print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

print("")
(one, two, *hey) = anotherTuple
print(one)
print(two)
print(hey)

print("")
(one, *two, hey) = anotherTuple
print(one)
print(two)
print(hey)

print("")
print(anotherTuple.count(34))
