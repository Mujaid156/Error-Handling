from tkinter import *
from tkinter import messagebox

# Window details
authen = Tk()
authen.title("Authentication")
authen.geometry("300x300")
authen.config(bg="skyblue")


# Creating labels
detail = Label(authen, text="Please enter login details", bg="skyblue")
name = Label(authen, text="Username", bg="skyblue")
word = Label(authen, text="Password", bg="skyblue")

# Creating entries
user = Entry(authen)
passw = Entry(authen)

def log():
    login_details = {"Zaid": "1000", "Aaliyah": "5566", "Lithe": "7700", "Thabo": "1244", "Zoe": "4582"}

    if login_details.get(user.get()):
        if login_details[user.get()] == passw.get():
            messagebox.showinfo("Message", "Access granted")
            authen.destroy()
            import quali
        else:
            messagebox.showerror("Message", "Access denied")

def clear_all():
    user.delete(0, END)
    passw.delete(0, END)

def exit_program():
    return authen.destroy()

# Crating Buttons
login = Button(authen, text="Login", command=log, bg="blue")
clear = Button(authen, text="Clear", command=clear_all, bg="blue")
exit = Button(authen, text="Exit", command=exit_program, bg="blue")

# Placing labels
detail.pack()
name.pack()


# Placing entries
user.pack()
word.pack()
passw.pack()

# Placing buttons
login.place(x=120, y=130)
clear.place(x=120, y=170)
exit.place(x=122, y=210)

authen.mainloop()
