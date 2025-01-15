
class Counter:
    count = 0
    
    @classmethod
    def increment(cls):
        cls.count += 1
        
    @staticmethod
    def display():
        print("Count is", Counter.count)

Counter.display()

Counter.increment()
Counter.display()
