########    9. Magic methods — Book comparison //Create a Book class with title, pages.
########   Implement __eq__, __lt__, and __repr__ so books can be compared and printed nicely.
class Book:
    def __init__(self,title,pages):
        self.title = title
        self.pages = pages
    def __repr__(self):
        return f"Title: {self.title}, Pages: {self.pages}"
    def __eq__(self, other):
        return self.title == other.title
    def __lt__(self, other):
        return self.pages < other.pages

item1=Book("Python",10)
item2=Book("Python",20)
print(repr(item1))
print(item2==item1)
print(item1<item2)