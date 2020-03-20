# Iterator in Python is simply an object that can be iterated upon. 
#An object which will return data, one element at a time.

#An object is called iterable if we can get an iterator from it.

class PowThree:
    """Class to implement an iterator 
    of powers of three"""

    def __init__(self, number = 0):
        self.number = number
    
    
    def __iter__(self):
        self.value = 0
        return self
    
    def __next__(self):
        if self.value <= self.number:
            result = 3 ** self.value
            self.value += 1
            return result
        else:
            raise StopIteration


class ToInf:
    """Inf iterator that returns
    the powers of two"""
    def __iter__(self):
        self.value = 0
        return self
#Dont forget to include a termimation condition    
    def __next__(self):
        if self.value <= 10:
            result = 2** self.value
            self.value +=1
            return result
        else:
            raise StopIteration
    

#Function that just returns one  
def retOne():
    return 1


list_to_iter = [1,2,3,5,7,9]

iter_to_test= iter(list_to_iter)

print(next(iter_to_test))

print(iter_to_test.__next__()) 

#This will raise an error if no items left
print(next(iter_to_test))

#Building your own iteration in Pyhton

print("--------Printing powers of three--------")
for i in PowThree(4):
    print(i)
    
#Infinite Iterators

not_finite = iter(retOne,2)

print(next(not_finite)) 

pow_two = iter(ToInf())


print("-------Printing powers of two-------")

print(next(pow_two))
print(next(pow_two))
print(next(pow_two))
print(next(pow_two))
print(next(pow_two))
print(next(pow_two))
   
    