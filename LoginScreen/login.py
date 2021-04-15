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


    def console(self):
        LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")
        
        d = {}
        with open(self.filename) as f:
            for line in f:
                try:
                    if line == "":
                        continue
                    else:
                        (key, value) = line.rstrip("\n").split(":")
                        print(1)
                except ValueError:
                    pass

                d[key] = value
        print(d)

        # When Login is pressed
        if LorS.lower() == 'l':
            usr_nme = input(f"Enter your {self.slot1}: ")
            
            if usr_nme not in d.keys():
                print("Invalid Username! Don't have an account? Try signing up!")
                self.console()

            else:
                usr_pwd = input(f"Enter your {self.slot2}: ")

                if d[usr_nme] != usr_pwd:
                    print("Invalid Password! Don't have an account? Try signing up!")

                else:
                    return usr_nme

        # When Sign-Up is pressed
        elif LorS.lower() == "s":
            f = open(self.filename, "a+")
            good_nme = False
            while good_nme == False:
                usr_nme = input("What username do you prefer? ")

                if usr_nme in d.keys():
                    print("Username already exists!")
                
                else:
                    good_nme = True

            good_pwd = False
            while good_pwd == False:
                usr_pwd = input("Type out your password: ")
                usr_confPwd = input("Re-Type password: ")

                if usr_confPwd == usr_pwd:
                    good_pwd = True

                else:
                    print("Passwords do not match!")

            # f = open(self.filename, "a+")
            f.write(usr_nme + ":" + usr_pwd  + "\n")

        else:
            print("Please type a valid option")
            self.console()


        
