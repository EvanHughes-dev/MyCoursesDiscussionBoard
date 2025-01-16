# My Courses Discussion Board
A lightweight Python script to clear all discussion posts on My Courses.

**As of version 1.0 of this project, only Chrome is supported but you only need to modify one line of code to use a different search engine**

## Setup:

1. Download the code either as a zip or by cloning the repo

2. Ensure Python in installed by running `python --version` in a command terminal 
    - If python is not installed, visit https://www.python.org/downloads/ to install
    - Make sure you allow the installer to save Python as a global variable

3. In a terminal, run `pip install selenium` to install the necessary library

## Execution

1. Locate the path to clearBoard.py file

2. In a command terminal, execute `python YOUR_PATH_HERE/clearBoard.py`
    - If an error occurs, make sure you have the correct file path and python was correctly installed by running `python --version` again

3. The terminal will prompt you for the URLs you want to clear. Enter each URL separated by a comma and press enter

4. The project will now launch Chrome. Due to security reasons, each time you run the program you will need to log into My Courses and use Duo Mobile

5. Once you have logged in the script will automatically complete the task and close itself once finished

