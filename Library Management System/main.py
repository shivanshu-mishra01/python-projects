import json
class Library:

    def __init__(self):
        self.store={}
        self.load_data()
    
    def add_book(self):
        book_id= (input("Enter Book ID:"))
        if book_id in self.store:
            print("ID already exists..Add Unique ID")
            return
        book_name= input("Enter Book name:")
        author=input("Enter Author name:")
        while True:
            copies=int(input("Enter Total copies:"))
            if copies < 0:
                print("Enter valid number of copies")
            else:
                break 
        
        
        self.store[book_id]={
        "book_name": book_name,
        "author":author,
        "copies":copies,
        "history": ["Book Added"]}
        print("Book Added successfully")
        self.save_data()
    
    
    def load_data(self):
        try:
            with open("data.json",'r') as file:
                self.store=json.load(file)
        except FileNotFoundError:
            self.store={}
    
    def save_data(self):
        with open("data.json",'w') as file:
            json.dump(self.store,file,indent=4)


    def view_book(self):
        if not self.store:
            print("Book not Available")
            return
        
        for book_id , book in self.store.items():
            print("-------------------------------")
            print("Book ID:",book_id)
            print("Book Name:",book['book_name'])
            print("Book Author:",book['author'])
            print("Copies:",book['copies'])
            print("-------------------------------")

    def search_book(self):
        book_id =str(input("Enter book ID:"))
        if book_id in self.store:
            book=self.store[book_id]
            print("-------------------------------")
            print("Book ID:",book_id)
            print("Book Name:",book['book_name'])
            print("Book Author:",book['author'])
            print("Copies:",book['copies'])
            print("-------------------------------")
        else:
            print("Book Not Found")
    
    def borrow(self):
        book_id=str(input("Enter book ID:"))
        if book_id not in self.store:
            print("Book doesn't exist")
        elif self.store[book_id]["copies"]<=0:
            print("Out of Stock..")
        else:
            self.store[book_id]['copies'] -=1
            self.store[book_id]['history'].append("Borrowed")
            self.save_data()
            print("Book Borrowed successfully")
            print( f'Remaining copies:{self.store[book_id]["copies"]}')
        
            
            
    def return_book(self):
        book_id = str(input("Enter book ID:"))
        if book_id not in self.store:
            print("Book doesn't exist")
        else:
            self.store[book_id]['copies'] +=1
            self.store[book_id]['history'].append("Returned")
            self.save_data()
            print("Book Returned successfully")
            print(f"Current copies:{self.store[book_id]['copies']}")

    def remove_book(self):
        book_id= str(input("Enter book ID:"))
        if book_id not in self.store:
            print("Book doesn't exist")
        else:
            del self.store[book_id]
            self.save_data()
            print("Book deleted successfully ")

    def book_history(self):
        book_id=str(input("Enter book ID:"))
        if book_id in self.store:
            history=self.store[book_id]['history']
            print("====== Book History ======")
            for data in history:
                print("•", data)
            print("==========================")
        else:
            print("Book not found")
            
    def menu(self):
        while True:
            user_input=int(input("""===== Welcome To Library Management System =====
                        1. Add Book
                        2. View All Book
                        3. Search Book
                        4. Borrow Book
                        5. Return Book
                        6. Remove Book
                        7. View Hisory
                        8. Exit
                        Enter your Choice :"""))
            
            if user_input == 1:
                self.add_book()
            elif user_input == 2:
                self.view_book()
            elif user_input==3:
                self.search_book()
            elif user_input ==4:
                self.borrow()
            elif user_input ==5:
                self.return_book()
            elif user_input==6:
                self.remove_book()
            elif user_input ==7:
                self.book_history()
            elif user_input == 8:
                print("Thanks for using our system. Exiting...")
                break
                    
            else:
                print("Invalid Input.. Please Try Again")
            

        






l=Library()
l.menu()