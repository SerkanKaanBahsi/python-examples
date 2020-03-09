#Python dictionary is an unordered collection of items. 
#While other compound data types have only value as an element, a dictionary has a key: value pair.

#Creating Dictionary
#Values can be of any data type and can repeat, keys must be of immutable type (string, number or tuple with immutable elements) and must be unique.
print("--------------------- "+"Creating Dictionaries"+" -----------------------------")
first_dict={1:"Name",2:"Last Name"}
try_dict={(1,2):"Name",("a",3):"Last Name"}
func_dict=dict({"name":"Arthur",2:"King"})
dif_dict=dict([(3,12),(4,45)])

#Accessing Elements
print("----------------------------- " +"Accessing Elements"+" ---------------------------")
print(first_dict[2])
print(try_dict[(1,2)])
#get()
print(func_dict.get("name"))
print(first_dict.get(4))

#Adding and Changing Elements
print("------------------------- "+"Adding and Changing Elements "+"-------------------------")
first_dict[0]="Age"
print(first_dict)
first_dict[2]="Second Name"
print(first_dict)

#Deleting and Removing Elements
print("-------------------------- "+"Deleting and Removing Elements "+"------------------------")
#pop(), popitem()(raises KEYERROR if empty), clear(), del
numbers_dict={1:1.1,2:2.2,3:3.3,4:4.4,5:5.5}
print(numbers_dict.pop(2))
print(numbers_dict)
print(numbers_dict.popitem())
print(numbers_dict)
del numbers_dict[4]
print(numbers_dict)
numbers_dict.clear()
print(numbers_dict)
del numbers_dict
#print(numbers_dict) throws Error

#Dictionary Methods
print("---------------------- "+"Methods"+" -----------------------")
#fromkeys()
value=["a","b"]
face={1,2,3,4,5,6,7}
end=dict.fromkeys(face)
print(end)
end=dict.fromkeys(face,12)
print(end)
end=dict.fromkeys(face,value)
print(end)
value.append("cd")
print(end)
end=dict.fromkeys(try_dict)
print(end)
#get() gets the value of the key if the key does not exist return the value get(key,[value]) or none
print(first_dict.get(5,[12]))
#Items() prints the items in the list
print(first_dict.items())
#Keys() prints the keys
print(first_dict.keys())
#setDefault(key,[d]) If key is in the dictionary, return its value. If not, insert key with a value of d and return d
print(first_dict.setdefault(3,"Hello"))
print(first_dict)
#update() Update the dictionary with the key/value pairs from other, overwriting existing keys.
x={1:"Updated"}
first_dict.update(x)
print(first_dict)
x={2:"New"}
first_dict.update(x)
print(first_dict)
#Values()
print(first_dict.values())
