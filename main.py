from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("Password Manager")
root.geometry("500x600")
root.configure(background='black')

lobsterFont = Font(family='Lobster', size=40)
opensansSemiBold = Font(family='OpenSans-SemiBold', size=10)

# frame = Frame(root)
# frame.pack()

titleLabel = Label(root, text="PassMan")
titleLabel.place(relx=0.5, rely=0.28, anchor=CENTER)
titleLabel.configure(font=lobsterFont,background='black')

usernameLabel = Label(root, text="Username")
usernameLabel.configure(background='black', font=opensansSemiBold)
username = StringVar()
usernameEntry = Entry(root, textvariable=username)
usernameEntry.configure(background='white', fg='black')
usernameLabel.place(relx=0.5, rely=0.46, anchor=CENTER)
usernameEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

passwordLabel = Label(root, text="Password")
passwordLabel.configure(background='black', font=opensansSemiBold)
password = StringVar()
passwordEntry = Entry(root, textvariable=password)
passwordEntry.configure(background='white', fg='black')
passwordLabel.place(relx=0.5, rely=0.6, anchor=CENTER)
passwordEntry.place(relx=0.5, rely=0.64, anchor=CENTER)

loginButton = Button(root, text='Login')
loginButton.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()