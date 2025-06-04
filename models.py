from app import Flask, request, jsonify 
import requests

class User:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def get_name(self):
        return self.name 
    
    def set_name(self, name):
        self.name = name 
        
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

class Book:
    def __init__(self, title, author, is_available = True):
        self.title = title 
        self.author = author 
        self.is_available = is_available

    def get_author(self):
        return self.author
    
    def get_title(self):
        return self.title 
    
    def get_isAvailable(self):
        return self.is_available
    
    def set_isAvailable(self, status):
        self.is_available = status

class Library:
    def __init__(self,name):
        self.name = name
        self.booksL = []

    def add_book_toLibrary(self, book):
        self.booksL.append(book)
        return True

    def get_name(self):
        return self.name
    
    def get_book(self, reader_name, book_title):
        for user in users:
            if user.get_name() == reader_name:
                for book in self.booksL:
                    if book.get_title() == book_title:
                        book.set_isAvailable(False)
                        return True
                   
    def see_books(self):
        return self.booksL

app = Flask(__name__)
users = []
libraries = []
books = []

# DO NOT include this in models.py
# if __name__ == '__main__':
#     app.run(debug=True)









