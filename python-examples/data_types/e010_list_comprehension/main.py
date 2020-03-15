# List Comprehension vs For Loop
letters = []
for letter in "Yare Yare":
    letters.append(letter)
print(letters)

dif_letters = [i for i in "OH MY GOD"]
print(dif_letters)

# Lambda Functions
new_letters = list(map(lambda x: x, "DORA DORA DORA"))
print(new_letters)

# Conditionals
numbers = [x for x in range(16) if x % 5 == 0]
print(numbers)

num = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(num)

count = ["Three" if i % 3 == 0 else "Any" for i in range(20)]
print(count)
