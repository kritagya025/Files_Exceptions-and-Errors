# Task 2: Write and Append Data to a File

with open("output.txt","a+") as f:

    content=input("Enter text to write to the file: ")
    f.write(content+"\n")

    print("Data successfully written to output.txt.")

    print()
    print()

    additional_content=input("Enter additional text to append: ")
    f.write(additional_content+"\n")

    print()
    print()

    f.seek(0)
    print("Final content of output.txt:")
    output=f.read()
    print(output)