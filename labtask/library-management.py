class Book:
    def __init__(self, isbn, title, author, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.quantity = quantity
        self.available_quantity = quantity


class Member:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.max_books = 3
        self.borrowed_books = []


class Library:
    def __init__(self, name):
        self.name = name
        self.books = {}      # {isbn : Book object}
        self.members = {}    # {member_id : Member object}

def add_book(self, book):
# -- book is objecet of BOOK class 
    if book.isbn in self.books:
        self.books[book.isbn].quantity += book.quantity
        self.books[book.isbn].available_quantity += book.quantity
    else:
        self.books[book.isbn] = book

# -- Remove Book 
def removeBook(self,book):
    if book.isbn in self.books:
        if self.books[book.isbn].quantity < book.quantity:
            print("Itni copies available nahi hain!")
            return
        self.books[book.isbn].quantity -= book.quantity
        self.books[book.isbn].available_quantity -= book.quantity
    else :
        print("Book not exist \n")
# -- regiester member 

def registerMember(self, member):

    if member.id in self.members:
        print("Member already registered")

    else:
        self.members[member.id] = member
        print("Member registered successfully")