## Relations Classification App

### Running the App

There are two choices for running the app, each held in their own .py file:

- main.py - For graphical interface. Needs an additional dependency to run this version of the app

- main_CLI.py - For terminal-based interface. Only requires python to run.

#### Using main.py

When the GUI boots up, a size for the matrix must be entered first before the matrix can be created and modified. (The size can be changed later by entering a new number and pressing ENTER)

After the size if chosen and the matrix shows up, it will be a full matrix of 0's which can be clicked to switch the value between 1 and 0.

Under the matrix you will see 4 more buttons. The first button confirms the "check" option chosen by the second button (which initiates a drop-down menu) and the third button does the same for the fix option picked in the fourth button (also a drop-down)

Under it all, there will be the results in text form of what the results/changes are of the choice. The matrix itself will also visually show what elements were changed in the most recent fix.

#### Using main_CLI.py

When the CLI runs, it will ask for a size for the matrix, this can not be changed without either running through the app until it asks for another matrix.

After the size is selected, the program will go row by row for what the elements of the matrix is. Each row has to be a selection of 1's or 0's seperated by spaces. NOTE: that if not enough elements are entered, then the program will fill it with 0's.

Next, the program will ask if you want to "check" or "fix" the matrix. Checking is pretty self-explanatory and will check if the matrix is of the selected option (only one operation can be used for a single matrix). Fixing a matrix will prompt for an operation and make the matrix represent that option (e.g. make an antisymmetric matrix symmetric).

After the results are printed, you can choose to go through another matrix (runs the program once again) or not (end the program).

### Required Dependencies

- Kivy - for use in the GUI version of the app 
