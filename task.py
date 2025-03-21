import sys
from typing import List

def main():

    if len(sys.argv) != 2:
        print("Incorrect number of input arguments.")
        quit_program()

    filePath = sys.argv[1]
    try:
        file = open(filePath, 'r+')
    except IOError:
        print("Error opening the file.")
        quit_program()

    #Keep track of the current contents of the file.
    #Minimizes the need for reading the file
    contents = []
    for line in file.readlines():
        contents.append(line.strip())

    #start to process user input
    ans = readUserInput()
    while ans != "Q":
        if ans == "1":
            addBook(file, contents)
        elif ans == "2":
            printBooks(contents)
        else:
            print("\nProvide proper input.")
        
        ans = readUserInput()
    quit_program()

def addBook(file, contents):
    title = input("\nGive the name of the book: ")
    writer = input("Give the name of the writer: ")
    isbn = input("Give the ISBN of the book: ")
    year = input("Give the puhlishing year of the book: ")
    while not checkInt(year):
        year = input("Give the publishing year of the book: ")
        
    record = title + "/" + writer + "/" + isbn + "/" + year
    printBooks([record])
    update = input("Do you want to add the book to the database? (y/n) ")

    while update != "y" and update != "n":
        print("Provide a proper answer.")
        update = input("Do you want to update the database? (y/n) ")
    if update == "n":
        print("Book was not added to the database.\n")
        return
    writeToFile(file, record, contents)
    
def writeToFile(file, record, contents):
    """
    Use binary search to find a location for the new record
    and insert at that location. Write the updated contents list
    to the file.
    """
    file.seek(0)
    left = 0
    right = len(contents)-1
    recordYear = int(record.split("/")[3])

    while left <= right:
        guessIdx = (left+right)//2
        guessYear = int(contents[guessIdx].split("/")[3])
        if guessYear <= recordYear:
            left = guessIdx+1
        else:
            right = guessIdx-1
        
    contents.insert(left, record)
    file.write("\n".join(contents)+"\n")
    print("Book added to the database!\n")


def readUserInput():
    print("Select one of the following choises:")
    print("1) Add new book")
    print("2) Print current database")
    print("Q) Exit the program")
    return input("Type 1, 2, or Q: ")

def printBooks(contents: List[str]):
    '''
    Variable colSpace is used to assign a number of characters for the headers and the 
    data below them. Helps with formatting the print. 
    '''
    headers = ["Title", "Writer", "ISBN", "Year"]
    colSpace = [50, 30, 20, 10]
    print("")
    for i in range(len(headers)):
        print(f"{headers[i] :<{colSpace[i]}}", end='')
    print("")
    print("-" * sum(colSpace))
    for book in contents:
        info = book.split("/")
        for i in range(len(headers)):
            print(f"{info[i] :<{colSpace[i]}}", end='')
        print("")
    print("")

def checkInt(value: str):
    isInt = True
    try:
        int(value)
    except ValueError:
        print("Value was not an integer!")
        isInt = False
    return isInt


def quit_program():
    print("Exiting program...")
    sys.exit()

if __name__ == "__main__":
    main()