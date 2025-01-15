                                                 
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):

    def speak(self):
        print("Woof!")

dog = Dog()
dog.speak()
