from tkinter import *
from tkinter.font import Font

from functools import partial
import os

import psycopg2

def authenticate(username, passw):
    con = psycopg2.connect(database=os.environ.get('DBNAME'), user=os.environ.get('DBUSER'), password=os.environ.get('DBPASS'),
                           host=os.environ.get('DBHOST'),port='5432')
    cursor = con.cursor()

    cursor.execute(f'SELECT pass FROM usertable WHERE name=\'{username}\';')

    result = cursor.fetchone()

    print("Username:", username, "Password:", passw)

    if result == passw:
        AUTHENTICATED = True
        print(AUTHENTICATED)
    
    AUTHENTICATED = False
    print(AUTHENTICATED)


def main():

    root = Tk()
    root.title("Password Manager")
    root.geometry("500x600")
    root.configure(background='black')

    lobsterFont = Font(family='Lobster Regular', size=40)
    opensansSemiBold = Font(family='OpenSans-SemiBold', size=10)

    titleLabel = Label(root, text="PassMan")
    titleLabel.place(relx=0.5, rely=0.28, anchor=CENTER)
    titleLabel.configure(font=lobsterFont,background='black', fg='white')

    usernameLabel = Label(root, text="Username")
    usernameLabel.configure(background='black', font=opensansSemiBold, fg='white')
    # username = StringVar()
    usernameEntry = Entry(root)
    usernameEntry.configure(background='white', fg='black')
    usernameLabel.place(relx=0.5, rely=0.46, anchor=CENTER)
    usernameEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

    passwordLabel = Label(root, text="Password")
    passwordLabel.configure(background='black', font=opensansSemiBold, fg='white')
    # password = StringVar()
    passwordEntry = Entry(root)
    passwordEntry.configure(background='white', fg='black')
    passwordLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
    passwordEntry.place(relx=0.5, rely=0.64, anchor=CENTER)

    validateLogin = partial(authenticate, usernameEntry.get(), passwordEntry.get())

    loginButton = Button(root, text='Login', command=validateLogin)
    loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

    root.mainloop()

if __name__ == "__main__":
    main()