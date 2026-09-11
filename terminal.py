import sys
from navigator import FileSystem
from classes import *

class Terminal:

    def __init__(self):
        self.history = []
        self.nav = FileSystem()
        self.nav.generate_fs()

        print(self.nav.curr_fol)

        print("========================================================================")
        print("Welcome to 'Who Was Here?' (An Incident Response Game)")
        print("========================================================================\n")

        print("Sweep this System which Was Recently Hacked.\nCheck for traces of hack, find out what they used for persistence and file a report at the end to win!")
        print("Type 'help' to see available commands")

        while True:
            self.listen()


    def listen(self):

        com_int_r = input(f"[Investigator@nox] [{self.nav.pwd()}] ")
        self.history.append(com_int_r)

        command = com_int_r.split()

        if command[0] == "help" and len(command) == 1:
            print("Here is the help list for you!")
            print("\t cd  \t- Change Directory.\n\t\t-> Usage 'cd Home' to go in the Home folder or 'cd ..' to go out of the current folder.\n\t\tYou can go up/down only one level at once. ")
            print("\t pwd \t- Print Working/Current Directory Path.")
            print("\t ls  \t- List Targeted Directory.\n\t\t-> By Default ls will execute with '-l' flag and display the current directory.\n\t\t-> Usage 'ls', 'ls -a', 'ls Home -a")
            print("\t cat \t- Concatenate.\n\t\t-> Used to view File.\n\t\t-> Usage 'cat file.txt'")
            print("\t report\t- Start the Report Writing Process\n\t\t-> Note: Once Started, you cannot execute any other command so make sure you are\n\t\tabsolutely sure before running this.\n\t\t-> Usage 'exit'")
            print("\t exit \t- Exit the Game.\n\t\t-> You couldn't do the Report.\n\t\t-> Usage 'exit'")


        elif command[0] == "cd" and len(command) == 2:
            if command[1] != "..":
                if command[1] == ".":
                    return
                else:
                    self.nav.jmp_into(command[1])
            else:
                self.nav.jmp_out()

        elif command[0] == "pwd" and len(command) == 1:
            print(self.nav.pwd())

        elif command[0] == "ls" and len(command) < 4:
            if len(command) == 3:
                if command[2] == "-a":
                    fol = self.nav.get_item(command[1])
                    if isinstance(fol, Folder):
                        fol.disp(True)
                    else:
                        print(f"ls: {command[1]} is a file or doesn't exist.")
                    return
                else:
                    print("ls: Invalid flag is given or out-of-format command is used.")
                    return

            elif len(command) == 2:
                if command[1] == "-a":
                    self.nav.curr_fol.disp(True)
                fol = self.nav.get_item(command[1])
                if isinstance(fol, Folder):
                    fol.disp()

            elif len(command) == 1:
                self.nav.curr_fol.disp()

            else:
                print("ls: out-of-format command is used.")

        elif command[0] == "cat" and len(command) == 2:
            filename = command[1]

            file = self.nav.get_item(filename)

            if not isinstance(file, File):
                print(f"cat: {filename} is a folder or doesn't exist.")
                return

            content = file.contents

            print(f"========{file.name}========")
            for line in content:
                print(line)

        elif command[0] == "exit" : exit()

t = Terminal()
