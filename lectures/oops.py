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
        self.name = name
    def print_name(self):
        print(self.name)
obj = simple('John')
obj.print_name()


#ex init method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
   

p1 = Person('John', 25)
print(p1.name)
print(p1.age)


