slice=lambda x:x/2
print(slice(10))

#Way to find upcase letters in a text
text=["S","K","M","a","c","z","k"]
new_text=list(filter(lambda x: (x < "a"),text))
print(new_text)

number=[1,1,1,1,1,1,0,0,1,1,1,0,0,0,1,0,1]
new=list(map(lambda x: (x*0),number))
print(new)
