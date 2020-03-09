#A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable
#However, the set itself is mutable. We can add or remove items from it.
#Sets can be used to perform mathematical set operations like union, intersection, symmetric difference etc.
#Set cant have mutable elements like list, set, dictionary.
#Set does not support indexing

#Creating Set

first_set={"S",1,2,3,"A"}
print(first_set)

exp_set={1,1,1,1,1,1,}
print(exp_set)

empty_set={}
print(type(empty_set))
empty_set=set()
print(type(empty_set))

#Changing a Set
#add() single element - update() multiple elements

first_set.add(4)
print(first_set)

first_set.add("S")
print(first_set)

first_set.update([1,"A",3,5])
print(first_set)

first_set.update([1,2,3], {4,5,6,"A"}, "Hello")
print(first_set)

#Deleting elements
#remove() - discard() - remove raises an exception if the element does not exist

exp_set.discard(1)
print(exp_set)
#Exception
#exp_set.remove(1)

#Random element
print(first_set.pop())
first_set.clear()
print(first_set)

#SET OPERATIONS *************************
#Sets can be used to carry out mathematical set operations like union, intersection, difference and symmetric difference
A={1,2,3,4,5,6,"a","b","c"}
B={3.2,4,5,"a","d","f"}
print("A = " ,A)
print("B = " ,B)
#Union
#Operator "|" -- Method union()
print("--------------- " + "Printing Union " + " ---------------------")
print(A | B)
print(B.union(A))

#Intersection
#Operator "&" -- Method intersection()
print("--------------- " + "Printing Intersection " + " ---------------------")
print(A & B)
print(B.intersection(A))
print(A.intersection(B))

#Difference
#Operator "-" -- Method difference()
print("--------------- " + "Printing Difference " + " ---------------------")
print(A-B)
print(B-A)
print(B.difference(A))
print(A.difference(B))

#Symmetric Difference
#Operator "^" -- Method symmetric_difference()
print("--------------- " + "Printing Symmetric Difference " + " ---------------------")
print(A ^ B)
print(B.symmetric_difference(A))
print(A.symmetric_difference(B))


#SET METHODS 
print("----------------- " + "Different Methods " + "---------------------")
#Copy
A={1,2,3,4,5,6}
B={2,3,4,7,8,9}
C={3,10,11,12,13}
D=set()
D=A.copy()
print(D)
#Difference Update 
result=A.difference_update(B)
print(A)
#Intersection Update
result=C.intersection_update(B,D)
print(C)
#IsDisjoint
print(A.isdisjoint(B))
#Issubset
print(A.issubset(D))
#IssuperSet
print(D.issuperset(A))
#Symmetric Difference Update
result=D.symmetric_difference_update(B)
print(D)

#Other Set Operations
print("---------------------- " + "Other Operatiosn " +"--------------------------")
#Membership
print(2 in B)
#Built in Functions
print("----------------------- " + "Built in Functions " + "--------------------------")
#All()
print(all(B))
#Any()
just_set={0,1,0,0}
print(any(just_set))
#Enumerate
name_set={"S","e","r","k","a","n","Kaan"}
my_enum=enumerate(name_set)
print(list(my_enum))
#len()
print(len(just_set))
#max()
print(max(B))
#min()
print(min(B))
#sorted()
new_list=sorted(name_set)
print(new_list)
#sum()
print(sum(just_set))

#Frozenset is a new class that has the characteristics of a set, but its elements cannot be changed once assigned. 
#While tuples are immutable lists, frozensets are immutable sets.

#Sets being mutable are unhashable, so they can't be used as dictionary keys. 
#On the other hand, frozensets are hashable and can be used as keys to a dictionary.

#Creating

Ice=frozenset(["A",1,2,0,"ssac",3.3,(5,4)])
print(Ice)
#This datatype supports methods like: 
#copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union()




