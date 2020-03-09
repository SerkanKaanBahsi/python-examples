#Tuples are immutable objects
print(tuple.__doc__)


print("\n")

tuple=("Serkan",12,5.3,"Hello",1+2j)
tuple2=("Basic",3)
print(tuple)
print(tuple2)

print(tuple[2:])
print(tuple[2:4])

#Appending
tuple2=tuple+tuple2
print(tuple2)
