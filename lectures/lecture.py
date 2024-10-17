text1 = "welcome to world of programming"
print(text1.split())

text2 = "one:two:three"
print(text2.split(','))

text2 = "one, two, three"
print(text2.split(','))

text3 = "CatBatSatFatOr"
print(text3.split('t'))

print("")
print("---------------")
print("")

word = 'welcome to world of programming'
print(word.split(' ', 0))

print(word.split(' ', 4))

print(word.split(' ', 1))

print(word.split(',', 1))

print("")
print("---------------")
print("")


word = 'Welcome to, programming'
print(word.rsplit(',', 1))

word = "Welcome@toprogramming@world"
print(word.rsplit('@', 1))

word = "Welcome@to@programming@world"
print(word.rsplit('@', -1))

string = "tic-tac-toe"
print(string.rsplit('-', 1))

print("")
print("-----partition-----")
print("")

string = "Light attracts bug"
print(string.partition('attracts'))

string = "gold is heavy"
print(string.partition('is'))

print("")
print("-----join-----")
print("")

str = '-'.join('hello')
print(str)

list1 = ['AA', 'BB', 'CC', 'DD']
print("".join(list1))

t1 = ('1', '2', '3', '4')
print('-'.join(t1))


list1 = {'1', '2', '3', '4', '4'}
print("*".join(t1))

Fuel_Type = {'Petrol': 1, 'Diesel': 2, 'CNG': 3}
print("-*-".join(Fuel_Type))

print("")
print("-----Functions-----")
print("")

def add_func(n1,n2):
    return n1+n2

print(add_func(10,20))

def add_func2(n1,n2):
    sum = n1+n2
    return sum

print(add_func2(10,20))

def even_odd(n):
    if n%2 == 0:
        print(n, "is Even Number")
    else:
        print(n, "is Odd Number")

even_odd(10)
even_odd(11)

def fact(num):
    result = 1
    while num >= 1:
        result *= num
        num -= 1
    return result

print(fact(5))

for i in range(1,5):
    print("The factorial of ", i, "is", fact(i))

def sum_sub(a,b):
    add = a+b
    sub = a-b
    return add, sub

result = sum_sub(100,50)
print(result)

x,y = sum_sub(100,50)
print("The sum is :", x)
print("The sub is :", y)

print("")
print("-----positional arguments-----")
print("")

def greet(name, msg):
    '''This function greets to the person with the provided message'''
    print("Hello", name, msg)

greet("Monica", "Good Morning!")
greet("Ross", "How are you?")

def markst(subject, marks):
    '''show marks along with subject'''
    print("Subject is %s and marks are %d" %(subject, marks))

markst("Maths", 87)

def greet(name, msg="Good Morning!"):
    '''This function greets to the person with the provided message'''
    print("Hello", name, msg)

greet(name="Ravi", msg="Good Morning!")
greet(msg="Good morning!", name = "Ravi")

def greet(name="Sarita", msg="Good day"):
    '''The function greets the person with the help of a message'''
    print("Hello", name, msg)

greet(name="Ravi",msg="Good morning!")
greet(msg="Good morning!", name="Ravi" )

def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(add(1,2,3,4,5))
print(add(10))
print(add())
print(add(10,20))
print(add(10,20,30))
print(add(10,20,30,40))



def func_kwargs(**kwargs):
    print("\n Data type of argument :", type(kwargs))

    for key, value in kwargs.items():
        print("{} is {} ".format(key,value))

func_kwargs(name="John", age=25, city="New York")
func_kwargs(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=191432657)


print("")
print("-----List-----")
print("")

#creating a empty list

list1 = []
print(list1)
print(type(list1))

#creating a list
l1 = [10,20,"Ram","Hari",40.5,46.5,38.5,42.5]
print(l1)
print(type(l1))

#using dynamic input

l1 = eval(input("Enter the list: "))
print(l1)
print(type(l1))

#creating a list with range using list function

l1 = list(range(0,10,2))
print(l1)
print(type(l1))

#creating a list from string

s1 = "Python Programming"
l1 = list(s1)
print(l1)

#creating a list from string using split method

s1 = "Python Programming"
l1 = s1.split()
print(l1)
print(type(l1))

#Accessing lists
#indexing a list positive indexing

emp_name = ["Ram", "John", "Sam"]
print(emp_name[0])
print(emp_name[1])
print(emp_name[2])

#negative indexing

print(emp_name[-1])
print(emp_name[-2])
print(emp_name[-3])

#nested list
id = [1,2,3]
emp_name = ["Ram", "John", "Sam"]
num_emp = 3
emp_list = [id, emp_name, num_emp]

#accessing nested list

print(emp_list[0])
print(emp_list[1])
print(emp_list[2])

#accessing nested list using negative indexing

print(emp_list[-1])
print(emp_list[-2])
print(emp_list[-3])


#access list condition
ls3 = [10,20,30,40,50,60,70,80,90]
print(ls3)
print(ls3[1])

print(ls3[1:5])
print(ls3[1:7:2])
print(ls3[:])

print(ls3[3:40])
print(ls3)
print(ls3[-4:-1:1])
print(ls3[-5:-20:-1])

#viewing nested list
print(emp_list)

#acessing elements of nested list

print(emp_list[0])
print(emp_list[1][0])
print(emp_list[1][0].title() + " is the best employee")

#accessing elements using postive indexing

print(emp_list[0][1])
print(emp_list[1][1])
print(emp_list[2][1])

#accessing elements using negative indexing

print(emp_list[-1][-1])
print(emp_list[-2][-1])
print(emp_list[-3][-1])

#traversing a list

ls3 = [10,20,30,40,50,60,70,80,90]
i=0
while i<len(ls3):
    print(ls3[i])
    i+=1

ls3 = [10,20,30,40,50,60,70,80,90]
for i in ls3:
    print(i)

l = ["A","B","C"]
x=len(l)
for i in range(x):
    print(l[i], "is available at positive index: ", i, "and at negative index: ", i-x)

#modify components of list
id = [1,2,3]
emp_name = ["Ram", "John", "Sam"]
num_emp = 3
emp_list = [id, emp_name, num_emp]
print(emp_list)
emp_list[2] = 2
emp_list[1][1] = 'Karan'
print(emp_list)
emp_list[1][0:2] = ["Hari","Geeta"]
print(emp_list)

#adding elements to list

ls3 = [10,20,30,40,50,60,70,80,90]
ls3.append(100)
print(ls3)

list2=[]
for i in range(101):
    if i%10==0:
        list2.append(i)
print(list2)

#adding tuple to list
list1 = [1,2,3]
list1.append(5,6)
print("\nList after addition of a tuple: ", list1)


#adding list to list
list3 = ['abc','def']
list1.append(list3)
print("\nList after addition of a list: ", list1)

#appending elements to the end of the nested list

emp_list = [[1,2,3], ['Ram','John','Sam'], 3]
print("Original nested list: ", emp_list)
emp_list[0].append(4)
print("After adding 4 to the nested list: ", emp_list)
emp_list[1].append('Nirmal')
print("After adding Nirmal to the nested list: ", emp_list)
emp_list.append([27,32,44,35])
print("After adding [27,32,44,35] to the nested list: ", emp_list)

#interesting element into list

ls3 = [10,20,30,40,50,60,70,80,90]
ls3.insert(2,100)
print(ls3)
ls3.insert(100,200)
print(ls3)
ls3.insert(-10,300)
print(ls3)

#interestin tuple 45,55 at index 1

ls3 = [10,20,30,40,50,60,70,80,90]
tup1 = (45,55)
ls3.insert(1,tup1)
print(ls3)

#interesting list [11,22] at index 3

ls3 = [10,20,30,40,50,60,70,80,90]
ls2 = [11,22]
ls3.insert(3,ls2)
print(ls3)

#extend method
list = [1,2,3,4]
print("Initial list: ", list)
list.extend(8,'abc','def')
print("List after extend: ", list)

#extend in nested list

print(emp_list)
emp_list[0].extend([102,103,104])
print(emp_list)


#removing elements from list

motorcylce = ['honda','yamaha','suzuki','hero']
print(motorcylce)
del motorcylce[0]
print(motorcylce)
del motorcylce[1:3]
print(motorcylce)
del motorcylce

#del removing elements from list 
id = [1,2,3,4,5]
emp_name = ['Ram','John','Sam',"Gitaq","Hari"]
num_emp = 5
age=[25,35,45,55,50]
emp_list = [id, emp_name, num_emp, age]
print(emp_list)
del emp_list[3]
print(emp_list)
del emp_list[1:3]
print(emp_list)

#remove using pop
motorcylce = ['honda','yamaha','suzuki','hero']
print(motorcylce)
motorcylce.pop(1)
print(motorcylce)
motorcylce.pop()
print(motorcylce)
motorcylce.pop(-1)
print(motorcylce)


#remove method
motorcylce = ['honda','yamaha','suzuki','hero','ducati']
print(motorcylce)
motorcylce.remove('suzuki')
print(motorcylce)

#clear method
n=[10,20,30,40]
print(n)
n.clear()
print(n)

#organizing list

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

n = [10,5,15,10,30]
n.sort()
print(n)

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

cars = ['bmw','audi','toyota','subaru']
print("Here is the original list: ", cars)

#sorted()
cars = ['bmw', 'audi','toyota','subaru']
print("Here is original list: ", cars)
print("Here is the sorted list: ", sorted(cars))
print("Here is the reverse sorted list: ", sorted(cars, reverse=True))


#reverse()

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)


#len()
ls1 = [10,20,30,40,50,40,30,50,20,40,50,30]
print(len(ls1))

#list aliasing
ls1=[1,2,3,4]
ls2=ls1
print(id(ls1))
print(id(ls1))
ls1[1]=55
ls2[2]=66
print(ls1)
print(ls2)

#copying list 
ls1 = [1,2,3,4]
ls2 = ls1[:]
ls1[1]=55
ls2[2]=66
print(ls1)
print(ls2)

#using copy()
ls1=[1,2,3,4]
ls2=ls1.copy()
ls1[1]=55
ls2[2]=66
print(ls1)
print(ls2)

#using list()
ls1=[1,2,3,4]
ls2=list(ls1)
ls1[1]=55
ls2[2]=66
print(ls1)
print(ls2)

#min(), max(), sum()
digits = [1,2,3,4,5,6,7,8,9]
print(min(digits))
print(max(digits))
print(sum(digits))

#index() and count()
print(ls1.index(40))
print(60 in ls1)
print(ls1.count(30))

#concatenation and repetition
ls1 = [10,20,30]
ls2 = ['a','b','c']
ls3 = ls1 + ls2
print(ls3)

#repetition
x = [10,20]
y = x * 3
print(y)

#comparing list objects
x = ["AAA", 20, "CCC", 30]
y = ["AAA", 20, "CCC", 30]
z = ["BBB", 20, "CCC", 30]
print(x==y)
print(x==z)
print(x!=z) 

#membership operator
n = [10,20,30,40]
print(10 in n)
print(10 not in n)
print(50 in n)
print(50 not in n)

#list comprehension

m = [x for x in range(5,50) if x%2 != 0]
print(m)

squares = [value**2 for value in range(1,11)]
print(squares)

list2 = [x for x in range(10) if x < 5]
print(list2)

#calculate squares of numbers from 1 to 10 using loop
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#ex 1 and 2 
v=[2**x for x in range(1,6)]
print(v)

#ex 2
m = [x for x in range(21)  if x%2==0]
print(m)

#ex 1 and 2 

words = ["Mumbai", "Chennai", "Kolkatta", "Delhi"]
words_len = [len(word) for word in words]
print(words_len)

#ex2 
num1 = [10,20,30,40]
num2= [30,40,50,60]
num3= [ i for i in num1 if i not in num2]
print(num3)

#combines two lists
[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

#nested loop 
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
print(combs)

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












