## T003_data_analyzer Version 1.0 07/12/2021

The Project Leader can be reached at: <br />
**Name:** Karran Dhillon<br />
**Website:** https://carleton.ca/ <br />
**Email:** karrandhillon@cmail.carleton.ca <br />

## Description:
________________________
* The project contains several modules used for analyzing Excel (.csv) files,
including functions to find desired information, functions to sort through the dictionary,
modifying such dataset, and a User Interface (UI) that incorporates all functions. All of which 
are controlled based on the commands inputted by the user. 

* The project is made up of multiple files:
    * P5_T003_load_dataset.py                   
    * T003_P2_search_modify_dataset.py	  
    * T003_P3_sorting.py
    * T003_P2_booksUI.py

* The user is only concerned with the "T003_P2_booksUI.py" script

## Installation:

________________________
Python 3.7.6 or later must be installed. <br />
Only built-in Python modules are used. No external modules are required.


## Usage:

________________________
The User Interface incorporates all functions from the other modules; it provides access to all 
funtions in an easy to use interface. Consisting of 10 commands 
(command names are listed before the ')'), a .csv file must be loaded to the 
function first using the **"L"** (load) command assuming the file is in the same directory as the script. 
Typing **"Q"** at any point will terminate the program.

Below are two examples outlining basic commands with error-handling 
in sorting and finding a book title

**>>> python T003_P4_booksUI.py**

**#Example 1** <br />
Enter the letter(s) before the ')' <br />
1- Command Line L)oad file <br />
2- Command Line A)dd book <br />
3- Command Line R)emove book <br />
4- Command Line F)ind book by title <br />
5- Command Line NC) Number of books in a category <br />
6- Command Line CA) Categories for an author <br />
7- Command Line CB) Categories for a book title <br />
8- Command Line G)et Book <br />
    R)ate   A)uthor   P)ublisher   C)ategory <br />
    CT) Category and Title    CR) Category and Rate <br />
9- Command Line S)ort book <br />
    T)itle  R)ate) P)ublisher  C)ategory  PA)ageCount <br />
10-Command Line Q)uit <br />
: f <br />
Please enter the title of the book <br />
: After Anna <br />
The book has been found! <br />

**#Example 2** <br />
Enter the letter(s) before the ')' <br />
1- Command Line L)oad file <br />
2- Command Line A)dd book <br />
3- Command Line R)emove book <br />
4- Command Line F)ind book by title <br />
5- Command Line NC) Number of books in a category <br />
6- Command Line CA) Categories for an author <br />
7- Command Line CB) Categories for a book title <br />
8- Command Line G)et Book <br />
    R)ate   A)uthor   P)ublisher   C)ategory <br />
    CT) Category and Title    CR) Category and Rate <br />
9- Command Line S)ort book <br />
    T)itle  R)ate) P)ublisher  C)ategory  PA)ageCount <br />
10-Command Line Q)uit <br />
: s <br />
Enter another letter for the specific subcommand <br />
: R <br />
AS)ending rate  D)escending rate <br />
: AS <br/>
**The sorted book list by rate and ascending order is displayed here**

Input is taken after the colon. When asked for a rating or page count,
 **do not** enter a non-float or 
integer value respectively. The program is case-sensitive.

## Credits
________________________

#### Karran Dhillon 
    - book_tuple_dictionary
    - get_books_by_rate, check_category_and_title, get_author_categories
    - sort_books_publisher, sort_books_pageCount, test_sort_books_title
    - T003_P4_case3

#### Tim Chang 
    - book_dictionary_publisher_list
    - add_book, get_books_by_author, get_books_by_category
    - sort_books_ascending_rate, sort_books_descending_rate, test_sort_books_category
    - T003_P4_case4
    - P5_T003_load_dataset, T003_data_analyzer

#### Robert Forward 
    - book_category_dictionary_list
    - print_dictionary_category, find_books_by_title, all_categories_for_book_title
    - sort_books_title, test_sort_books_publisher, test_sort_books_pageCount
    - T003_P4_case1

#### Toniloba Kumapayi 
    - book_list_dictionary
    - remove_book, get_books_by_publisher, get_book_by_category_and_rate
    - sort_books_category, test_sort_books_ascending_rate, test_sort_books_descending_rate
    - T003_P4_case2

## License
________________________
Copyright 2021 Karran Dhillon, Tim Chang, Robert Forward, and Toniloba Kumapayi (T003). All rights reserved.

