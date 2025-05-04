## Relations Classification App

### Present Files

- main.py - GUI file
- relationscalc.kv - styling file for GUI
- main_CLI.py - Terminal-based interface file
- relations.py - home file of the algorithms
- test_relations.py - test cases for the relations.py algorithms
- README.md - this file

### Running the App

There are three choices for running the app, two held in their own .py file and another by way of importing:

- main.py - For graphical interface. Needs an additional dependency to run this version of the app

- main_CLI.py - For terminal-based interface. Only requires python to run.

- import relations.py - For use in self-created programs

#### Using main.py

To run this version of the program, first make sure that you have a python venv set up with the required dependencies installed inside. Then, either use an IDE specific way of running python scripts or using the command line and entering "python main.py"

When the GUI boots up, a size for the matrix must be entered first before the matrix can be created and modified. (The size can be changed later by entering a new number and pressing ENTER)

After the size if chosen and the matrix shows up, it will be a full matrix of 0's which can be clicked to switch the value between 1 and 0.

Under the matrix you will see 4 more buttons. The first button confirms the "check" option chosen by the second button (which initiates a drop-down menu) and the third button does the same for the fix option picked in the fourth button (also a drop-down)

Under it all, there will be the results in text form of what the results/changes are of the choice. The matrix itself will also visually show what elements were changed in the most recent fix.

#### Using main_CLI.py

To run the CLI either use an IDE specific way of running a python file or command lining "python main_CLI.py".

When the CLI runs, it will ask for a size for the matrix, this can not be changed without either running through the app until it asks for another matrix.

After the size is selected, the program will go row by row for what the elements of the matrix is. Each row has to be a selection of 1's or 0's seperated by spaces. NOTE: that if not enough elements are entered, then the program will fill it with 0's.

Next, the program will ask if you want to "check" or "fix" the matrix. Checking is pretty self-explanatory and will check if the matrix is of the selected option (only one operation can be used for a single matrix). Fixing a matrix will prompt for an operation and make the matrix represent that option (e.g. make an antisymmetric matrix symmetric).

After the results are printed, you can choose to go through another matrix (runs the program once again) or not (end the program).

#### Using Import

If you want to make your own uses or program to utilize the relation algorithms, simply import the relations.py file into your own program. 

With this method, the functions can each be used in whatever way is deemed necessary for the specific program. 

Understanding the uses of each function is easy as well. If it has "make" at the front, that means it takes in a matrix in the form of an NxN multidimensional list. If the function has "check" at the beginning, that means it will take in the same NxN matrix and return either true or false depending on the specific operation.

There is one exception to this, that being making a matrix antisymmetric. In this case, one function is named make_antisymmetric and another make_antisymmetric_double. The function with "double" in the name will remove both sides of any symmetry found (for example, if the coordinates (1,2) and (2,1) have a value of 1, that means it will make both positions a 0 instead of just one).

Important things to remember is that the matrix must be N-height and the same N-width. The values inside must also be "1" or "0"; they can be strings of those numbers, but they **MUST ONLY** contain "1" or "0" otherwise the algorithm will break.

### Test Cases

Tests for the relations.py algorithms are contained within the test_relations.py file. Each function inside relations.py has its own class named after which algorithm it is testing.

To run the test cases, use an IDE's inbuilt file running method so you are able to view the results of the tests. Those results should show that 83 tests pass successfully.

### Required Dependencies

- Kivy - for use in the GUI version of the app 

- unittest - for test cases in the test_relations.py
