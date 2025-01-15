
class Encapsulation:
    def __init__(self):
        self.__privateAttribute = 10

    def getPrivateAttribute(self):
        return self.__privateAttribute

    def setPrivateAttribute(self, value):
        self.__privateAttribute = value

encapsulation = Encapsulation()
print(encapsulation.getPrivateAttribute())