def add_one(num):
    if (num >= 9):
        return num + 1
    total = num + 1
    print(total)
    return add_one(total)


finalTotal = add_one(0)
print('Final Total')
print(finalTotal)

print("")
value = 1
while value:
    print(value)
    value = 0

print("")
value = True
while value:
    print(value)
    value = False


print("")
value = 1
count = 0
while value:
    count += value
    print(count)
    if (count >= 5):
        break
    else:
        value = 0
        continue
