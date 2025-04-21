# Task 1: Read a File and Handle Errors

try:
    with open("sample.txt","r") as f:
        content=f.read()
        print(content)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")