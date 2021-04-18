"""
This file is used to create the Login screen for various applications, websites etc

CONTAINS:
* Console
* Tkinter
"""


class CreateLogin:

    def __init__(self, slot1="username", slot2="password", filename="loginData.txt"):
        self.slot1 = slot1
        self.slot2 = slot2
        self.filename = filename

        f = open(self.filename, "a+")
        f.close()

    def console(self):
        import consoleFile
        consoleFile.run_on_console()

    def colorama(self):
        from coloramaFile import styleLogin
        win_log = styleLogin()
        win_log.Login_or_Sign()

    def tkinter(self):
        from tkinterFile import gui_window
        gui = gui_window()
        gui.login_or_sign()
