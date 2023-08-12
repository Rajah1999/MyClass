# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Raj>,<8-9-2023>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "C:\\Python\\_PythonClass\\Assignment05\\ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
File = None
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        File = open(objFile, "r")
        for row in File:
            lstTable = row.split(",")
            dicRow = {"ID": lstTable[0], "Task": lstTable[1], "Priority": lstTable[2].strip()}
            print(dicRow)
        File.close()
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        File = open(objFile, "a")
        IDinfo = input("Enter an ID: ")
        TaskName = input("Enter Task: ")
        TaskPriority = input("Enter priority level: ")
        lstTable = [IDinfo, TaskName, TaskPriority]
        dicRow = {"ID":lstTable[0], "Task": lstTable[1], "Priority": lstTable[2]}
        File.write(dicRow["ID"] + "," + dicRow["Task"]+ "," + dicRow["Priority"] + "\n")
        File.close()
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        IDinfo = input("Enter an ID to remove: ")
        lstTable = []
        File = open(objFile, "r")
        for row in File:
            lstRow = row.split(",")
            if lstRow[0] != IDinfo:
                lstTable.append(row)
        File.close()
        File = open(objFile, "w")
        for row in lstTable:
            File.write(row)
        File.close()
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        File = open(objFile, "w")
        for row in lstTable:
            lstRow = row.split(",")
            File.write(lstRow[0] + "," + lstRow[1] + "," + lstRow[2].strip() + "\n")
        File.close()
        print("Data saved to file!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program
