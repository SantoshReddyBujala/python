# Dictionaries
band = {
    "key": "value",
    "key1": "value1"
}

band1 = dict(key="value", key1="value1")
print(band)
print(band1)
print(type(band))
print(len(band))

# Access the items
print("")
print(band["key"])
print(band.get("key1"))

# List all keys
print("")
print(band.keys())

# List all values
print("")
print(band.values())

# List of key,value fairs as a tuples
print("")
print(band.items())

# Verify Keys
print("")
print("key" in band)
print("keys" in band)

# Change value
print("")
band["key"] = "value2"
band.update({"key2": "value2"})
print(band)

# Remove items
print("")
print(band.pop("key2"))
print(band)

print("")
band["key3"] = "value3"
print(band)

print("")
print(band.popitem())
print(band)

# Delete or Clear
print("")
band["key4"] = "value4"
print(band)
del band["key4"]
print(band)

band1.clear()
print(band1)

del band1
# print(band1)

# Copying
# band1 = band  # it create a reference
# print("Bad copy😲🤣")
# print(band1)
# print(band)

# band1["key5"] = "value5"
# print(band)

band1 = band.copy()  # it create a new memory
print("right copy 👌")

band1["key6"] = "value6"
print(band)
print(band1)

# copy with constructor
print("")
band2 = dict(band)
print("right copy 👌")
print(band2)

# Nested dictionaries
print("")
member = {"key": "value", "key1": "value1"}
member1 = {"key2": "value2", "key3": "value3"}
band3 = {"key4": member, "key5": member1}
print(band3)
print(band3["key4"]["key"])

# Sets
print("Sets\n")
num = {1, 2, 3, 4, 5}
num1 = set((1, 2, 3, 4, 5))
print(num)
print(num1)
print(type(num))
print(len(num))

# No duplicates allowed
num2 = {1, 2, 3, 3, 4, 5}
print("")
print(num2)

# True is a duplicate of 1 and False is a duplicate of 0
num3 = {1, True, 2, 3, 3, False, 4, 5, 0}
print("")
print(num3)

# Check if a value in set
num4 = {1, 2, 3, 7}
print("")
print(7 in num4)

# Add a new element to set
print("")
num4.add(10)
print(num4)

# Add one set to another set
print("")
num4.update(num2)
print(num4)

# update will work with list, dictionary and tuples

# Merge 2 sets to another
print("")
set = {1, 2, 3}
set1 = {2, 3, 4}

mergeSet = set.union(set1)
print(mergeSet)

# Keep only duplicates
set.intersection_update(set1)
print(set)

# Keep exclude duplicates
set2 = {1, 2, 3}
set3 = {2, 3, 4}
set2.symmetric_difference_update(set3)
print(set2)
