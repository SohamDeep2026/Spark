# utility modules
import time
import datetime
from click import clear

# command modules
from Admin import *
from Members import *

# sql connector module 
import mysql.connector as sqlcon

USER = {}

mycon = sqlcon.connect(
    host="localhost",
    user="shuvam",
    passwd="guikJBVhjjhb102!?",
    database="lib_mng_db",
)

if mycon.is_connected() is False:
    print("Error connecting to MySQL Database")

c_user = mycon.cursor()
c_user.execute("select * from User_Details")
data_user = c_user.fetchall()
c_book = mycon.cursor()
c_book.execute("select * from Books")
data_book = c_book.fetchall()
c_user_book = mycon.cursor()
c_user_book.execute("select * from User_Books")
data_user_book = c_user_book.fetchall()

users = { i[0]: [i[1], i[3], i[-1]] for i in data_user } # dictionary of user data. key is username, value is list of name, type, password


# login register code

while True:

    clear()

    print('''Login
Register
        
['L' for login, 'R' for register]\n''')

    lr = input()

    if lr.upper() == "L":
        
        in_uname = input("Enter your username: ")
        in_pass = input("Enter your password: ")

        if in_uname in users:
            if users[in_uname][2] == in_pass:
                USER = {
                    "username": in_uname,
                    "name": users[in_uname][0],
                    "type": users[in_uname][1]
                }
        
        if USER == {}: 
            print("\nERROR: Incorrect Credentials")
            time.sleep(2)
            continue
        else:
            if USER['type'] == "Admin":
                print(f'Successfully logged in as Admin { USER["name"] }')
            else:
                print(f'Successfully logged in as Member { USER["name"] }')
            break

    elif lr.upper() == "R":
        in_uname = input("Choose your username: ")
        in_name = input("Enter your name: ")
        in_about = input("Enter a short description about yourself: ")
        in_pass = input("Choose your password: ")
        in_confirmpass = input("Confirm your password: ")

        issue = ""

        if in_pass == in_confirmpass:
            if not in_uname in users:
                USER = {
                    "username": in_uname,
                    "name": in_name,
                    "type": "Member"
                }
                now = datetime.datetime.now()
                reg_user = mycon.cursor()

                try:
                    reg_user.execute(f'''insert into User_Details (Username, U_Name, About, U_Type, U_Password) 
values ('{in_uname}', '{in_name}', '{in_about}', 'Member', '{in_pass}')''')
                    mycon.commit()
                except:
                    mycon.rollback()
                    USER = {}
                    issue = "ERROR: Changes couldn't be save. Try again later."


            else:
                issue = "ERROR: Username already taken"
        else:
            issue = "ERROR: Passwords do not match"

        if USER == {}: 
            print("\n" + issue)
            time.sleep(2)
            continue
        else:
            time.sleep(1)
            print(f'Successfully logged in as Member {USER["name"]}')
            break

clear()

# at the end of this loop the user is logged in 


# list of instructions 
instructions = [
    ["Add users", "Admin"],
    ["Add books", "Admin"],
    ["Update book details", "Admin"],
    ["Issue a book", "Member"],
    ["Return a book", "Member"],
    ["Display book details", "AdminMember"],
    # ["Help", "AdminMember"], removed help command, was redundant
    ["Exit", "AdminMember"]
]

# this list consists of all the commands the logged in user can execute
valid_instructions = {}
j = 1
for i in instructions:
    if USER["type"] in i[1]:
        valid_instructions[str(j)] = i[0]
        j += 1

# this is the loop which allows us to execute commands
while True:

    for i in valid_instructions:
        print(f'{i} > {valid_instructions[i]}')
    print('\n[Enter respective numbers to execute commands]')
    command = input()

    if valid_instructions[command]:
        cmd = valid_instructions[command]
        if cmd == "Add users":
            add_user(c_user, c_book, c_user_book, mycon)
        elif cmd == "Add books":
            add_book(c_user, c_book, c_user_book, mycon)
        elif cmd == "Update book details":
            update_book(c_user, c_book, c_user_book, mycon, data_book)
        elif cmd == "Issue a book":
            issue_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
        elif cmd == "Return a book":
            return_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
        elif cmd == "Display book details":
            c_book = mycon.cursor()
            c_book.execute("select * from Books")
            data_book = c_book.fetchall()
            display_book(data_book)
        elif cmd == "Exit":
            break
        else:
            print("ERROR: Invalid command")
            time.sleep(2)
    
    print("\n")


mycon.close()


# instructions()

# while True:

#     command = input("Enter your choice")

#     if command == "1":
#         add_user(c_user, c_book, c_user_book, mycon)
#     elif command == "2":
#         add_book(c_user, c_book, c_user_book, mycon)
#     elif command == "3":
#         update_book(c_user, c_book, c_user_book, mycon, data_book)
#     elif command == "4":
#         issue_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
#     elif command == "5":
#         return_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
#     elif command == "6":
#         display_book(data_book)
#     elif command == "7":
#         instructions()
#     elif command == "8":
#         break
#     else:
#         print("the command you entered was not recognized")




#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################
#########################################################################################

# # all module imports
#
# import os
# import db as database
# import time
# import datetime
# from click import clear
#
#
# # module imports end here
#
#
# # pre-defines
#
# USER = []
#
# # pre-defines end
#
#
# # this is the login in process
#
# clear()
#
# while True:
#     flag = False
#     choice = input("noname@library:~$ ")
#
#     if choice == "login":
#         username = input("username: ")
#         password = input("password: ")
#
#         users = database.users_read()
#         if username in users:
#             if password == users[username]["password"]:
#                 USER = [username, users[username]["type"]]
#                 flag = True
#             else:
#                 clear()
#                 print("the password you entered was incorrect")
#
#                 time.sleep(2)
#                 clear()
#         else:
#             clear()
#             print("the username you entered is not that of a registered user")
#
#             time.sleep(2)
#             clear()
#
#     if choice == "register":
#         username = input("username: ")
#         name = input("name: ")
#         about = input("about: ")
#         password = input("password: ")
#         password_check = input("re-enter the password: ")
#
#         users = database.users_read()
#
#         if password == password_check:
#             if username in users:
#                 clear()
#                 print("the username you entered is already taken")
#
#                 time.sleep(2)
#                 clear()
#             else:
#                 users[username] = {
#                     "username": username,
#                     "name": name,
#                     "about": about,
#                     "type": "member",
#                     "date of joining": datetime.datetime.now().strftime("%d %B %Y"),
#                     "password": password
#                     }
#                 USER = [username, users[username]["type"]]
#                 database.users_write(users)
#                 flag = True
#         else:
#             clear()
#             print("the passwords do not match")
#
#             time.sleep(2)
#             clear()
#
#     if flag:
#         break
#
# print("\nyou have logged in successfully")
# time.sleep(0.5)
#
# if USER[1] == "admin":
#     from admin import *
# elif USER[1] == "member":
#     from member import *
#
# # the user has logged in, imports have been made, now we move on to the commands
# # screen, where all the commands are processed
#
#
# # this is a while true loop that will endlessly process commands the user enters
#
# clear()
#
# while True:
#
#     command = input(f"{USER[0]}@library:~$ ").lower()
#
#     if command in ["exit", "e"]:
#         break
#     elif command in ["help", "h"]:
#         commands()
#     elif command in ["books", "b"]:
#         view_books()
#     elif command in ["borrowed books", "bb"]:
#         view_borrowed_books(USER)
#     elif command in ["profile", "p"]:
#         view_profile(USER)
#     elif command in ["choose", "c"]:
#         choose_book(input("\nenter the name of the book you wish to borrow: "), USER)
#     elif command in ["return", "r"]:
#         return_book(input("\nenter the name of the book you wish to return: "), USER)
#     else:
#         print("the command you entered was not recognized")
#
#     print("")
