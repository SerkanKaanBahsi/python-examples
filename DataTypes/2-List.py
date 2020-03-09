list1=[1,2,3,4]
list2=[1,"a","c","d"]
list3=["OH NO",list2]
#Printing the List
print("First index = {}".format(list1[0]))
print(list1[1])
print(list2[1:3])
print(list3[0][1])
print(list3[1][2])
#With negavtive index
print(list2[-2])
print(list3[:-1])
print(list2[:])
print(list1[:-1])

#Change List
print("Methods list.append() list.extend() list.insert()")
list1[0]="a"
list1[1:4]=[4,6,8]
print(list1)

list2.append(15)

list2.extend(["b",2,5,"h"])
print(list2)

print(list1+list2)

list1.insert(1,"c")

list1[0:0]=["h","e","l"]
print(list1)

#Deleting from list
print("Methods del list[] list.remove() list.pop() list.clear()")
del list1[0]
print(list1)
del list1[0:5]
print(list1)
#del list1
#print(list1)

list2.remove("d")

print(list2.pop())
print(list2.pop(0))
print(list2)

#list2.clear()
#print(list2)
#print(list3)

list2[2:-3]=[]
print(list2)

#List Comprehension
#List comprehension is an elegant and concise way to create new list from an existing list in Python.
half=[y/2 for y in range(15)]
print(half)
half2=[int(y/2) for y in range(15) if y%2==0]
print(half2)
sentence=([x+y for x in ["Going to ","Coming from "] for y in ["School","House"]])
print(sentence)

#Membership
print("School" in sentence)
print("Going to School" in sentence)

#Methods in general
print("We already used append(),extend(),insert(),remove(),pop(),clear()")
print("Now we are going to use index(),count(),sort(),reverse(),copy()")
list_ex=[1,2,2,4,4,8,8,1,"a","a"]
print("İndex")
print(list_ex.index(1))

print("Count")
print(list_ex.count("a"))

print("Sort")
print(list_ex.sort())

print("Reverse")
print(list_ex.reverse())

list_ex2=[]
print("Copy list 1 to list 2")
print("First List" ,list_ex)
print("Second List" ,list_ex2)
list_ex2 = list_ex.copy()
print("Second List" ,list_ex2)

#Why should we use copy if we use normal
#list_ex2=list_ex when we change the elements of first or the second list
#It will effect both of the list but we can also copy with slicing
#list_ex2=list_ex[:]

