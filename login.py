from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Login form")
root.geometry('350x370')
root.configure(bg='grey')

def login():
    username = "gokul"
    password = "12345"
    if username_entry.get()==username and password_entry.get()==password:
        messagebox.showinfo(title="Login Success", message="You successfully login.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = Frame(bg='#333333')

login_label = Label(frame, text="Login", bg="#63B3EB", fg="white", font=("Arial", 30))
username_label = Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = Entry(frame, font=("Arial", 16))
password_entry = Entry(frame, show="*", font=("Arial", 16))
password_label = Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = Button(frame, text="Login", bg="skyblue", fg="#FFFFFF", font=("Arial", 16), command=login)


login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
root.mainloop()