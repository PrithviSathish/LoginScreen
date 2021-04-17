# from termcolor import colored
import colorama
from pyfiglet import Figlet
# from main import CreateLogin

colorama.init()


class styleLogin():

	def __init__(self):
		f = open("LoginData.txt", "a+")
		f.close()
	
	def Login_or_Sign(self):
		f = Figlet(font='slant')
		word = 'L O G I N  /  S I G N - U P'
		CLEAR_SCREEN = '\033[2J'
		RED = '\033[31m'   # mode 31 = red forground
		RESET = '\033[0m'  # mode 0  = reset
		print(CLEAR_SCREEN + RED + f.renderText(word) + RESET)

		LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")
        
        d = {}
        with open(self.filename) as f:
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

        if LorS.lower() == "s":
            self.Sign()

        elif LorS.lower() == "l":
            self.Log()

        else:
            print("Please enter a valid choice!")
            self.Login_or_Sign()

    def Log(self):
        pass

    def Sign(self):
        pass



