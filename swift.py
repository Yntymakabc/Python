class Book():
    def __init__(self, title):
        self.title = title
        self.isAvailable = True
        self.borrowedBy = None

    def getTitle(self):
        return self.title
    
    def setTitle(self,newTitle):
        self.title = newTitle

    def getIsavailable(self):
        return self.isAvailable
    
    def setIsavailable(self, status):
        self.isAvailable = status

    def setBorrowedBy(self, reader):
        self.borrowedBy = reader

class Library():
    def __init__(self):
        self.books = []

    def listAvailableBooks(self):
        return [book.getTitle() for book in self.books if book.getIsavailable() == True]
    
    def addBook(self, Book):
        self.books.append(Book)
        return f'{Book.getTitle()} was added successfully'
    
    def borrow(self, title, Student):
        for i in self.books:
            if i.getTitle() == title:
                i.setIsavailable(False)
                i.setBorrowedBy(Student.getName())
                return f'{title} was taken by student {Student.getName()} successfully'
            
    def returnBook(self, title, Student):
        for i in self.books:
            if i.getTitle() == title:
                i.setIsavailable(True)
                i.setBorrowedBy(None)
                return f'{title} was returned successfully'
            
class Student():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def borrow(self, bookTitle, Library):
        Library.borrow(bookTitle, self)

    def returnBooks(self, bookTitle, Library):
        Library.returnBook(bookTitle, self)

    
student = Student("yntymak")
library = Library()
book = Book("the subtle art of not giving a fuck")
print(library.addBook(book))
student.borrow("the subtle art of not giving a fuck", library)
student.returnBooks("the subtle art of not giving a fuck", library)
            

print(library.listAvailableBooks())