# Creating Nested Dictionary

inside = {"first_box": {1: "Meat", 2: "Medicine", 3: "Sweets"}, "second_box": {1: "Water", 2: "Air", 3: "Sprey"}}
print(inside)

# Access elements of Dictionary
print(inside["first_box"][2])
print(inside["second_box"][1])

# Changing Elements of The Nested Dictionary
print("-------------------" + " Changing")
inside["third box"] = {}
inside["third box"][1] = "FleshLight"
inside["third box"][2] = "Knife"
inside["third box"][3] = "Rope"
print(inside["third box"])

# Deleting Elements of Nested Dictionary
print("-------------------" + " Deleting")
del inside["first_box"][3]
del inside["third box"]
print(inside["first_box"])
print(inside)

# Iterating Through a Nested Dictionary
print("-----------------" + " Iterating")
print(inside.items())
for box_num, box_info in inside.items():
    print("\nBox Number:", box_num)
    for item in box_info:
        print("Item number: {0} , item name: {1}".format(item, box_info[item]))

"""Nested dictionary is an unordered collection of dictionary
Slicing Nested Dictionary is not possible.
We can shrink or grow nested dictionary as need.
Like Dictionary, it also has key and value.
Dictionary are accessed using key.
"""
