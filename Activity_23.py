
list = ['banana','oranges','raspberry','grapes','strawberry']
list.append('blackberry')  #adds item
print(list)
list.pop() #deletes item from the list
print(list)
list.insert(0,'pineapple')  #adds item to the specific position
print(list)
for i in list:
    print(f"{i} in the list")

peace = 'Glenn Russel Tiangco'
for g in peace:
    print(g)
print("\nReversed\n")
for r in peace[::-1]:
    print(r)
