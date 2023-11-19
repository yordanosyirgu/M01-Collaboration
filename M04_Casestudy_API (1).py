# Yordanos Yirgu
# Module 4 Case study APIs

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy book data (for testing purposes)
books = [
    {"id": 1, "book_name": "Book 1", "author": "Author 1", "publisher": "Publisher 1"},
    {"id": 2, "book_name": "Book 2", "author": "Author 2", "publisher": "Publisher 2"},
    {"id": 3, "book_name": "Book 3", "author": "Author 3", "publisher": "Publisher 3"},
    {"id": 4, "book_name": "Book 4", "author": "Author 4", "publisher": "Publisher 4"},
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'book_name': request.json['book_name'],
        'author': request.json['author'],
        'publisher': request.json['publisher']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book['book_name'] = request.json.get('book_name', book['book_name'])
        book['author'] = request.json.get('author', book['author'])
        book['publisher'] = request.json.get('publisher', book['publisher'])
        return jsonify(book)
    return jsonify({'error': 'Book not found'}), 404

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

if __name__ == '__main__':
    app.run(debug=True)