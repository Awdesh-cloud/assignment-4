print("Task 6: Read File Safely (Error Handling Inside File Handling Only")

# 1. Ask the user for a filename to open.
# 2. Read and print the file if it exists.
# 3. If the file does not exist, print:
#    "File not found. Please check the filename."
# 4. Note: Simple condition checks with os.path.exists() are allowed.

import os

# Ask the user for a filename
filename= input("Please enter the file name")
print(os.getcwd())


# Add .txt if missing
if not filename.endswith(".txt"):
    filename+=".txt"

if os.path.exists(filename):
    with open(filename,"r") as f:
        print("\n File content\n")
        for line in f:
            print(line.strip())
else:
    print("File not found, Please check the file name")