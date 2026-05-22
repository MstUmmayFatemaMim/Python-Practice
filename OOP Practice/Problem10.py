#########   10. Composition — Library system // Create a Book class and a Library class.
######## Library should hold a list of Books and have methods add_book(), remove_book(), and find_by_author().

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        print("**********   Added books   **********")
        self.books.append(book)
        print(f"Added {book.title} by {book.author}")
        return book  # Returns the book object

    def remove_book(self, book):
        print("**********   Remove books   **********")
        for book in self.books:
            if book in self.books:
                self.books.remove(book)
                print(f"Removed {book.title}")
        return book

    def show_books(self):
        print("**********   Showing all books   **********")
        for book in self.books:
            print(f"{book.title} is written by {book.author}")

    def find_by_author(self, author):
        print("**********   Finding books by author   **********")
        for book in self.books:
            if book.author == author:
                print(f"{book.title} is written by {book.author}")
                return book
        print(f"Any book is not written by {author}")
        return None


# 1. Create the library instance
my_library = Library()

# 2. Create a Book instance with title and author
# new_book = Book("Python 202", "John Doe")
# new_book1 = Book("Python 203", "John Down")

# 3. Add the book object to the library
my_library.add_book(Book("C#","Fahad"))
my_library.add_book(Book("Python","John"))
my_library.add_book(Book("Java","Jovan"))
# 4. Call methods and see the output
# print(f"Added Book: {added_book.title} by {added_book.author}")
my_library.show_books()

my_library.remove_book("Python")
# print(f"Removed Book: {removed_book.title} ")

my_library.find_by_author("John Doe")
