person = "Santosh"
coins = 3

message = "\n%s has %s coins left." % (person, coins)
print(message)

message = "\n{} has {} coins left.".format(person, coins)
print(message)

# indexing with format method
message = "\n{1} has {0} coins left.".format(coins, person)
print(message)

# parameters with format method
message = "\n{person} has {coins} coins left.".format(
    coins=coins, person=person
)
print(message)

player = {'person': "Bujala", 'coins': 5}
# Dectionary
message = "\n{person} has {coins} coins left.".format(**player)
print(message)

#######################
# f-Strings! This is the way.

message = f"\n{person} has {coins} coins left."
print(message)

message = f"\n{person} has {coins * 4} coins left."
print(message)

message = f"\n{person.upper()} has {coins * 4} coins left."
print(message)

message = f"\n{person.lower()} has {coins * 4} coins left."
print(message)

# Double quote starts params wrap with single quotes
message = f"\n{player['person']} has {coins * 4} coins left."
print(message)

# Single quote starts params wrap with double quotes
message = f'\n{player["person"]} has {coins * 4} coins left.'
print(message)

######################
# You can pass formatting options
num = 5
print(f"\n2.25 times {num} is {2.25 * num:.2f}")

print(f"\n2.25 times {2*num} is {2.25 * (2*num):.2f}\n")
for num in range(1, 16):
    print(f"2.25 times {num} is {2.25 * num:.2f}")
