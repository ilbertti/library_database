# Python library database

Implements a library for storing books in a given .txt file.
Uses Python version 3.10.7.

## Usage

Run the script from the command line and provide the library file:

```cmd
python library_db.py library.txt
```

The program prints instructions to the command line and asks for user input.
The user has 3 choices for input: '1', '2' and 'Q'.
- '1' Starts the process of adding a new book to the database.
The user needs to provide the following information:
    - The name of the book.
    - The name of the author.
    - The ISBN number of the book.
    - The release year of the book as an integer.

    After giving the information, the program asks if the information is correct (y/n):
    - 'y' adds the book to the database.
    - 'n' stops the process and returns to the main view.
- '2' prints the current database content.
- 'Q' exits the program.

## Properties/ToDo

The program makes some assumptions about the user syntax:
- The book title, writer, and ISBN can be anything that the user inputs.
    - The publishing year is checked to be an integer and can be negative.
- It is assumed that the provided file is empty or that it contains books in the proper format (title/writer/ISBN/year) and is sorted in an ascending order by the year.