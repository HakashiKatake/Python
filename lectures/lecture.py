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








