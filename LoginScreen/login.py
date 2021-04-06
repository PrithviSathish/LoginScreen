'''
This file is used to create the Login screen for various applications, websites etc

CONTAINS:
* Console
* Tkinter
'''

class CreateLogin:


    def __init__(self, slot1, slot2, filename="loginData.txt"):
        self.slot1 = slot1
        self.slot2 = slot2
        self.filename = filename

        self.f = open(self.filename, "a+")
        self.d = dict(self.f.readlines())


    def console(self):
        LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")

        if LorS.lower() == 'l':
            usr_name = input("Enter your {self.slot1}: ")

            if usr_name not in self.d.keys():
                print("Invalid Username! Don't have an account? Try signing up!")
                self.console()

            else:
                usr_pwd = input("Enter your {self.slot2}: ")

                if self.d[usr_name] != usr_pwd:
                    print("Invalid Password! Don't have an account? Try signing up!")

                else:
                    return usr_name


        
