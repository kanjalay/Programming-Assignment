# tests.py
from operations import add_book, add_member, borrow_book, return_book, delete_book

def test_add_book():
    books = {}
    result = add_book(books, "12345", "Abiku", "Wole soyinka", "Non-Fiction", 3)
    assert "12345" in books
    assert result["title"] == "Abiku"

def test_add_duplicate_book():
    books = {"12345": {"title": "Abiku", "author": "wole soyinka", "genre": "Non-Fiction", "total_copies": 3, "available": 3}}
    result = add_book(books, "12345", "Abiku", "wole soyinka", "Non-Fiction", 3)
    assert result == "Book with this ISBN already exists."

def test_add_member():
    members = []
    result = add_member(members, 1, "kanja sesay", "sesaykanja2@gmail.com")
    assert len(members) == 1
    assert members[0]["name"] == "kanja"

def test_borrow_book():
    books = {"12345": {"title": "Abiku", "author": "Wole soyinka", "genre": "Non-Fiction", "total_copies": 3, "available": 3}}
    members = [{"member_id": 1, "name": "kanja sesay", "email": "sesaykanja2@gmail.com", "borrowed_books": []}]
    result = borrow_book(books, members, 1, "12345")
    assert books["12345"]["available"] == 2
    assert "12345" in members[0]["borrowed_books"]

def test_return_book():
    books = {"12345": {"title": "Abiku", "author": "Wole soyinka", "genre": "Non-Fiction", "total_copies": 3, "available": 2}}
    members = [{"member_id": 1, "name": "kanja", "email": "sesaykanja2@mail.com", "borrowed_books": ["12345"]}]
    result = return_book(books, members, 1, "12345")
    assert books["12345"]["available"] == 3
    assert "12345" not in members[0]["borrowed_books"]
