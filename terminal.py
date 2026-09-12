import sys
from navigator import FileSystem
from classes import *
import readline


class Terminal:

    def __init__(self):
        self.history = []
        self.nav = FileSystem()
        self.nav.generate_fs()
        self.nav.infect()

        #print(self.nav.curr_fol)

        print("========================================================================")
        print("Welcome to 'Who Was Here?' (An Incident Response Game)")
        print("========================================================================\n")

        print("Sweep this System which Was Recently Hacked.\nCheck for traces of hack, find out what they used for persistence and file a report at the end to win!")
        print("Type 'help' to see available commands")


        readline.set_completer(self.complete_path)
        readline.parse_and_bind("tab: complete")

        while True:
            self.listen()

    def complete_path(self, text, state):
        matches = []

        for item in self.nav.curr_fol.all:
            name = item.name

            if name.startswith(text):

                matches.append(name)

        matches.sort()

        if state < len(matches):
            return matches[state]

        return None


    def listen(self):

        com_int_r = input(f"[Investigator@nox] [{self.nav.pwd()}] > ")
        self.history.append(com_int_r)

        command = com_int_r.split()
        if not command:
            return

        if command[0] == "help" and len(command) == 1:
            print("Here is the help list for you!")
            print("\t cd  \t- Change Directory.\n\t\t-> Usage 'cd Home' to go in the Home folder or 'cd ..' to go out of the current folder.\n\t\tYou can go up/down only one level at once. ")
            print("\t pwd \t- Print Working/Current Directory Path.")
            print("\t tree\t- Print the entire folder and subfolders in a tree format.")
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

        elif command[0] == "tree" and len(command) == 1:
            print(self.nav.curr_fol)

        elif command[0] == "ls" and len(command) < 4:
            if len(command) == 3:
                if command[2].startswith("-"):
                    fol = self.nav.get_item(command[1])
                    if isinstance(fol, Folder):
                        if "a" in command[2][1:]:
                            fol.disp(True)
                        else: fol.disp()
                    else:
                        print(f"ls: {command[1]} is a file or doesn't exist.")
                    return
                else:
                    print("ls: Invalid flag is given or out-of-format command is used.")
                    return

            elif len(command) == 2:
                if command[1].startswith("-"):
                    if "a" in command[1][1:]:
                        self.nav.curr_fol.disp(True)
                    else:
                        self.nav.curr_fol.disp()

                fol = self.nav.get_item(command[1][1:])
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

        elif command[0] == "report" and len(command) == 1:
            print("\n" + "="*72)
            print("REPORT WRITING PROCESS STARTED")
            print("="*72)
            print("WARNING: You will not be able to run any more commands.")
            confirm = input("Are you sure you want to proceed? (y/n): ")
            if confirm.lower() != 'y':
                print("Report cancelled.")
                return

            total_questions = 0
            correct_answers = 0

            print("\nPlease answer the following questions based on your findings:\n")
            
            for index, q_set in enumerate(self.nav.ques_sets):
                if not q_set:
                    continue
                    
                import random
                num_q = random.randint(1, len(q_set))
                selected_q = random.sample(q_set, num_q)
                
                print(f"--- Finding {index + 1} ---")
                for q_dict in selected_q:
                    question = q_dict.get("question", "")
                    valid_answers = [str(a).strip().lower() for a in q_dict.get("answers", [])]
                    
                    user_ans = input(f"> {question}\nAnswer: ").strip().lower()
                    
                    if user_ans in valid_answers:
                        correct_answers += 1
                    total_questions += 1
                print()

            print("="*72)
            print("REPORT COMPLETE")
            print("="*72)
            print(f"Your Score: {correct_answers} / {total_questions}")
            
            percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
            if percentage == 100:
                print("Rating: S - Excellent work, Investigator! You found all the traces.")
            elif percentage >= 70:
                print("Rating: A - Good job! You identified most of the attack footprint.")
            elif percentage >= 40:
                print("Rating: B - Fair effort, but you missed some critical indicators.")
            else:
                print("Rating: C - You missed several key indicators. Back to training.")
                
            print("\nExiting game...")
            exit(0)

        else:
            print(f"Invalid Command: {com_int_r}. Type 'help' to see list of available commands.")

t = Terminal()
