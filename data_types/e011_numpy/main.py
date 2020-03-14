import numpy

# Array
A = numpy.array([1, 2, 3])
print(A)
print(type(A))

# Integer
numww = numpy.array([[1, 2, 3], [4, 5, 6]])

# Floats
float_num = numpy.array([[2.3, 1.1, 5], [3, 12, 3]])

# Complex Numbers
comp = numpy.array([[2, 3, 12], [5, 6, 7]], dtype=complex)
print("Numbers= ", numww)
print("Floats= ", float_num)
print("Complex= ", comp)

# Array of Zeroes and Ones
re_zero = numpy.zeros((3, 2))
print("Zeroes= ", re_zero)

# numpy.int32 makes 32 bits(4bytes) integers
number_one = numpy.ones((1, 4), dtype=numpy.int32)
print("Ones= ", number_one)

# Arange and shape functions
numbers = numpy.arange(6)
print("Numbers= ", numbers)

second_numbs = numpy.arange(4).reshape(2, 2)
print("Second= ", second_numbs)

exp = numpy.arange(3, 4, 0.2)
print("Example= ", exp)

# linspace and indices functions

exp2 = numpy.linspace(2., 5., 3)
print("Second Example= ", exp2)

exp3 = numpy.indices((4, 4))
print("Example 3= ", exp3)

# Matrix in Numpy

A = numpy.array([[1, 2], [3, 4]])
B = numpy.array([[2, 3], [4, 5]])
C = A + B
print(C)

# Multiplication
D = numpy.array([[2, 1], [0, 2], [0, 1]])
F = numpy.array([[2], [3]])
E = D.dot(F)
print("This is E")
print(E)
print()
print(D.transpose())

# Access
print(D[0])
print(D[1])
print(D[:, 0])

# Slicing
print(D[:2, :1])
