import tkinter
from tkinter import *
from tkinter import messagebox


class gui_window:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x200")
        self.root.configure(bg="light sky blue")
        self.sign_page = False

        self.d = {}
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

                self.d[key] = value

        self.name_var = StringVar()
        self.pwd_var = StringVar()
        self.re_pwd_var = StringVar()

    def login_or_sign(self):
        self.root.title("Login or Sign-Up")
        self.login()

        self.root.mainloop()

    def log_submit(self):
        name = self.name_var.get()
        pwd = self.pwd_var.get()

        if name not in self.d.keys():
            tkinter.messagebox.showerror("Verification", "Invalid Username! Don't have an account? Try signing up!")

        else:
            if self.d[name] != pwd:
                tkinter.messagebox.showerror("Verification", "Invalid Password! Don't have an account? Try signing up!")

            else:
                tkinter.messagebox.showinfo("Verification", "Username and Password verified!")
                self.root.destroy()
                self.top.destroy()
                return True

        # print(name, pwd)

    def sign_submit(self):
        name = self.name_var.get()
        pwd = self.pwd_var.get()
        re_pwd = self.re_pwd_var.get()

        if name not in self.d.keys():
            if pwd == re_pwd:
                self.f.write(name + ":" + pwd + "\n")
                tkinter.messagebox.showinfo("Verification", "Account created successfully")
                self.root.destroy()
                self.top.destroy()
                return True
            else:
                tkinter.messagebox.showerror("Verification", "Re-entered password does not match!")
        else:
            tkinter.messagebox.showerror("Verification", "Username already exists")

    def login(self):
        self.root.title("Login")
        if self.sign_page:
            self.root.deiconify()
            self.top.withdraw()
        else:
            Label(self.root, text="     Username: ", bg="light sky blue").grid(row=1, column=0)
            Label(self.root, text="     Password: ", bg="light sky blue").grid(row=3, column=0)

            self.e1 = Entry(self.root, textvariable=self.name_var).grid(row=1, column=2)
            self.e2 = Entry(self.root, textvariable=self.pwd_var).grid(row=3, column=2)

            sub_btn = tkinter.Button(self.root, text="Login", width=25, fg="green", bg="white",
                                     command=self.log_submit)
            sign_btn = tkinter.Button(self.root, text="Don't have an account? Sign In!", fg="blue", bg="white",
                                      width=40,
                                      command=self.sign)
            sub_btn.grid(pady=20, row=5, column=1)
            sign_btn.grid(pady=40, row=6, column=1)

        self.root.mainloop()

    def sign(self):
        if not self.sign_page:
            # Creating a new window
            self.top = Toplevel()
            self.top.geometry("600x200")
            self.top.title("Sign Up")
            self.top.configure(bg="light sky blue")

        if self.sign_page:
            self.top.deiconify()

        self.sign_page = True
        self.root.withdraw()

        self.f = open("loginData.txt", "a+")

        Label(self.top, text="Choose a Username: ", bg="light sky blue").grid(row=1, column=0)
        Label(self.top, text="Type out your Password: ", bg="light sky blue").grid(row=3, column=0)
        Label(self.top, text="Re-Type out your Password: ", bg="light sky blue").grid(row=5, column=0)

        self.e1 = Entry(self.top, textvariable=self.name_var).grid(row=1, column=2)
        self.e2 = Entry(self.top, textvariable=self.pwd_var).grid(row=3, column=2)
        self.e3 = Entry(self.top, textvariable=self.re_pwd_var).grid(row=5, column=2)

        sub_btn = tkinter.Button(self.top, text="Sign Up for free!", width=25, fg="green", bg="white",
                                 command=self.sign_submit)
        sign_btn = tkinter.Button(self.top, text="Already have an account? Login!", fg="blue", bg="white", width=40,
                                  command=self.login)
        sub_btn.grid(pady=20, row=7, column=1)
        sign_btn.grid(pady=40, row=8, column=1)

        # self.root.mainloop()
        self.top.mainloop()
