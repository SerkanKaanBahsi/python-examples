#Its like a list but we cannot change the elements

#Creating Tuples

empty=()
normal_tuple=(1,2,3,4)
nested=(1,"Hi","OH NO",5,67,12)

#Without () but its kinda harder to read
other_tuple=1,2,"Hi"

#One element
one_tup=("Hi")
real_tup=("Hi",)
print(type(one_tup))
print(type(real_tup))

#Unpacking
tp=(1,"a",2,"name")
x,y,z,m=tp
print(x,y,z,m)

#Print time normal and slice
print(empty)
print(normal_tuple)
print(nested)
print(other_tuple)

print(nested[0])
print(nested[2][1])
print(real_tup[0])
print(real_tup[0][0])

print(nested[2:5])

#Negative

print(nested[-1])
print(nested[-4:-1])

#Changing Elements 

the_tuple=(1,2,3,["a","b","c"])
#the_tuple[0]=2 we cant do this but we can change the list inside the tuple
the_tuple[3][1]="Hello"
print(the_tuple)
#Or we can change the tuple completely
the_tuple=("c","h","a","n","g","e")
print(the_tuple)

#Deleting
#We cant delete only one element but we can delete the tuple
gone_tuple=(1,2,3)
print(gone_tuple)
del gone_tuple
#print(gone_tuple)

#Methods
print("METHODS")
# count and index
op_tuple=(1,2,2,3,4,4,5,1,1)
print(op_tuple.count(1))

#index
print(op_tuple.index(4))

#Membership
print(1 in op_tuple)
print(2 not in op_tuple)



