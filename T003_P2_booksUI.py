# P4 Task 2: Final Team Code

# December 9, 2021
# Version 1.0

# T003:
# Karran Dhillon (101229275)
# Toniloba Kumapayi (101236693)
# Robert Forward (101224089)
# Timothy Chang (101222138)

# --Constants--
CMD_PROMPT = ': ' # When grabbing user input

# --Imports--
import string # for string manipulation
from P5_T003_load_dataset import load_dataset
from T003_P2_search_modify_dataset import *
from T003_P3_sorting import *

# --Function Definitions--
def print_menu() -> None:
    """
    Prints the menu containing the list of commands that are valid
    
    Written by: All Members of the Team
    
    >>> print_menu()
    	1- Command Line L)oad file
	8- Command Line G)et Book
		R)ate   A)uthor   P)ublisher   C)ategory
		CT) Category and Title    CR) Category and Rate
	10-Command Line Q)uit
    """
    print("Enter the letter(s) before the ')'")
    print("1- Command Line L)oad file")
    print("2- Command Line A)dd book")
    print("3- Command Line R)emove book")
    print("4- Command Line F)ind book by title")
    print("5- Command Line NC) Number of books in a category")
    print("6- Command Line CA) Categories for an author")
    print("7- Command Line CB) Categories for a book title")
    print("8- Command Line G)et Book")
    print("\tR)ate   A)uthor   P)ublisher   C)ategory")
    print("\tCT) Category and Title    CR) Category and Rate")
    print("9- Command Line S)ort book")
    print("\tT)itle  R)ate) P)ublisher  C)ategory  PA)ageCount")
    print("10-Command Line Q)uit\n")
    
def input_type_check(expected_type: int, input_value: int) -> bool:
    """
    Checks whether or not an input is the proper type of the expected_type, works 
    for ints and floats
    
    Written by: Robert Forward (101224089)
   
    >>>input_type_check(int,5)
    True
    >>>input_type_check(int,4.5)
    False
    >>>input_type_check(float,5)
    False
    >>>input_type_check(float,'glue')
    False
    """
    if expected_type == float:
        for i in input_value:
            if i not in '1234567890.':
                return False
        return expected_type == type(float(input_value))
    elif expected_type == int:
        for i in input_value:
            if i not in '1234567890':
                return False        
        return expected_type == type(int(input_value))

def sub_commands(get_book: dict, book_dict: dict, key: str) -> dict: # Executes the command
    """
    Based on the book_dict dictionary argument, the subcommands of the function
    are executed. Returns the updated dictionary if add book command is called, otherwise,
    None is returned
    
    Preconditions: book_dict, get_book must be inputted as a dictionary, key is 
    a string of the command
    
    Written by: All Team Members
    
    **Input after the ': ' is by the user
    >>> book_dict = load_dataset('Google_Books_Dataset.csv')
    >>> get_book = {'G': {'A': get_books_by_author, 'P': get_books_by_publisher,
                'R': get_books_by_rate, 'C': get_books_by_category, 'CT': check_category_and_title,
                'CR': get_book_by_category_and_rate}}
    >>> sub_commands(get_book, book_dict, 'A')
    Please enter the author's name
    : Tor Books
    The author Tor Books has published the following books:
    
    >>> sub_commands(get_book, book_dict, 'CR')
    Please enter the categories name
    : Fiction
    Please enter the desired rate
    : 3
    The category Fiction and rating 3 has the following books :
    Antiques Roadkill: A Trash 'n' Treasures Mystery
    Bring Me Back
    Mrs. Pollifax Unveiled
    """
    if key == 'AD': # Add book (overlapping key as A)uthor under 'G' command)
        addbook_title = input('WHAT IS THE TITLE OF THE BOOK?\n: ')
        addbook_author = input('WHO IS THE AUTHOR OF THE BOOK?\n: ')
        addbook_rating = input('WHAT IS THE RATING OF THE BOOK?\n: ')
        while input_type_check(float, addbook_rating) == False:
            addbook_rating = input('INVALID INPUT\nWHAT IS THE RATING OF THE BOOK?\n: ')
        if float(addbook_rating) - 5 > 0.01:
            addbook_rating = input('INVALID INPUT\nWHAT IS THE RATING OF THE BOOK?\n: ')
        addbook_rating = round(float(addbook_rating),1)
        addbook_publisher = input('WHO IS THE PUBLISHER OF THE BOOK?\n: ')      
        addbook_pageCount = input('WHAT IS THE PAGE COUNT OF THE BOOK?\n: ')
        while input_type_check(int, addbook_pageCount) == False:
            addbook_pageCount = input('INVALID INPUT\nWHAT IS THE PAGE COUNT OF THE BOOK?\n: ')      
        addbook_pageCount = int(addbook_pageCount)      
        addbook_generes = input('WHAT IS THE GENRE OF THE BOOK?\n: ')       
        addbook_language = input('IN WHAT LANGUAGE IS THE BOOK WRITTEN?\n: ')   
        new_book = (addbook_title,addbook_author,addbook_language,addbook_publisher,addbook_generes,addbook_rating,addbook_pageCount,)
        main_dict = add_book(book_dict, new_book)
        return main_dict # return updated dictionary
    
    elif type(get_book.get('R', None)) == dict: # special case for sorting by rate 
        # There are repeated 'R' subcommands, this ensurs this is the correct one
        print("AS)ending rate  D)escending rate")
        cmd = input(CMD_PROMPT).upper().strip()
        while cmd not in get_book[key]: # until valid input
            print("No such command")
            cmd = input(CMD_PROMPT).upper().strip()
        
        get_book[key].get(cmd)(book_dict)
    
    elif key == 'A': # Get book by an author
        print("Please enter the author's name")
        get_book[key](input(CMD_PROMPT).strip(), book_dict)
        
    elif key == 'R': # Get books by rating
        print("Please enter the desired rate")
        get_book[key](int(input(CMD_PROMPT).strip()), book_dict)
        
    elif key == 'P': # Grab a book by publisher
        print("Please enter the publisher's name")
        get_book[key](input(CMD_PROMPT).strip(), book_dict) 
        
    elif key == 'C' or key == 'CR' or key == 'CT': # Grab books by Category
        print("Please enter the categories name")
        category = input(CMD_PROMPT).strip()
        if key == 'CR':
            print("Please enter the desired rate")
            get_book[key](category, int(input(CMD_PROMPT).strip()), book_dict)
        elif key == 'CT':
            print("Please enter the title's name")
            get_book[key](category, input(CMD_PROMPT).strip(), book_dict)
        else:
            get_book[key](category, book_dict)
            
def get_commands(commands: dict) -> None:
    """
    Grabs the desired command to be run from the user with error checking on commands,
    not on additonal paramters of the function definitions
    
    Preconditions: commands is a dictionary with keys as the corresponding command,
    and the values being the functions themselves
    
    Written by: All Team Members
    
    >>> commands = {'L': load_dataset, 'A': add_book, 'R': remove_book, 'F': find_books_by_title,
                'NC': print_dictionary_category, 'CA': get_author_categories, 'CB': all_categories_for_book_title,
                'G': {'A': get_books_by_author, 'P': get_books_by_publisher,
                'R': get_books_by_rate, 'C': get_books_by_category, 'CT': check_category_and_title,
                'CR': get_book_by_category_and_rate}, 'S': {'T': sort_books_title, 'R' : {'AS': sort_books_ascending_rate,
                                                                                          'D': sort_books_descending_rate}, 
                     'P' : sort_books_publisher, 'C' : sort_books_category,
                     'PA' : sort_books_pageCount}} # G has a subset of commands
                     
    >>> get_commands(commands)
    Enter the letter(s) before the ')'
    1- Command Line L)oad file
    2- Command Line A)dd book
    3- Command Line R)emove book
    4- Command Line F)ind book by title
    5- Command Line NC) Number of books in a category
    6- Command Line CA) Categories for an author
    7- Command Line CB) Categories for a book title
    8- Command Line G)et Book
            R)ate   A)uthor   P)ublisher   C)ategory
            CT) Category and Title    CR) Category and Rate
    9- Command Line S)ort book
            T)itle  R)ate) P)ublisher  C)ategory  PA)ageCount
    10-Command Line Q)uit

    : a
    No file loaded
    No such command
    --------------------------------------------------
    
    >>> get_commands(commands)
    Enter the letter(s) before the ')'
    1- Command Line L)oad file
    2- Command Line A)dd book
    3- Command Line R)emove book
    4- Command Line F)ind book by title
    5- Command Line NC) Number of books in a category
    6- Command Line CA) Categories for an author
    7- Command Line CB) Categories for a book title
    8- Command Line G)et Book
            R)ate   A)uthor   P)ublisher   C)ategory
            CT) Category and Title    CR) Category and Rate
    9- Command Line S)ort book
            T)itle  R)ate) P)ublisher  C)ategory  PA)ageCount
    10-Command Line Q)uit

    : l
    Enter the file name: Google_Books_Dataset.csv
    File loaded properly
    --------------------------------------------------
    """
    file_loaded = False # initially false
    print_menu() # Print the menu
    command = input(CMD_PROMPT).upper().strip() # Grab user input
    while command != 'Q': # Until quit is selected
        if command == 'L':
            file_name = input('Enter the file name: ').strip()
            book_dict = commands.get(command)(file_name) # Run load_dataset function
            print("File loaded properly")
            file_loaded = True
            
        elif command not in commands: # improper input, but file is loaded
            print("No such command")
            
        elif not file_loaded: # In case file is not loaded -- must be done first
            print("No file loaded")
            if command not in commands:
                print("No such command")
                          
        else: # File loaded and a proper command is selected
            if command == 'R' or command == 'F' or command == 'CB': # all books with title arguments
                print("Please enter the title of the book")
                title = input(CMD_PROMPT).strip() # Grab user input
                if command == 'R': # does not need category
                    print("Please enter the category of the book")
                    book_dict = commands[command](title, input(CMD_PROMPT).strip(), book_dict) # Store the book_dict
                else:
                    commands[command](title, book_dict) # covers F and CB commands
            
            elif command == 'A': # A lot of prompts, so it has it's own function
                book_dict = sub_commands(commands, book_dict, "AD") # overlapping 'A)' command
            
            elif command == 'NC': # Need category
                print("Please enter the category of the book")
                commands[command](input(CMD_PROMPT).strip(), book_dict) # Grab user input

            elif command == 'CA': # Need author
                print("Please enter the author of the book")
                commands[command](input(CMD_PROMPT).strip(), book_dict) # Grab user input
                
            elif command == 'G' or command == 'S': # These commands have sub commands
                print("Enter another letter for the specific subcommand")
                key = input(CMD_PROMPT).upper().strip() # Grab user input
                while key not in commands[command]: # Subset of commands
                    print("No such command")
                    print("Enter another letter for the specific get book")
                    key = input(CMD_PROMPT).upper().strip() # Grab user input                
                if command == 'S' and key != 'R': # R has a sub command prompt
                    commands[command].get(key)(book_dict)
                else:
                    sub_commands(commands[command], book_dict, key) # key-value pair
            
        print('-----'*10)
        print_menu() # Redisplay menu upon execution
        command = input(CMD_PROMPT).upper().strip() # Grab user input    

# --Main Script--
if __name__ == '__main__':
    commands = {'L': load_dataset, 'A': add_book, 'R': remove_book, 'F': find_books_by_title,
                'NC': print_dictionary_category, 'CA': get_author_categories, 'CB': all_categories_for_book_title,
                'G': {'A': get_books_by_author, 'P': get_books_by_publisher,
                'R': get_books_by_rate, 'C': get_books_by_category, 'CT': check_category_and_title,
                'CR': get_book_by_category_and_rate}, 'S': {'T': sort_books_title, 'R' : {'AS': sort_books_ascending_rate,
                                                                                          'D': sort_books_descending_rate}, 
                     'P' : sort_books_publisher, 'C' : sort_books_category,
                     'PA' : sort_books_pageCount}} # G and S have a subset of commands
    get_commands(commands) # Main command executions    