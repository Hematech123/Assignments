from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login Form")
root.geometry("300x200")

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "admin" and password == "123":
        messagebox.showinfo("Login", "Login Successful")
    else:
        messagebox.askyesnocancel("Login", "Invalid Username or Password")

# Username Label
label1 = Label(root, text="Username")
label1.pack()

# Username Entry
entry1 = Entry(root)
entry1.pack()

# Password Label
label2 = Label(root, text="Password")
label2.pack()

# Password Entry
entry2 = Entry(root, show="*")
entry2.pack()

# Login Button
button = Button(root, text="Login", command=login)
button.pack()

root.mainloop()