
import sys
class library:
    def __init__(self,list_of_books):
        self.available_books=list_of_books

    def display_books(self):
        for book in self.available_books:
            print(book)

    def lend_book(self,requested_book):
        if requested_book in self.available_books:
            print("the book has been borrowed")
            self.available_books.remove(requested_book)
        else:
            print("the book you want to lend is not found")

    def add_book(self,added_book):
        self.available_books.append(added_book)
        print("thanks for returning the borrowed book")

class student:
    def request_book(self):
        print("enter the book you want to lend")
        self.book=input()
        return self.book
    def added_book(self):
        print("enter the name of the book you want to add")
        self.book=input()
        return self.book

def main():
    library1=library(["The Last Battle","The Screwtape letters","The Great Divorce"])
    student1=student()

    done = True
    while done == True:
        print(""" ======LIBRARY MENU=======
                      1. Display all available books
                      2. Request a book
                      3. Return a book
                      4. Exit
                      """)
        choice=int(input("enter your choice:"))
        if choice==1:
            library1.display_books()
        elif choice==2:
            library1.lend_book(student1.request_book())
        elif choice==3:
            library1.add_book(student1.added_book())
        elif choice==4:
             sys.exit()

main()
