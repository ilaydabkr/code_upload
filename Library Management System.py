class Library:
    def __init__(self):
        self.file_name = 'books.txt'
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self. file. readlines()
        if not books: 
            print("Oh no! There is no such a book.")
        else:
            print("List of Books:")
            for book in books:
                book_info = book.strip().split(",")
                print (f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_books(self):
        title = input("Enter title:")
        author = input("Enter book author: ")
        first_release_year = input("Enter first release year: ")
        num_pages = input("Enter number of pages: ")
        genre = input("Enter genre of the book: ")
        book_info = f"{title},{author},{first_release_year},{num_pages},{genre}\n"
        self.file.write(book_info)
        print("Well done, you did it!")
    
    
    def remove_books(self):
        title = input("Enter book title that you would like to remove:")
        self.file.seek(0)
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(updated_books)
        print("Good work, it is done.")

lib = Library()

while True:
    print("***MENU***")
    print("1) List of Books")
    print("2) Add Book")
    print ("3) Remove Book")
    print ("Note: Press 'Q' to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_books()
    elif choice == "3":
        lib.remove_books()
    elif choice == "Q":
        break
    else:
        print("Invalid choice! Try again, you can do it.")