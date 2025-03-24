'''
Implements a library database which supports adding books
to a given text file and printing the existing books to the command line.
'''

import sys
from typing import List

def main():
    '''Main function.'''
    if len(sys.argv) != 2:
        error_msg = "Incorrect number of input arguments."
        quit_program(error_msg)

    file_path = sys.argv[1]

    try:
        file = open(file_path, 'r+', encoding="utf-8")
    except IOError:
        error_msg = "Error opening the file."
        quit_program(error_msg)

    #Keep track of the current contents of the file.
    #Minimizes the need for reading the file.
    contents = []
    for line in file.readlines():
        contents.append(line.strip())

    #start to process user input
    ans = read_main_input()
    while ans not in ("Q", "q"):
        if ans == "1":
            add_book(file, contents)
        elif ans == "2":
            print_books(contents)
        else:
            print("\nProvide proper input.")

        ans = read_main_input()
    quit_program()

def add_book(file, contents: List[str]):
    '''
    Starts the process of adding a book to the database.
    Asks for needed user input, prints the result, and
    calls the write_to_file function.
    '''
    title = input("\nGive the name of the book: ")
    writer = input("Give the name of the writer: ")
    isbn = input("Give the ISBN of the book: ")
    year = input("Give the puhlishing year of the book: ")
    while not check_int(year):
        year = input("Give the publishing year of the book: ")

    record = title + "/" + writer + "/" + isbn + "/" + year
    print_books([record])
    update = input("\nDo you want to add the book to the database? (y/n): ")

    while update not in ('y', 'n'):
        print("\nProvide a proper answer.")
        update = input("\nDo you want to update the database? (y/n): ")
    if update == "n":
        print("\nThe book was not added to the database.")
        return
    write_to_file(file, record, contents)

def write_to_file(file, record: str, contents: List[str]):
    """
    Writes a given record to the database contents and the file.
    Uses binary search to insert the record at correct index.
    """
    file.seek(0)
    left = 0
    right = len(contents)-1
    record_year = int(record.split("/")[3])

    while left <= right:
        guess_idx = (left+right)//2
        guess_year = int(contents[guess_idx].split("/")[3])
        if guess_year <= record_year:
            left = guess_idx+1
        else:
            right = guess_idx-1

    contents.insert(left, record)
    file.write("\n".join(contents)+"\n")
    print("\nThe book was added to the database!")


def read_main_input() -> str:
    '''
    Prints the user's choices and returns the given input.
    '''
    print("\nSelect one of the following choices:")
    print("1) Add a new book.")
    print("2) Print the current database.")
    print("Q) Exit the program.")
    return input("Type 1, 2, or Q: ")

def print_books(contents: List[str]):
    '''
    Prints the stored books in the parameter contents.
    '''
    headers = ["Title", "Writer", "ISBN", "Year"]
    col_space = [70, 40, 20, 10]
    header_length = len(headers)
    print("")
    for i in range(header_length):
        print(f"{headers[i] :<{col_space[i]}}", end='')
    print("")
    print("-" * sum(col_space))
    for book in contents:
        info = book.split("/")
        for i in range(header_length):
            print(f"{info[i] :<{col_space[i]}}", end='')
        print("")

def check_int(value: str) -> bool:
    '''
    Tries to cast the given user input as an integer.

    Args:
        value (str): User input.
    Returns:
        bool: if casting was successful.
    '''
    is_int = True
    try:
        int(value)
    except ValueError:
        print("\nValue was not an integer!")
        is_int = False
    return is_int


def quit_program(error_msg = ""):
    '''
    Quits the program with a given error message or
    no message if quitting is from a user input ('Q').
    '''
    print(error_msg)
    print("Exiting program...")
    sys.exit()

if __name__ == "__main__":
    main()
