# Python does not have built in matrix but we can use lists
# Creating Matrix

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_matrix)
print("matris[0][1]=", my_matrix[0][1])
print("matris[2][-1]=", my_matrix[2][-1])

# Add two matrices
# Nested Loop
second = [[2, 2, 2], [3, 3, 3], [4, 4, 4]]
last = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(my_matrix)):
    for j in range(len(my_matrix[0])):
        last[i][j] = my_matrix[i][j] + second[i][j]

print(last)
# Column
column = []
i = 0
# ?
for row in my_matrix:
    column.append(row[0])
    print(row[i])
    i = i + 1
print(column)
# Nested List Comprehension
result = [[my_matrix[i][j] + second[i][j] for j in range(len(my_matrix[0]))] for i in range(len(my_matrix))]

print(result)

# Transpose
for i in range(len(my_matrix)):
    for j in range(len(my_matrix[0])):
        last[j][i] = my_matrix[i][j]
print(last)

# With Comprehension
new_res = [[second[j][i] for j in range(len(second))] for i in range(len(second[0]))]
print(new_res)

# Some ways to create
my_mat = []
for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    my_mat.append(a)
second = []
for i in range(3):
    second.append(int(input()))
c = [0, 0, 0]
for i in range(3):
    for j in range(3):
        c[i] += my_mat[i][j] * second[j]
for i in range(3):
    for j in range(3):
        print(my_mat[i][j], end=" ")
    print()
for i in range(3):
    print(c[i])
