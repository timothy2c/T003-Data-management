# P3 Task 2: Milestone 2's Final Team Code -- Function Definitions

# T003:
# Authors:
# Karran Dhillon (101229275)
# Toniloba Kumapayi (101236693)
# Robert Forward (101224089)
# Timothy Chang (101222138)

# --Imports--
import string

# --Function Definitions--
# Conversions dictionary to a list
def to_list(book_dict: dict) -> list[dict]:
    """
    Returns a list of the book data, based on the "book_dict" dictionary argument
    
    Written by: All T003 Group members
    
    Preconditions: book_dict is inputed as a dictionary with keys as the category
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset_unsorted.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> to_list(booK_dict)
    [{'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English',
    'rating': 4.2, 'publisher': 'Vintage', 'page_count': 32, 'generes': 'Social Science'},
    {'title': 'Happy: Why More or Less Everything is Absolutely Fine', 'author': 'Derren Brown',
    'language': 'English', 'rating': 4.0, 'publisher': 'Random House', 'page_count': 576, 'generes': 'Social Science'},
    {'title': 'Freakonomics Rev Ed: A Rogue Economist Explores the Hidden Side of Everything',
    'author': 'Steven D. Levitt', 'language': 'English', 'rating': 3.8, 'publisher': 'Harper Collins', 'page_count': 336, 'generes': 'Social Science'},
    {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Management'}, 
    {another book element}
    ...
    ]
    
    >>> file_name = 'Google_Books_Dataset_another_book.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> to_list(book_dict)
    [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English',
    'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'generes': 'Comics'},
    {'title': 'Young Justice Vol. 1', 'author': 'Art Baltazar', 'language': 'English',
    'rating': 4.1, 'publisher': 'DC', 'page_count': 164, 'generes': 'Comics'}, 
    {'title': 'Ultimate Spider-Man Vol. 11: Carnage', 'author': 'Brian Michael Bendis',
    'language': 'English', 'rating': 4.1, 'publisher': 'Marvel Entertainment', 'page_count': 144, 'generes': 'Comics'},
    {'title': 'Immortal Hulk Vol. 1: Or Is He Both?', 'author': 'Al Ewing', 'language': 'English', 'rating': 4.4,
    'publisher': 'Marvel Entertainment', 'page_count': 128, 'generes': 'Comics'}, {'title': 'Watchmen (2019 Edition)',
    'author': 'Alan Moore', 'language': 'English', 'rating': 4.2, 'publisher': 'DC Comics', 'page_count': 448, 'generes': 'Comics'},
    {'title': 'The Joker', 'author': 'Brian Azzarello', 'language': 'English', 'rating': 4.4, 'publisher': 'DC', 'page_count': 130, 'generes': 'Comics'},
    {another book element}
    ...
    ]
    """
    book_list = [] # Initalize empty dictionary with book information
    for key, books in book_dict.items():
        for book in books: # Each book in the list
            book.update({"generes": key}) # Append the genre to the book
            book_list.append(book) # Each categories respective books
            # Genre is a key characteristic that differentitates books with the same title    
    return book_list

# Function 1 (Developed by Robert Forward (101224089))
def sort_books_title(dictionary:dict) ->list[dict]:
    """
    Takes parameter dictionary, where books are stored. Returns a list of book
    data, where the books are sorted alphabetically by title.
   
    Written by Robert Forward 101224089
    
    >>>sort_books_title(load_dataset('T003_Google_Books_Dataset_fxn1_case1_unsort.csv'))
    [{'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'generes': 'Fiction'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'generes': 'Fiction'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'page_count': 368, 'generes': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'generes': 'Comics'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'generes': 'Fiction'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'generes': 'Economics'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'language': 'English', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'generes': 'Psychology'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'page_count': 176, 'generes': 'Business'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'generes': 'Fiction'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Economics'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'page_count': 224, 'generes': 'Business'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'generes': 'Fiction'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': '', 'publisher': 'Hachette UK', 'page_count': 384, 'generes': 'Fiction'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'generes': 'Detective'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'generes': 'Fiction'}]
   
    >>>sort_books_title(load_dataset('T003_Google_Books_Dataset_fxn1_case2_unsort.csv'))
    [{'title': 'A Trace of Vice (a Keri Locke Mystery--Book #3)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.8, 'publisher': 'Blake Pierce', 'page_count': 250, 'generes': 'Fiction'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 240, 'generes': 'Detective'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 240, 'generes': 'Fiction'}, {'title': "Final Option: 'The best one yet'", 'author': 'Clive Cussler', 'language': 'English', 'rating': 5.0, 'publisher': 'Penguin UK', 'page_count': 400, 'generes': 'Crime'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'language': 'English', 'rating': 4.0, 'publisher': 'Kensington Books', 'page_count': 288, 'generes': 'Detective'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'generes': 'Mystery'}, {'title': 'Platform Revolution: How Networked Markets Are Transforming the Economyâ€”and How to Make Them Work for You', 'author': 'Geoffrey G. Parker', 'language': 'English', 'rating': 4.5, 'publisher': 'W. W. Norton & Company', 'page_count': 256, 'generes': 'Business'}, {'title': 'The Black Box', 'author': 'Michael Connelly', 'language': 'English', 'rating': 4.0, 'publisher': 'Hachette UK', 'page_count': 448, 'generes': 'Fiction'}, {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields', 'language': 'English', 'rating': '', 'publisher': 'AMACOM', 'page_count': 320, 'generes': 'Business'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'language': 'English', 'rating': 3.8, 'publisher': 'Penguin', 'page_count': 272, 'generes': 'Business'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'language': 'English', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'generes': 'Classics'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'language': 'English', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'generes': 'Fantasy'}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'generes': 'Fiction'}, {'title': 'Total Control', 'author': 'David Baldacci', 'language': 'English', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'generes': 'Mystery'}, {'title': 'Watching (The Making of Riley Paigeâ€”Book 1)', 'author': 'Blake Pierce', 'language': 'English', 'rating': 4.6, 'publisher': 'Blake Pierce', 'page_count': 250, 'generes': 'Mystery'}]
    """
    book_list = to_list(dictionary) # book list of the data
        
    for i in range(len(book_list)): #iterates over all elements in the list
        for elem in range(0, len(book_list)-i-1):
            book1 = book_list[elem].get('title').strip(string.punctuation) #Finds the title of the book, removes punctuation
            book2 = book_list[elem+1].get('title').strip(string.punctuation) #Finds the title of the next book, removes punctuation
            if book1 > book2: #If the first book comes after the second book alphabetically, swaps their order in the list
                book_list[elem], book_list[elem+1] = book_list[elem+1], book_list[elem]
            elif book1 == book2: #If the two books are the same with different genres
                book1 = book_list[elem].get('generes').strip(string.punctuation) #Finds the genre of the book
                book2 = book_list[elem+1].get('generes').strip(string.punctuation) #Finds the genre of the next book
                if book1 > book2: #If the first book's genre comes after the second book's genre alphabetically, swaps their order in the list
                    book_list[elem], book_list[elem+1] = book_list[elem+1], book_list[elem]                
    print(book_list)
    return book_list

# Function 2 (Developed by Timothy Chang (101222138))
def sort_books_ascending_rate(book_dict: dict) -> list[dict]:
    """
    Returns a list of books sorted by ratings in ascending order
    based on a given book dictionary. The book dictionary must
    have a key called 'rating'.
    
    Author: Timothy Chang (101222138)
    
    >>> sort_books_ascending_rate(book_dict)
    [{'title': 'Business Strategy (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English', 'rating': 0, 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Business'}, 
    ...
    {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'generes': 'Mystery'}, 
    ...
    {'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'page_count': 40, 'generes': 'Traditional'}]
    
    >>> sort_books_ascending_rate(load_dataset('T003_fxn2_unsorted_book_dict1.csv'))
    [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy',
    'language': 'English', 'rating': 0, 'publisher': 'AMACOM', 'page_count': 112, 'generes': 'Economics'},
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham',
    'author': 'John Grisham', 'language': 'English', 'rating': 0, 'publisher': 'Hachette UK', 'page_count': 384, 'generes': 'Fiction'},
    {another book element}
    ...]
    """
    # Adding each book to a list
    book_list = to_list(book_dict) # Refaactored code
    
    # now we have each book in the dictionary in the form of a list of dictionaries
    # sorting in ascending rate using bubble sort
    
    # we need to set books with ratings of '' to 0 before sorting
    for book in book_list: # for each book in the list
        if book.get('rating') == '': # if it has a rating of ''
            book['rating'] = 0 # set it to 0

    # bubble sort the book_list
    length = len(book_list) 
    for i in range(length):
        for j in range(0, length-i-1):
            if book_list[j].get("rating") == book_list[j+1].get("rating"):
                # Same rating -- sort by title
                if book_list[j].get("title") > book_list[j+1].get("title"):
                    book_list[j], book_list[j+1], = book_list[j+1], book_list[j]
                    
                elif book_list[j].get("title") == book_list[j+1].get("title"): 
                    # Sort by generes if they have the same titles
                    if book_list[j].get("generes") > book_list[j+1].get("generes"):
                        book_list[j], book_list[j+1], = book_list[j+1], book_list[j]            
            elif book_list[j].get("rating") > book_list[j+1].get("rating"):
                book_list[j], book_list[j+1], = book_list[j+1], book_list[j]
            
    
    print(book_list) # print the sorted list
    
    return book_list

# Function 3 (Developed by Timothy Chang (101222138))
def sort_books_descending_rate(book_dict: dict) -> list[dict]:
    """
    Returns a list of books sorted by ratings in descending order
    based on a given book dictionary. The book dictionary must
    have a key called 'rating'.
    
    Author: Timothy Chang (101222138)
    
    >>> sort_books_descending_rate(load_dataset('Google_Books_Dataset.csv'))
    [{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie', 'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'page_count': 40, 'generes': 'Detective'}, 
    ...
    {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8, 'publisher': 'Kensington Books', 'page_count': 288, 'generes': 'Detective'}, 
    ...
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'language': 'English', 'rating': 0, 'publisher': 'Hachette UK', 'page_count': 384, 'generes': 'Legal'}]
    
    >>> sort_books_descending_rate(load_dataset('T003_fxn3_unsorted_book_dict1.csv')
    [{'title': 'The Red Signal: An Agatha Christie Short Story', 'author': 'Agatha Christie',
    'language': 'English', 'rating': 5.0, 'publisher': 'HarperCollins UK', 'page_count': 40,
    'generes': 'Detective'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson',
    'language': 'English', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'generes': 'Adventure'},
    {'title': 'Shantaram', 'author': 'Gregory David Roberts', 'language': 'English', 'rating': 4.5,
    'publisher': 'Hachette UK', 'page_count': 944, 'generes': 'Detective'},
    {another book elements}
    ...]
    """
    # Adding each book to a list
    book_list = to_list(book_dict) # Refaactored code
    
    # now we have each book in the dictionary in the form of a list of dictionaries
    # sorting in ascending rate using bubble sort
    
    # we need to set books with ratings of '' to 0 before sorting
    for book in book_list: # for each book in the list
        if book.get('rating') == '': # if it has a rating of ''
            book['rating'] = 0 # set it to 0

    # bubble sort the book_list
    length = len(book_list) 
    for i in range(length):
        for j in range(0, length-i-1):
            if book_list[j].get("rating") == book_list[j+1].get("rating"):
                
                if book_list[j].get("title") > book_list[j+1].get("title"):
                    book_list[j], book_list[j+1], = book_list[j+1], book_list[j]
                    
                elif book_list[j].get("title") == book_list[j+1].get("title"):
                
                    if book_list[j].get("generes") > book_list[j+1].get("generes"):
                        book_list[j], book_list[j+1], = book_list[j+1], book_list[j]
                        
            elif book_list[j].get("rating") < book_list[j+1].get("rating"):
                book_list[j], book_list[j+1], = book_list[j+1], book_list[j]
    
    print(book_list) # print the sorted list
    return book_list    

# Function 4 (Developed by Karran Dhillon (101229275))
def sort_books_publisher(book_dict: dict) -> list[dict]:
    """
    Returns a list with the book data stored as a dictionary sorted in alphabetical
    order relative to the publisher, based on the "book_dict" dictionary argument
    
    Precondition: book_dict is inputted as a dictionary with keys as the category
    
    Written by: Karran Dhillon 101229275
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset_unsorted.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> sort_books_publisher(book_dict)
    The books sorted alphabetically by publisher:
    ------------------------------------
    {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112}, 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski',
    'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'generes': 'Fiction', 'page_count': 400},
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham',
    'author': 'John Grisham', 'language': 'English', 'rating': '', 'publisher': 'Hachette UK', 'generes': 'Fiction', 'page_count': 384},
    {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0,
    'publisher': 'Harper Collins', 'generes': 'Fiction', 'page_count': 336},
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker',
    'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'generes': 'Business', 'page_count': 224},
    {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'generes': 'Fiction', 'page_count': 416},
    {another book element}
    ...
    
    [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112}, 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski',
    'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'generes': 'Fiction', 'page_count': 400},
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham',
    'author': 'John Grisham', 'language': 'English', 'rating': '', 'publisher': 'Hachette UK', 'generes': 'Fiction', 'page_count': 384},
    {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'language': 'English', 'rating': 4.0,
    'publisher': 'Harper Collins', 'generes': 'Fiction', 'page_count': 336},
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker',
    'language': 'English', 'rating': 4.6, 'publisher': 'Harper Collins', 'generes': 'Business', 'page_count': 224},
    {'title': 'After Anna', 'author': 'Alex Lake', 'language': 'English', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'generes': 'Fiction', 'page_count': 416},
    {another book element}
    ...]
    
    >>> file_name = 'Google_Books_Dataset_unsorted_case2.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> sort_books_publisher(book_dict)
    The books sorted alphabetically by publisher:
    ------------------------------------
    {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112},
    {'title': 'Rework', 'author': 'Jason Fried', 'language': 'English', 'rating': 4.1, 
    'publisher': 'Currency', 'generes': 'Economics', 'page_count': 288}, 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski',
    'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'generes': 'Mythical Creatures', 'page_count': 400},
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham',
    'author': 'John Grisham', 'language': 'English', 'rating': '', 'publisher': 'Hachette UK', 'generes': 'Thrillers', 'page_count': 384},
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further',
    'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'generes': 'Economics', 'page_count': 30},
    {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'language': 'English', 'rating': 4.7,
    'publisher': 'Hachette UK', 'generes': 'Fantasy', 'page_count': 688}, 
    {another book element}
    ...
    
    [
    {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112},
    {'title': 'Rework', 'author': 'Jason Fried', 'language': 'English', 'rating': 4.1, 
    'publisher': 'Currency', 'generes': 'Economics', 'page_count': 288}, 
    {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski',
    'language': 'English', 'rating': 4.8, 'publisher': 'Hachette UK', 'generes': 'Mythical Creatures', 'page_count': 400},
    {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham',
    'author': 'John Grisham', 'language': 'English', 'rating': '', 'publisher': 'Hachette UK', 'generes': 'Thrillers', 'page_count': 384},
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further',
    'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'generes': 'Economics', 'page_count': 30},
    {'title': 'The Way Of Shadows: Book 1 of the Night Angel', 'author': 'Brent Weeks', 'language': 'English', 'rating': 4.7,
    'publisher': 'Hachette UK', 'generes': 'Fantasy', 'page_count': 688}, 
    {another book element}
    ...
    ],
    """
    book_list = to_list(book_dict) # book list of the data
    
    length = len(book_list) # length of list
    for i in range(length):
        for elem in range(length-i-1): # Last i elements already in place
            # Swap elements if it is greater than adjacent
            if book_list[elem].get("publisher") == book_list[elem + 1].get("publisher"): # same publisher
                # sorting based on title when the page count is the same
                if book_list[elem].get("title") > book_list[elem + 1].get("title"):
                    book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]
            
                elif book_list[elem].get("title") == book_list[elem + 1].get("title"): # same titile
                    # sort by genre
                    if book_list[elem].get("generes") > book_list[elem + 1].get("generes"):
                        book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]                  
                
            # current element (and adjacent one) not alphabetically sorted
            elif book_list[elem].get("publisher") > book_list[elem + 1].get("publisher"):
                # swap their places
                book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]

    print("The books sorted alphabetically by publisher:")
    print("------"*6) # create some seperation
    for book in book_list: # print the book data
        print(book)
    
    return book_list

# Function 5 (Developed by Karran Dhillon (101229275))
def sort_books_pageCount(book_dict: dict) -> list[dict]:
    """
    Returns a list with the book data stored as a dictionary sorted in ascending
    order relative to the page count, based on the "book_dict" dictionary argument
    
    Precondition: book_dict is inputted as a dictionary with keys as the category
    
    Written by: Karran Dhillon 101229275
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset_unsort_case1.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> sort_books_pageCount(book_dict)
    The books sorted in ascending order based on page_count:
    ------------------------------------
    {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 
    'publisher': 'Marvel Entertainment', 'generes': 'Comics', 'page_count': 96}, 
    {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112},
    {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5,
    'publisher': 'Kogan Page Publishers', 'generes': 'Business', 'page_count': 176}, 
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English',
    'rating': 4.6, 'publisher': 'Harper Collins', 'generes': 'Business', 'page_count': 224}, 
    {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English',
    'rating': 4.8, 'publisher': 'Tor Books', 'generes': 'Fiction', 'page_count': 226},
    {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 
    'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'generes': 'Fiction', 'page_count': 288},
    {another book element}
    ...
    
    [
    {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'language': 'English', 'rating': 4.2, 
    'publisher': 'Marvel Entertainment', 'generes': 'Comics', 'page_count': 96}, 
    {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112},
    {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5,
    'publisher': 'Kogan Page Publishers', 'generes': 'Business', 'page_count': 176}, 
    {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'language': 'English',
    'rating': 4.6, 'publisher': 'Harper Collins', 'generes': 'Business', 'page_count': 224}, 
    {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'language': 'English',
    'rating': 4.8, 'publisher': 'Tor Books', 'generes': 'Fiction', 'page_count': 226},
    {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English',
    'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'generes': 'Fiction', 'page_count': 288},
    {another book element}
    ...
    ]
    
    >>> file_name = 'Google_Books_Dataset_unsort_case2.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> sort_books_pageCount(book_dict)
    The books sorted in ascending order based on page_count:
    ------------------------------------
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further',
    'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'generes': 'Economics','page_count': 30},
    {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English',
    'rating': 4.2, 'publisher': 'Vintage', 'generes': 'Social Science', 'page_count': 32}, 
    {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112}, 
    {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg',
    'language': 'English', 'rating': 5.0, 'publisher': 'Penguin', 'generes': 'Biography', 'page_count': 112},
    {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5,
    'publisher': 'Kogan Page Publishers', 'generes': 'Economics', 'page_count': 176},
    {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English',
    'rating': 4.4, 'publisher': 'HarperCollins UK', 'generes': 'Classics', 'page_count': 208},
    {another book element}
    ...
    
    [
    {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further',
    'author': 'Alvin Hall', 'language': 'English', 'rating': 3.7, 'publisher': 'Hachette UK', 'generes': 'Economics','page_count': 30},
    {'title': 'We Should All Be Feminists', 'author': 'Chimamanda Ngozi Adichie', 'language': 'English',
    'rating': 4.2, 'publisher': 'Vintage', 'generes': 'Social Science', 'page_count': 32}, 
    {'title': 'Management (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'language': 'English',
    'rating': '', 'publisher': 'AMACOM', 'generes': 'Economics', 'page_count': 112}, 
    {'title': 'No One Is Too Small to Make a Difference', 'author': 'Greta Thunberg',
    'language': 'English', 'rating': 5.0, 'publisher': 'Penguin', 'generes': 'Biography', 'page_count': 112},
    {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'language': 'English', 'rating': 3.5,
    'publisher': 'Kogan Page Publishers', 'generes': 'Economics', 'page_count': 176},
    {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'language': 'English',
    'rating': 4.4, 'publisher': 'HarperCollins UK', 'generes': 'Classics', 'page_count': 208},
    {another book element}
    ...
    ]
    """
    book_list = to_list(book_dict) # book list of the data
    
    # Bubble Sort
    length = len(book_list) # length of list
    for i in range(length): # current index
        for elem in range(length-i-1): # Last i elements already in place
            # Swap elements if it is greater than adjacent
            if book_list[elem].get("page_count") == book_list[elem + 1].get("page_count"): # same page_count
                # sort alphabetically by title if the same page count
                if book_list[elem].get("title") > book_list[elem + 1].get("title"):
                    book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]
                    
                elif book_list[elem].get("title") == book_list[elem + 1].get("title"): # same titile
                    # sort by genre
                    if book_list[elem].get("generes") > book_list[elem + 1].get("generes"):
                        book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]                    
            
            # current element has a higher page count then the next element
            elif book_list[elem].get("page_count") > book_list[elem + 1].get("page_count"):
                # flip places 
                book_list[elem], book_list[elem + 1] = book_list[elem + 1], book_list[elem]
    
    print("The books sorted in ascending order based on page_count:")
    print("------"*6) # create some seperation
    for book in book_list: # print the book data
        print(book)
    
    return book_list    

# Function 6 (Developed by Toniloba Kumapayi (101236693))
def sort_books_category(dictionary: dict)-> list[dict]:
    """
    Returns a list with the book data stored as a dictionary book where the book are sorted alphabetically by category.
    Function prints the book data of such list.
    
    Written by: Toniloba Kumapayi (101236693)
    
    >>>sort_books_category(book_list_dictionary('Google_Books_Dataset.csv'))
    book_list= [{'title': 'A Feast for Crows (A Song of Ice and Fire, Book 4)',
             'author': 'George R.R. Martin',
             'rating': 4.5,
             'publisher': 'HarperCollins UK',
             'page_count': 864,
             'generes': 'Adventure'
             'language': 'English'}
             {'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)',
             'author': 'George R.R. Martin',
             'rating': 4.5, 
             'publisher': 'HarperCollins UK',
             'page_count': 4544,
             'generes': 'Adventure',
             'language': 'English'}
             ...
             {'title': 'The Red Signal: An Agatha Christie Short Story',
             'author':'Agatha Christie',
             'rating': 5.0,
             'publisher': 'HarperCollins UK',
             'page_count': 40,
             'generes': 'Traditional'
             'language': 'English'}
             ]are tested
    if the returns are the same for the expected and actual
             
    >>> sort_books_category(book_list_dictionary('T003_Milestone_2_Test1.csv.csv'))
    [{'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt',
    'language': 'English', 'rating': 4.6, 'publisher': 'HarperCollins Leadership',
    'page_count': 288, 'generes': 'Business'}, 
    {'title': 'The Essentials of Finance and Accounting for Nonfinancial Managers', 'author': 'Edward Fields',
    'language': 'English', 'rating': '', 'publisher': 'AMACOM', 'page_count': 320, 'generes': 'Business'},
    {'title': 'Antiques Con', 'author': 'Barbara Allan', 'language': 'English', 'rating': 4.8,
    'publisher': 'Kensington Books', 'page_count': 288, 'generes': 'Detective'},
    {another book element}
    ...]
    """
    book_list = to_list(dictionary)
    
    for i in range(len(book_list)): #loops through the list a number of times based on how many elements are in the list
        min_idx=i
        for j in range(1+i, len(book_list)): # compares with the element ahead of it
            if book_list[i]['generes']>book_list[j]['generes']: # compares the categories to see which is bigger
                temp=book_list[i] 
                min_idx=j
                book_list[i]=book_list[min_idx] # swaps the elements
                book_list[min_idx]=temp # stores a new key to compare with
            elif (book_list[i]['generes']==book_list[j]['generes']) and (book_list[i]['title'] > book_list[j]['title']):
                # criteria for when books are in same category but have different title, arranges them alphabetically
                temp=book_list[i]
                min_idx=j
                book_list[i]=book_list[min_idx] # swaps elements based on title
                book_list[min_idx]=temp #stores a new key to compare with
    print(book_list)# prints the book data
    return book_list #returns list