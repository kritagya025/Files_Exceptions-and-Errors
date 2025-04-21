File Handling in Python
==============================================

This Python script set contains two basic file handling tasks:

------------------------------------------------------------
Task 1: Read a File and Handle Errors
------------------------------------------------------------

Description:
- Tries to open a file named 'sample.txt' in read mode.
- If the file exists, it reads and prints its content.
- If the file is not found, it catches the FileNotFoundError and displays a user-friendly message.

Sample Output:
Error: The file 'sample.txt' was not found.

------------------------------------------------------------
Task 2: Write and Append Data to a File
------------------------------------------------------------

Description:
- Opens (or creates) 'output.txt' in append + read mode (a+).
- Takes user input and writes it to the file.
- Takes additional input and appends that to the same file.
- Then reads and displays the full content of 'output.txt'.

Sample Input/Output:
Enter text to write to the file: Hello
Enter additional text to append: World

Final content of output.txt:
Hello
World

------------------------------------------------------------
Requirements:
- Python 3.x
- No external libraries needed

------------------------------------------------------------
How to Run:
1. Save the files as 'Task_1.py' and 'Task_2.py'.
2. Open a terminal or command prompt.
3. Run using:
   python Task_1.py
   python Task_2.py

------------------------------------------------------------
Notes:
- Make sure 'sample.txt' exists in the same directory before running Task 1, or it will display an error message.
- 'output.txt' will be created automatically if it doesn't already exist when running Task 2.
