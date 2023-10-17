from Admin import *
from Members import *
import mysql.connector as sqlcon


mycon = sqlcon.connect(
    host="localhost",
    user="root",
    passwd="_password_to_access_MySQL_connection_of_host_to_use_to_create_the_database",
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


def instructions():
    print("Instructions(Select the option number)")
    print("1) Add users - (admin)")
    print("2) Add books - (admin)")
    print("3) Update book details - (admin)")
    print("4) Issue a book - (member)")
    print("5) Return a book - (member)")
    print("6) Display book details - (admin & member)")
    print("7) Help")
    print("8) Exit")


instructions()

while True:
    command = input("Enter your choice")

    if command == "1":
        add_user(c_user, c_book, c_user_book, mycon)
    elif command == "2":
        add_book(c_user, c_book, c_user_book, mycon)
    elif command == "3":
        update_book(c_user, c_book, c_user_book, mycon, data_book)
    elif command == "4":
        issue_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
    elif command == "5":
        return_book(c_user, c_book, c_user_book, mycon, data_book, data_user)
    elif command == "6":
        display_book(data_book)
    elif command == "7":
        instructions()
    elif command == "8":
        break
    else:
        print("the command you entered was not recognized")

mycon.close()



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
