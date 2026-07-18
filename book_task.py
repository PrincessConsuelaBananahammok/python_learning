class Book:
    def __init__(self, title, author, pages, is_available=True):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_available = is_available

    def borrow(self):
        if self.is_available == False:
            raise ValueError("Book is already borrowed")
        else:
            self.is_available = False
            print("You taked a book")

    def return_book(self):
        if self.is_available == True:
            raise ValueError("Book is already in library")
        else:
            self.is_available = True
            print("You returned a book")

    def reading_time(self, speed):
        if speed <= 0:
            raise ValueError("Incorect value")
        else:
            return self.pages / speed


book1 = Book("Shining", "Stephen King", 500)

print(book1.title)

print(book1.reading_time(5))

