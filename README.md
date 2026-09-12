# Who Was Here?

#### Video Demo: <URL HERE>

#### Description:

Alriiight! This was CS50! Thank you Team Harvard and Professor Malan for guiding us through this Wonderful Journey.

**Who Was Here?** is a CLI-based Incident Response Training Game. You play as an Investigator / Incident Responder, and your job is to sweep a recently infected virtual machine, collect evidence, discover how the attacker gained persistence, and file a comprehensive report to win!

Every time you play, the game generates a unique scenario by injecting a random selection of malicious traces and persistence mechanisms into a virtual filesystem. You will need to use your terminal skills to explore the filesystem, read files, and identify the anomalies left behind by the attacker.

### Features
* **Virtual Filesystem:** A completely simulated, interactive filesystem populated dynamically upon launch.
* **Randomized Scenarios:** Traces and persistence mechanisms are selected at random each game, ensuring high replayability.
* **Basic Shell Commands:** Navigate using familiar commands like `cd`, `ls`, `pwd`, `tree`,and `cat`.
* **Tab Completion:** Supports standard shell tab-completion for faster navigation.
* **Interactive Reporting:** Once you've gathered your evidence, use the `report` command to take a randomized quiz on your findings and receive a performance rating (S, A, B, C).

### How to Play
Run the game using Python 3:
```bash
python3 terminal.py
```

Once in the game terminal, you can use the following commands to investigate:
* `help` - Show the list of available commands.
* `pwd` - Print the current working directory.
* `tree` -  Print the tree structure from the current folder.
* `ls` / `ls -a` - List files and directories in the current folder (supports viewing hidden files).
* `cd <directory>` - Change your current directory to explore different parts of the system.
* `cat <file>` - Read the contents of a file to look for suspicious modifications.
* `report` - Start the final report writing process. **Note:** Once started, you cannot go back to exploring. You will be asked questions about the anomalies you should have found!
* `exit` - Quit the game early.

### Project Structure
* `terminal.py`: The main entry point. Handles the game loop, user input, and command execution.
* `navigator.py`: Manages the virtual filesystem tree, handles directory traversal, and injects the attacker payloads.
* `classes.py`: Defines the `File` and `Folder` object models used to build the virtual filesystem.
* `infection.py`: Handles the randomized selection of attack traces and persistence mechanisms.
* `infections.py`: The database of all possible attack traces, affected files, payloads, and the corresponding quiz questions.
* `filecontent.py`: Contains the benign, default contents for files on the system before they are infected.
* `basefs.json`: A JSON map defining the base directory structure of the virtual OS.

Happy hunting, Investigator!


## AI Usage & Content Generation

Generative AI tools, specifically **Google Gemini and OpenAI ChatGPT**, were used in the creation of the following files:

* `basefs.json`
* `filecontent.py`
* `infections.py`

These files were generated and refined with AI assistance primarily for the purpose of creating **artificial visual and narrative data** for the game's simulated incident-response environment. Their contents provide fictional filesystem states, logs, traces, persistence indicators, and other details intended to make investigations more interesting and believable within the game.

These files **do not implement the core mechanics of WhoWasHere?** and do not determine how the game's underlying systems operate. They primarily provide data that the game's mechanics can display and interpret.

The simulated traces and persistence indicators are **fictional game representations**. Although some of them may resemble terminology, artifacts, or concepts associated with real-world cybersecurity incidents, they are not intended to constitute accurate instructions, procedures, or representations of real-world compromise, persistence, exploitation, or attack techniques.

All potentially malicious-looking commands, paths, payloads, and other content contained within these files are **non-executable strings/data** used solely for visual presentation, investigation gameplay, and narrative purposes. They are not intended to execute, modify, compromise, damage, or otherwise interfere with the user's actual device or operating system.

AI was therefore used primarily as a **content-generation and brainstorming tool for fictional game data**, rather than as the author of the game's core functionality or mechanics. The implementation and integration of the game's actual systems were developed separately.

