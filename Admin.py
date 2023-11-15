from tabulate import tabulate

# Add a member
def add_user(c_user, c_book, c_user_book, mycon):
    Username = input("Enter username")
    U_Name = input("Enter your name")
    About = input("Enter a few words about yourself")
    U_Type = input("Enter Admin/Member")
    U_Pswd = input("Set Password")
    c_user.execute(
        "insert into User_Details(Username, U_Name, About, U_Type, Date_of_Joining, U_Password) values('{}', '{}', '{}', '{}', curdate(), '{}')".format(
            Username, U_Name, About, U_Type, U_Pswd
        )
    )
    mycon.commit()


# Add a book
def add_book(c_user, c_book, c_user_book, mycon):
    Bk_ID = input("Enter bookID")
    Bk_Title = input("Enter book name")
    A_Name = input("Enter author name")
    Genre = input("Enter Genre")
    N_o_C = input("Enter number of copies of the book")
    c_user.execute(
        "insert into Books(Book_ID, Book_Title, Author_Name, Genre, Number_of_Copies, Number_of_Available_Copies) values('{}', '{}', '{}', '{}', {}, {})".format(
            Bk_ID, Bk_Title, A_Name, Genre, N_o_C, N_o_C
        )
    )
    mycon.commit()


# Update book count
def update_book(c_user, c_book, c_user_book, mycon, data_book):
    check = True
    Bk_ID = int(input("Enter book ID of the book to update."))
    choice = input("Number of copies of the book decreases or increases? d/i")
    if choice == "d":
        for i in data_book:
            if i[0] == Bk_ID:
                N_o_C = i[4]
                N_o_A_C = i[5]
                break
        else:
            print("Incorrect book ID. Try again.")
            check = False
        if check:
            decrease = int(input("Enter decrease in the number of copies of the book."))
            if N_o_C - decrease > 0:
                c_book.execute(
                    "update Books set Number_of_Copies = {} where Book_ID = {}".format(
                        N_o_C - decrease, Bk_ID
                    )
                )
            else:
                print(
                    "Invalid decrease in number of copies. Number of copies available = ",
                    N_o_C,
                )
    elif choice == "i":
        for i in data_book:
            if i[0] == Bk_ID:
                N_o_C = i[4]
                N_o_A_C = i[5]
                break
        else:
            print("Incorrect book ID. Try again.")
            check = False
        if check:
            increase = int(input("Enter increase in the number of copies of the book."))
            c_book.execute(
                "update Books set Number_of_Copies = {}, Number_of_Available_Copies = {} where Book_ID = '{}'".format(
                    N_o_C + increase, N_o_A_C + increase, Bk_ID
                )
            )
    mycon.commit()


# View Book Details
def display_book(data_book):
    data_book.insert(0, ["BookID", "Book Title", "Book Author", "Genre", "Total Copies", "Available Copies"])
    print_table(data_book)

a = (1, 'Concepts of Physics', 'HC Verma', 'Physics', 9, 9)

head = ["BookID", "Book Title", "Book Author", "Genre", "Copies", "Available Copies"]

def print_table(table):
    # Assuming the first list is the heading row
    headings = table[0]
    data = table[1:]

    # Use the 'tabulate' function to format the table
    table_str = tabulate(data, headers=headings, tablefmt="grid")

    print(table_str)
