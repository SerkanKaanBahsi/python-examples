#Arguments get wrapped up into a tuple before being passed into the function

def AllAboard(*mates):
    for mate in mates:
        print(mate)
def WithKeys(**kwargs):
    for key,door in kwargs.items():
        print("Key= ",key , door , "Door")


name=123
AllAboard("Jon","Lisa","Bell",name)
WithKeys(first=1,second=2,third=3)
#TO DO SEARCH **kwagss
