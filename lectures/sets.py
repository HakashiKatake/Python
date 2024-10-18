print("")
print("---Sets-----")
print("")


#set example of update

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set1.update(set2)
print(set1)

#set add example

set1 = {1,2,3,4,5}
set1.add(6)
print(set1)

#set copy example

set1 = {1,2,3,4,5}
set2 = set1.copy()
print(set2)

#set pop example

set1 = {1,2,3,4,5}
print(set1.pop())
print(set1)

#set remove example

set1 = {1,2,3,4,5}
set1.remove(2)
print(set1)

#set discard example

set1 = {1,2,3,4,5}
set1.discard(2)
print(set1)

#set clear example

set1 = {1,2,3,4,5}
set1.clear()
print(set1)

#set union example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.union(set2)
print(set3)

#set intersection example   

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.intersection(set2)
print(set3)

#set difference example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.difference(set2)
print(set3)

#set symmetric difference example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
set3 = set1.symmetric_difference(set2)
print(set3)

#set issubset example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}  
print(set1.issubset(set2))

#set issuperset example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}  
print(set1.issuperset(set2))    

#set isdisjoint example

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}  
print(set1.isdisjoint(set2))

#how to input set from user

#set1 = set(input("Enter the set: "))
#print(set1) 

#set comprehension example

set1 = {x for x in range(1,11)}
print(set1)


#set comprehension example with condition

set1 = {x for x in range(1,11) if x%2 == 0}
print(set1)