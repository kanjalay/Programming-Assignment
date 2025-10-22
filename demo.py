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