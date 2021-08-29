from tkinter import *
from tkinter.font import Font

from postg import pg


root = Tk()
username = StringVar()
password = StringVar() 

def authenticate(username, passw):
    result = pg(f"SELECT pass FROM usertable WHERE name='{username}';",cond='one') 

    print("Username:", username, "Password:", passw)
    print(result,"\n\n")

    if result!=None and len(result)>0 and result[0] == passw:
       print("Authenticated =",True)
    else:
        print("Authenticated =",False)


def button_load():
    authenticate(username.get(), password.get())
    print("btn call complete")


def main():
    root.title("Password Manager")
    root.geometry("500x600")
    root.configure(background='black')

    lobsterFont = Font(family='Lobster', size=40)
    opensansSemiBold = Font(family='OpenSans-SemiBold', size=10)

    titleLabel = Label(root, text="PassMan")
    titleLabel.place(relx=0.5, rely=0.28, anchor=CENTER)
    titleLabel.configure(font=lobsterFont,background='black', fg='white')

    usernameLabel = Label(root, text="Username")
    usernameLabel.configure(background='black', font=opensansSemiBold, fg='white')
    usernameEntry = Entry(root, textvariable=username)
    usernameEntry.configure(background='white', fg='black')
    usernameLabel.place(relx=0.5, rely=0.46, anchor=CENTER)
    usernameEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

    passwordLabel = Label(root, text="Password")
    passwordLabel.configure(background='black', font=opensansSemiBold, fg='white')
    passwordEntry = Entry(root, textvariable=password, show='*')
    passwordEntry.configure(background='white', fg='black')
    passwordLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
    passwordEntry.place(relx=0.5, rely=0.64, anchor=CENTER)

    loginButton = Button(root, text='Login', command=button_load)
    loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

    root.mainloop()


main()