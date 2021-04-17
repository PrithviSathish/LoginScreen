def run_on_console():
    # consoleFile.confile()

    LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")

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
    # print(d)

    # When Login is pressed
    if LorS.lower() == 'l':
        usr_nme = input("Enter your username: ")

        if usr_nme not in d.keys():
            print("Invalid Username! Don't have an account? Try signing up!")
            run_on_console()

        else:
            usr_pwd = input("Enter your password: ")

            if d[usr_nme] != usr_pwd:
                print("Invalid Password! Don't have an account? Try signing up!")
                run_on_console()
            else:
                return usr_nme

    # When Sign-Up is pressed
    elif LorS.lower() == "s":
        f = open("loginData.txt", "a+")
        good_nme = False
        while not good_nme:
            usr_nme = input("What username do you prefer? ")

            if usr_nme in d.keys():
                print("Username already exists!")

            else:
                good_nme = True

        good_pwd = False
        while not good_pwd:
            usr_pwd = input("Type out your password: ")
            usr_confPwd = input("Re-Type password: ")

            if usr_confPwd == usr_pwd:
                good_pwd = True

            else:
                print("Passwords do not match!")

        # f = open(filename, "a+")
        f.write(usr_nme + ":" + usr_pwd + "\n")

    else:
        print("Please type a valid option")
        run_on_console()