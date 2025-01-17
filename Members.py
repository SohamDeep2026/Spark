from tabulate import tabulate

# Issue a book
def issue_book(c_user, c_book, c_user_book, mycon, data_book, data_user):
    check = True
    Username = input("Enter username: ")
    Bk_ID = int(input("Enter book ID of book to issue: "))
    for i in data_user:
        if i[0] == Username: break
    else:
        print("Incorrect username. Try again.")
        check = False
    for i in data_book:
        if i[0] == Bk_ID:
            N_o_A_C = i[5]
            break
    else:
        print("Incorrect book ID. Try again.")
        check = False
    if N_o_A_C < 1:
        check = False
    if check:
        c_book.execute(
            "update Books set Number_of_Available_Copies = {} where Book_ID = {}".format(
                N_o_A_C - 1, Bk_ID
            )
        )
        c_user_book.execute(
            "insert into User_Books(Username, Book_ID, Issued_Date, Return_Date) values('{}', {}, curdate(), null)"
            .format(
                Username, Bk_ID
            )
        )
    mycon.commit()


# Return a book
def return_book(c_user, c_book, c_user_book, mycon, data_book, data_user):
    Username = input("Enter your username: ")
    Bk_ID = int(input("Enter book ID of the book that you want to return: "))
    for i in data_user:
        if i[0] == Username:
            break
    else:
        print("Incorrect username. Try again.")
        check = False
    for i in data_book:
        if i[0] == Bk_ID:
            N_o_A_C = i[5]
            break
    else:
        print("Incorrect book ID. Try again.")
        check = False
    c_book.execute(
        "update Books set Number_of_Available_Copies = {} where Book_ID = {}".format(
            N_o_A_C + 1, Bk_ID
        )
    )
    c_user_book.execute(
        "update User_Books set Return_Date = curdate() where Book_ID = {} and Username = '{}'".format(
            Bk_ID, Username
        )
    )
    mycon.commit()


# View Book Details
def display_book(data_book):
    data_book.insert(0, ["BookID", "Book Title", "Book Author", "Genre", "Total Copies", "Available Copies"])
    print_table(data_book)

def print_table(table):
    headings = table[0]
    data = table[1:]

    table_str = tabulate(data, headers=headings, tablefmt="grid")

    print(table_str)

