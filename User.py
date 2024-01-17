# utility modules
import time
import datetime
from click import clear

# command modules
from Admin import *
from Members import *

# sql connector module
import mysql.connector as sqlcon
mycon = sqlcon.connect(host='localhost', user='root', passwd='', database='lib_mng_db')

data_user = data_book = data_user_book = c_user = c_book = c_user_book = None

USER = {}

def idiot():
    global data_user
    global data_book
    global data_user_book
    global c_user
    global c_book
    global c_user_book
    c_user = mycon.cursor()
    c_user.execute("select * from User_Details")
    data_user = c_user.fetchall()
    c_book = mycon.cursor()
    c_book.execute("select * from Books")
    data_book = c_book.fetchall()
    c_user_book = mycon.cursor()
    c_user_book.execute("select * from User_Books")
    data_user_book = c_user_book.fetchall()

idiot()

users = {i[0]: [i[1], i[3], i[-1]] for i in
         data_user}  

while True:

    # clear()

    print(
        '''Login
Register

['L' for login, 'R' for register]\n'''
        )

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
                print(f'Successfully logged in as Admin {USER["name"]}')
            else:
                print(f'Successfully logged in as Member {USER["name"]}')
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
                    reg_user.execute(
                        f'''insert into User_Details (Username, U_Name, About, U_Type, 
                        U_Password) 
values ('{in_uname}', '{in_name}', '{in_about}', 'Member', '{in_pass}')'''
                        )
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


instructions = [
    ["Add users", "Admin"],
    ["Add books", "Admin"],
    ["Update book details", "Admin"],
    ["Issue a book", "Member"],
    ["Return a book", "Member"],
    ["Display book details", "AdminMember"],
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
        idiot()
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
