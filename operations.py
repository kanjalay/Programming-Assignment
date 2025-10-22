# Library Management System Data Structures

# 1. Books dictionary: ISBN → book details
books = {}

# 2. Members list: each member is a dictionary
members = []

# 3. Genres tuple
genres = ()
#Using CRUD
# Add a book
def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "A Book with this ISBN exists."
    if genre not in genres:
        return "Invalid genre."
    books[isbn] = {"title": title, "author": author, "genre": genre, "total_copies": total_copies}
    return f"Book '{title}' added successfully."

# Add a member
def add_member(member_id, name, email):
    for m in members:
        if m["member_id"] == member_id:
            return "Member ID already exists."
    members.append({"member_id": member_id, "name": name, "email": email, "borrowed_books": []})
    return f"Member '{name}' added successfully."

# Search for books
def search_books(keyword):
    result = []
    for isbn, details in books.items():
        if keyword.lower() in details["title"].lower() or keyword.lower() in details["author"].lower():
            result.append({isbn: details})
    return result if result else "No matching books found."

# Update book
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in genres:
        return "Invalid genre."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies:
        books[isbn]["total_copies"] = total_copies
        books[isbn]["available_copies"] = total_copies
    return f"Book '{isbn}' updated successfully."

# Delete book
def delete_book(isbn):
    if isbn not in books:
        return "Book not found."
    for m in members:
        if isbn in m["borrowed_books"]:
            return "Book cannot be deleted, it is currently borrowed."
    del books[isbn]
    return f"Book '{isbn}' deleted successfully."

# Borrow book
def borrow_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if len(m["borrowed_books"]) >= 3:
                return "Cannot borrow more than 3 books."
            if isbn not in books or books[isbn]["available_copies"] == 0:
                return "Book not available."
            m["borrowed_books"].append(isbn)
            books[isbn]["available_copies"] -= 1
            return f"Book '{books[isbn]['title']}' borrowed by {m['name']}."
    return "Member not found."

# Return book
def return_book(member_id, isbn):
    for m in members:
        if m["member_id"] == member_id:
            if isbn not in m["borrowed_books"]:
                return "This book was not borrowed."
            m["borrowed_books"].remove(isbn)
            books[isbn]["available_copies"] += 1
            return f"Book '{books[isbn]['title']}' returned successfully."
    return "Member not found."
# Demo (demo.py simulation)

print(add_book("001", "Abiku", "Wole soyinka", "Fiction", 5))
print(add_book("002", "Blind boy", "chinu Achebeh", "Non-Fiction", 3))

print(add_member("M001", "kanja sesay", "sesaykanja2@gmail.com@example.com"))
print(add_member("M002", "loko", "loko@example.com"))

print(search_books("Python"))

print(borrow_book("M001", "001"))
print(return_book("M001", "001"))

print(update_book("002", title="Abiku"))
print(delete_book("001"))



