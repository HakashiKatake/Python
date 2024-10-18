#defining a class

class First:
    pass

f = First()
#Ex class

class Dog:
    def eat(self):
        print('Eating')
d=Dog()
d.eat()

#self variable

class Dog:
    def eat(self):
        print('Eating')
d=Dog()
d.eat()
Dog.eat(d)


#__init__ method

class simple:
    def __init__(self,name):
        print("Initializing")
    def pr(self):
        print("Sample class")
        
obj = simple()
obj.pr()

#Constructor

class simple:
    def __init__(self,name):
        print("Initializing")
    def pr(self):
        print("Sample class")
        
obj = simple()
obj = simple()
obj.pr()




#ex init method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
   

p1 = Person('John', 25)
print(p1.name)
print(p1.age)


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
p1 = Person('John', 25)
p2 = Person('Marie', 22)

print(p1.name)
print(p1.age)



