#Books = ['Maths', 'English', 'Literature', 'Physics']
Books = ['Maths', 'English']

def view_books(Books):
    return f"These are the available books : {Books}"

def borrow_book(Books):
    book = input('What book do you want? ')

    if book in Books:
        Books.remove(book)
        return f"Here you go, take your {book} Book."
    else:
        return f"The book you have requested is not in our library. Check back later"
  
def return_a_book(Books):
    book = input('What book do you want to return? ')
    Books.append(book)
    return f"Thank you!"

def user_actions():
    while True:
        action = input("Welcome to our LMS!. What would you like to do? ")

        if action == "view books":
                print(view_books(Books))

        elif action == "borrow a book":
                if Books == []:
                    print("There are no more books available!")
                else:
                    print(borrow_book(Books))
                    print(Books)

        elif action == "return a book":
                print(return_a_book(Books))
                print(Books)
        
        elif action == "exit":
                return f"Thank you for visiting, see you some other time."
        
        else:
                print("Please choose a valid option!")

print(user_actions())

    
