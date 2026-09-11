# Who Was Here?

#### Video Demo: <URL HERE>

#### Description:

Alriiight! This was CS50! Thank you Team Harvard and Professor Malan for guiding us through this Wonderful Journey.

**Who Was Here?** is a CLI-based Incident Response Training Game. You play as an Investigator / Incident Responder, and your job is to sweep a recently infected virtual machine, collect evidence, discover how the attacker gained persistence, and file a comprehensive report to win!

Every time you play, the game generates a unique scenario by injecting a random selection of malicious traces and persistence mechanisms into a virtual filesystem. You will need to use your terminal skills to explore the filesystem, read files, and identify the anomalies left behind by the attacker.

### Features
* **Virtual Filesystem:** A completely simulated, interactive filesystem populated dynamically upon launch.
* **Randomized Scenarios:** Traces and persistence mechanisms are selected at random each game, ensuring high replayability.
* **Basic Shell Commands:** Navigate using familiar commands like `cd`, `ls`, `pwd`, and `cat`.
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
