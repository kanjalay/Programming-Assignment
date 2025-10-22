README.md 
MINI LIBRARY MANAGEMENT SYSTEM 
�
� Overview 
The Mini Library Management System is a simple Python-based project designed to 
manage books and members in a small library. It demonstrates CRUD operations 
(Create, Read, Update, Delete) and borrowing/returning functionalities using Python 
data structures — dictionaries, lists, and tuples. 
�
� Features 
• Add, search, update, and delete books 
• Add, update, and delete members 
• Borrow and return books 
• List all available books and active members 
• Validations for duplicates and borrowing limits 
�
� Data Structures Used 
• Dictionary (dict): Used to store books with their ISBN as unique keys for fast 
lookup and updates. 
• List (list): Used to store multiple members and their borrowed books. 
• Tuple (tuple): Used to define fixed genres of books since they don’t change 
often. 
�
�
 ️ Project Files 
• operations.py → Contains all the library management functions (core logic) 
• demo.py → Demonstrates how each function works step-by-step 
• README.md → Project overview and setup instructions 
⚙
 ️ How It Works 
1. Add a Book 
add_book(isbn, title, author, genre, total_copies) 
Stores a new book in the library collection. 
2. Add a Member 
add_member(member_id, name, email) 
Registers a new library member. 
3. Search for a Book 
search_books(keyword) 
Returns matching books based on title or author. 
4. Borrow & Return 
borrow_book(member_id, isbn) 
return_book(member_id, isbn) 
Allows members to borrow or return books with validation. 
5. Update or Delete 
update_book(isbn, title=None, author=None, genre=None, total_copies=None) 
delete_book(isbn) 
Modify book details or remove a book entirely. 
▶
 ️ How to Run 
1. Ensure Python 3 is installed. 
2. Place all files (operations.py, demo.py, README.md) in the same folder. 
3. Run the demo file: 
python demo.py 
�
� Example Output 
LIBRARY SYSTEM DEMO  
Book added successfully 
Member added successfully 
Book found: Python Basics 
Book borrowed successfully 
Book returned successfully 
Book deleted successfully 
DEMO COMPLETE  
�
�
 ‍
 💻 Author 
Kanja Abraham Joe Sesay (student of Limkokwing) 
�
� Contact 
sesaykanja2@gmail.com 
+232 73 807 472 
20B Banana Water, Congo Cross 
