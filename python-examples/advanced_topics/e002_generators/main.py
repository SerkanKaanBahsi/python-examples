#Python generators are a simple way of creating iterators

#A generator that reverses a list

def reverse(my_list):
    lenght = len(my_list)
    for i in range(lenght-1,-1,-1):
        yield my_list[i]

print("---------Reverse List----------")
for element in reverse([1,2,3,4]):
    print(element)

#Generator Expression
print("---------Generator Expression---------")

my_list = [1,2,3,4]

my_listcomp = [x+2 for x in my_list]
print(my_listcomp)
my_generator = (x+2 for x in my_list) 

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
#Generates Error "StopIteration"
#(next(my_generator))

#We can also use them with functions

print(sum(x+2 for x in my_list))

"""Why use them: They are easy to implement, memory efficient,
represent infinite stream(in theory), can be pipelined"""

