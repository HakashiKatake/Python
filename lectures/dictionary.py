print("")
print("-----Dictionary-----")
print("")


d = dict(A="jack", B="jill")
print(d)


d = {100: "Jack", 200: "Jill"}
print(d)

print(d.get(100))

#deleting elements from dictonary

d = {100: "Jack", 200: "Jill"}
del d[100]
print(d)

#clear method & del method


d = {100: "Jack", 200: "Jill"}
d.clear()
print(d)

#copy method

d = {100: "Jack", 200: "Jill"}
d2 = d.copy()
print(d2)

#pop method

d = {100: "Jack", 200: "Jill"}
d.pop(100)
print(d)

#popitem method

d = {100: "Jack", 200: "Jill"}
d.popitem()
print(d)

#keys() method

d = {100: "Jack", 200: "Jill"}
print(d.keys())

#values() method

d = {100: "Jack", 200: "Jill"}
print(d.values())


#items() method

d = {100: "Jack", 200: "Jill"}
print(d.items())

#update() method

d = {100: "Jack", 200: "Jill"}
d.update({300: "John"})
print(d)

#fromkeys() method

keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = dict.fromkeys(keys, value)
print(vowels)

#dictinoary comprehension instead of fromkeys()

keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'
vowels = {key: value for key in keys}
print(vowels)

#setdefault() method

person = {'name': 'Phill', 'age': 22}
age = person.setdefault('age')
print('person = ',person)
print('age = ',age)

#nested disctionary 

people = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'}}

print([people[1]['name']])
print(people[2]['age'])


#add elementt to a nested list dicionary 

people = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'}}

print(people)
people[3] = {}
people[3]['name'] = 'Luna'
people[3]['age'] = 24
people[3]['married'] = 'No'
print(people)

#delete elements from a nested dictionary 

people = {1: {'name': 'John', 'age': '27'},
          2: {'name': 'Marie', 'age': '22'},
          3: {'name': 'Peter', 'age': '29', 'married': 'Yes'}}

del people[3]['married']
print(people)


#dictionary comprehension

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value * dollar_to_pound for (item, value) in old_price.items()}
print(new_price)














