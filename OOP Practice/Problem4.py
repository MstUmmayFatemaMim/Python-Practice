########    4. Counter class // Build a Counter class that starts at 0.
# ######## Add increment(), decrement(), and reset() methods, and a get_count() method.
class Counter:
    def __init__(self,count):
        self.count = 0

    def get_count(self):
        return self.count

    def increment(self):
        self.count += 1
        print(f"Increment : {self.count}")

    def decrement(self):
        self.count -= 1
        print(f"Decrement : {self.count}")

    def reset(self):
        self.count = 0
        print(f"Reset : {self.count}")

x=Counter(100)
print(x.get_count())

x.increment()
print(x.get_count())
x.decrement()
print(x.get_count())
x.reset()
print(x.get_count())

