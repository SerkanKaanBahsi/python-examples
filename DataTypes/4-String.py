#In Python, string is a sequence of Unicode character.

#Creating
str_1="Oh No"
str_2='OH NO'
str_3="""OH NO 
      OH MY GOD"""
print(str_1)
print(str_2)
print(str_3)

#Indexing
work_str="My Name"
print("Str =" ,work_str)
print("Str[1] =" ,work_str[1])
print("Str[1:4] =" ,work_str[1:4])

print("Str[-1] =" ,work_str[-1])

#Change and Delete

work_str="Hello"
print(work_str)
del work_str
#print(work_str)

#String Operations

print(str_1 + str_2)
print(str_1*4)
print("Hi" "Friend")

for letter in str_2:
    print(letter)

print("OH" in str_2)
print("Oh" in str_2)

#Built in Functions
the_list=list(enumerate(str_2))
print(the_list)
print(len(str_2))

#String Formating
#Escape Sequance

print("""Gandalf said, "Fly you fools" """)
print('Aragorn said, "For Frodo\"')
print('He said, "What\'s there?"')
print("Gandalf said, \"Fly you fools\"")

print("This \
is \
ignored")
print("Hello \n Welcome")

print("When u need a \\")

print("\'")
print("\"")
#print("\a")
print("What \b who")
print("What \f who")
#Formating (Open a new .py for this)

basic="{} is the first and {}, {} comes".format("Plane","Ship","Car")
print(basic)

new_basic="{1},{2},{0}".format("Hello","Hey","Hi")
print(new_basic)
with_basic="{name},{price},{date}".format(name="Pizza",price=12,date="12/10/2019")
print(with_basic)

print("{0:b} is the binary version of {0}".format(128))
print("5/12 is {0:f}".format(5/12))