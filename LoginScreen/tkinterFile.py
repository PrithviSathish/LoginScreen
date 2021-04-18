import tkinter
from tkinter import *
from tkinter import messagebox


class gui_window:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x200")
        self.root.configure(bg="light sky blue")

        self.name_var = StringVar()
        self.pwd_var = StringVar()

    def login_or_sign(self):
        self.root.title("Login or Sign-Up")
        self.login()

        self.root.mainloop()

    def submit(self):
        name = self.name_var.get()
        pwd = self.pwd_var.get()

        d = {}
        with open("loginData.txt") as f:
            for line in f:
                try:
                    if line == "":
                        continue
                    else:
                        (key, value) = line.rstrip("\n").split(":")
                        # print(1)
                except ValueError:
                    pass

                d[key] = value

        if name not in d.keys():
            tkinter.messagebox.showerror("Verification", "Invalid Username! Don't have an account? Try signing up!")

        else:
            if d[name] != pwd:
                tkinter.messagebox.showerror("Verification", "Invalid Password! Don't have an account? Try signing up!")

            else:
                tkinter.messagebox.showinfo("Verification", "Username and Password verified!")
                self.root.destroy()
                return name

        # print(name, pwd)

    def login(self):
        Label(self.root, text="     Username: ", bg="light sky blue").grid(row=1, column=0)
        Label(self.root, text="     Password: ", bg="light sky blue").grid(row=3, column=0)

        self.e1 = Entry(self.root, textvariable=self.name_var).grid(row=1, column=2)
        self.e2 = Entry(self.root, textvariable=self.pwd_var).grid(row=3, column=2)

        sub_btn = tkinter.Button(self.root, text="Login", width=25, fg="green", bg="white",
                                 command=self.submit)
        sign_btn = tkinter.Button(self.root, text="Don't have an account? Sign In!", fg="blue", bg="white", width=40,
                                  command=self.sign)
        sub_btn.grid(pady=20, row=5, column=1)
        sign_btn.grid(pady=40, row=6, column=1)

        self.root.mainloop()

    def sign(self):
        pass
