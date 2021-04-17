import tkinter
from tkinter import *


class gui_window:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x200")
        # self.root.configure(bg="yellow")

    def login_or_sign(self):
        self.root.title("Login or Sign-Up")
        self.login()

        self.root.mainloop()

    def submit(self):
        pass

    def login(self):
        Label(self.root, text="Username: ", bg="white").grid(row=1)
        Label(self.root, text="Password: ", bg="white").grid(row=3)

        e1 = Entry(self.root)
        e2 = Entry(self.root)
        e1.grid(row=1, column=1)
        e2.grid(row=3, column=1)

        sub_btn = tkinter.Button(self.root, text="Login", width=25, fg="green", bg="white", command=self.submit)
        sign_btn = tkinter.Button(self.root, text="Don't have an account? Sign In!", fg="yellow", bg="white", width=40,
                                  command=self.sign)
        sign_btn.grid(row=5, column=1)
        sub_btn.grid(row=5, column=0)

        self.root.mainloop()

    def sign(self):
        pass
