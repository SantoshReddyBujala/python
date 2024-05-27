value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("Value now is equal to " + str(value))

names = ["Santosh", "Reddy", "Bujala"]
# for name in names:
#     print(name)

# for char in "Atlanta":
#     print(char)

# for name in names:
#     if name == "Reddy":
#         break
#     print(name)

# for name in names:
#     if name == "Reddy":
#         continue
#     print(name)

# for num in range(5):
#     print(num)

# for num in range(2, 5): #auto increment by 1
#     print(num)

# for num in range(0, 50, 5): #increment by 5
#     print(num)

# for num in range(0, 51, 5):  # increment by 5
#     print(num)
# else:
#     print("Glad that\'s over✅")

names = ["Santosh", "Reddy", "Bujala"]
actions = ['drink', 'eat', 'walk']
# for name in names:
#     for action in actions:
#         print(name+" "+action+".")

for action in actions:
    for name in names:
        print(name+" "+action+".")
