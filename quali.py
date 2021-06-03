from tkinter import *
from tkinter import messagebox

qual = Tk()
qual.title("Exception handling")
qual.geometry("400x400")
qual.config(bg="skyblue")

# Creating labels
amount = Label(qual, text="Please enter amount in account", bg="skyblue")

# Creating entries
account = Entry(qual)

def check():
    try:
        if int(account.get()) >= 3000:
            messagebox.showinfo("Status Feedback", "Congratulations. You qualify to go to Malaysia.")
    except ValueError:
        if account.get() != int:
            messagebox.showinfo("Message", "Insert more funds into account")
    else:
        if int(account.get()) < 3000:
            messagebox.showerror("Message", "Invalid")

def clear_all():
    account.delete(0, END)

def exit_program():
    return qual.destroy()

# Creating buttons
check = Button(qual, text="Check qualification", command=check, bg="blue")
clear = Button(qual, text="Clear", command=clear_all, bg="blue")
exit = Button(qual, text="Exit", command=exit_program, bg="blue")


# Placing
amount.place(x=100, y=20)
account.place(x=120, y=80)
check.place(x=120, y=130)
clear.place(x=160, y=190)
exit.place(x=165, y=240)

qual.mainloop()
