from app import request, jsonify
from models import app, User, Book, Library, users, books, libraries

@app.route('/')
def home():
    return "hello"

@app.route('/create_user', methods = ["POST"])
def add_user():
    data = request.get_json()
    user = User(
        name = data['name'], 
        age = data['age']
    )
    users.append(user)
    return jsonify({
        'status': 'success'
    })

@app.route('/get_users', methods = ["GET"])
def get_user():
    return jsonify(
        [{'name' : user.name, 'age' : user.age }for user in users]
    )

@app.route('/create_book', methods = ["POST"])
def create_book():
    data = request.get_json()
    book = Book(
        title=data['title'], 
        author=data['author']
    )
    books.append(book)
    return jsonify({
        'message': 'success',
        'title': book.get_title(),
        'author': book.get_author(),
        'is_available': book.get_isAvailable()})

@app.route('/get_books')
def get_book():
    return jsonify(
        [{'title':book.title, 'author':book.author, 'is_available':book.is_available}for book in books]
    )

@app.route('/take_book', methods = ["POST"])
def take_book():
    data = request.get_json()
    book_title = data['book_title']
    reader_name = data['reader_name']
    library_name = data['library_name']
    for library in libraries:
        if library.get_name() == library_name:
            if library.get_book(reader_name, book_title):
                return jsonify({'status':'success',
                                    'book':book_title,
                                    'reader':reader_name,
                                    "library": library_name
                                
                                    })
                
@app.route('/return_book', methods = ["POST"])
def return_book():
    data = request.get_json()
    book_title = data["book_title"]
    library_name = data['library_name']
    for library in libraries:
        if library.get_name() == library_name:
            lib_books = library.see_books()
            for book in lib_books:
                if book.get_title() == book_title and book.get_isAvailable() == False:
                    book.set_isAvailable(True)
                    return jsonify({
                        "status":"success", 
                        "message":f'{book_title} was returned'
                        })
        
@app.route('/create_library', methods = ["POST"])
def create_library():
    data = request.get_json()
    name = data["name"]
    library = Library(name)
    libraries.append(library)
    return jsonify({
        "status":'success', 
        "message":"library was created"
    })

@app.route('/get_libraries', methods = ["GET"])
def get_libraries():
    return jsonify([{"name":library.get_name()}for library in libraries])


@app.route('/add_book_toLibrary', methods = ["POST"])
def add_book_to_library():
    data = request.get_json()
    book_title = data['book_title']
    library_name = data["library_name"]
    for library in libraries:
        if library.get_name() == library_name:
            for book in books:
                if book.get_title() == book_title:
                    if library.add_book_toLibrary(book):
                        return jsonify({
                        "status":"success", 
                        "message": f'{book_title} was added to library {library_name}'
                         })
                    
@app.route('/see_library_books', methods = ["GET"])
def see_library_books():
    library_name = request.args.get("library_name")
    for library in libraries:
        if library.get_name() == library_name:
            return jsonify([
                {
                "title":book.get_title(), 
                "author":book.get_author(),
                "is_available":book.get_isAvailable()} for book in library.see_books()])






# This should stay in routes.py
if __name__ == '__main__':
    app.run(debug=True)