# P2 Task 3: Milestone 1's Final Team Code -- Function Definitions

# T003:
# Authors:
# Karran Dhillon (101229275)
# Toniloba Kumapayi (101236693)
# Robert Forward (101224089)
# Timothy Chang (101222138)

# --Imports--

# --Function Definitions--
# Function 1 (Developed by Robert Forward (101224089))
def print_dictionary_category(category:str, dictionary:dict) ->int:
    """
    Returns the number of books in dictionary associated with category
    
    Written by: Robert Forward (101224089)
   
    >>>print_dictionary_category('Business', load_dataset('Google_Books_Dataset.csv'))
    20
    >>>print_dictionary_category('Economics', load_dataset('Google_Books_Dataset.csv'))
    22
    >>>print_dictionary_category('Fiction', load_dataset('Google_Books_Dataset.csv'))
    39
    >>>print_dictionary_category('Marvel', load_dataset('Google_Books_Dataset.csv'))
    0
    """
    num_books = 0
    temp_list = []
    if category in dictionary: #If the category is in the dictionary
        genre = dictionary.get(category) #Finds the values associated with the category
        for i in genre:
            temp_list.append(i.get('title')) #adds each book title to a list
            num_books += 1 #adds 1 to the book counter
    result = ('The category ' + category + ' has ' + str(num_books) +
              ' books. This is the list of books in category ' + category
              + ':') #this will be printed
    for j in temp_list: #adds titles to the print statement
        result += '\n' + j
    print(result)
    return num_books

# Function 2 (Developed by Timothy Chang (101222138))
def add_book(book_dict: dict, book_info: tuple) -> dict:
    """
    Takes a dictionary where a book is to be added and a tuple including
    seven values (title, author, language, publisher, category, rating,
    page count). Returns the dictionary with the book added to or returns
    "there was an error adding the book" if the book is unable to be added
    to the dictionary.
    
    Written by: Timothy Chang (101222138)
    
    Preconditions:
    title, author, language, publisher, and category should be str values.
    rating should be a float value and page count should be an int.
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)
    >>> add_book(book_dict, ("title", "author", "language", "publisher", "category", 3.3, 100))
    {'Psychology': 
    [{'title': 'How To Win Friends and Influence People', 
    'author': 'Dale Carnegie', 
    'language': 'English', 
    'rating': 4.3, 
    'publisher': 'Simon and Schuster', 
    'page_count': 320}, {another element},
    ... 
    'Business': 
    [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 
    'author': 'T. Harv Eker', 
    'language': 'English', 
    'rating': 4.6, 
    'publisher': 
    'Harper Collins', 
    'page_count': 224}, {another element},
    ...
    'category': 
    [{'title': 'title', 
    'author': 'author', 
    'language': 'language', 
    'publisher': 'publisher', 
    'rating': 3.3, 
    'page_count': 100}]
    }
    "The book has been added correctly"
    
    >>> add_book(book_dict, ("title"))
        {'Psychology': 
    [{'title': 'How To Win Friends and Influence People', 
    'author': 'Dale Carnegie', 
    'language': 'English', 
    'rating': 4.3, 
    'publisher': 'Simon and Schuster', 
    'page_count': 320}, {another element},
    ... 
    'Business': 
    [{'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 
    'author': 'T. Harv Eker', 
    'language': 'English', 
    'rating': 4.6, 
    'publisher': 
    'Harper Collins', 
    'page_count': 224}, {another element},
    ...]}
    "There was an error adding the book"
    """
    if len(book_info) == 7: # if the tuple is the right size
        valid_tuple = True # determines if it is possible to add the book info to the dictionary
        for i in book_info[0:4]: # check to see if the title, author, language, publisher, and category are the right type
            if type(i) != str: # if they arent's set valid_tuple to false
                valid_tuple = False
        if type(book_info[5]) != float: # determines if the rating is the right type
            valid_tuple = False
        if type(book_info[6]) != int: # determines if the page count is the right type
            valid_tuple = False
        
        if valid_tuple == True: # if the above conditions are met
            book_titles = (("title", book_info[0]), ("author", book_info[1]), ("language", book_info[2]),
                     ("publisher", book_info[3]), ("generes", book_info[4]), ("rating", book_info[5]),
                     ("page_count", book_info[6]))
            book_info_dict = dict(book_titles)
            
            category = book_info_dict.get("generes") # finds the category of the book info
            del book_info_dict["generes"] # delete the category name since it will be the key value
            
            if book_dict.get(category) != None: # if the book category is already in the dictionary
                book_info_dict = book_dict.get(category).append(book_info_dict) # add the book info
                
            else: # if the book category is not in the dictionary
                book_dict[category] = [book_info_dict] # add a new dictionary list to the dictionary containing the book info
                
            print("The book has been added correctly")
            
        else: # if the tuple is not valid
            print("There was an error adding the book")
           
    else: # if the tuple is not the right size
        print("There was an error adding the book")
    return book_dict

# Function 3 (Developed by Toniloba Kumapayi (101236693))
def remove_book(book_title: str, category: str, dictionary:dict)-> dict:
    """
    Returns the updated dictionary with book removed from dictonary.
    Stating "The book has been removed correctly" or 
    "There was an error removing the book.Book not found"
    
    Written by: Toniloba Kumapayi (101236693)
    
    >>>remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction", load_dataset('Google_Books_Dataset.csv'))
    "The book has been removed correctly"

    >>>remove_book("After Anna", "lol", load_dataset('Google_Books_Dataset.csv'))
    "There was an error removng the book.Book not found"

    >>>remove_book("Firstborn Trilogy: The Final Empire", "Fantasy", load_dataset('Google_Books_Dataset.csv'))
    "There was an error removng the book.Book not found"
    """
    if category in dictionary: # checks if category in dictionary
        for book in dictionary.get(category): # gets the values in the dictionary
            if book.get('title') == book_title: #checks if book title is the same as one indictionary
                dictionary.get(category).remove(book) # removes book if meets the criteria
                print("The book has been removed correctly")
                return dictionary

    print( "There was an error removing the book. Book not found") # would print this if category not in book
    return dictionary

# Function 4 (Developed by Karran Dhillon (101229275))
def get_books_by_rate(rate: int, book_dict: dict) -> dict:
    """
    Returns a dictionary with all the books whose rating is the positive 
    integer argument "rate", based on the book dictionary inputted
    
    Written by: Karran Dhillon 101229275
    
    Preconditions: rate must be an integer > 0
    book_dict must be a dictionary with categories as the keys
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)

    >>> get_books_by_rate(3, book_dict)
    Title: "Antiques Roadkill: A Trash 'n' Treasures Mystery"
    Author: "Barbara Allan"
    Language: "English"
    Rating: 3.3
    Publisher: "Kensington Publishing Corp."
    Page_count: 288
    Category: "Fiction"
    
    Title: "Bring Me Back"
    Author: "B A Paris"
    Language: "English"
    Rating: 3.8
    Publisher: "HarperCollins UK"
    Page_count: 368
    Category: "Fiction"

    ...
    {1: {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': \
    'Barbara Allan', 'language': 'English', 'rating': 3.3, 'publisher': \
    'Kensington Publishing Corp.', 'page_count': 288}, 2: {'title': 'Bring Me Back',\
    'author': 'B A Paris', 'language': 'English', 'rating': 3.8, 'publisher': 'HarperCollins UK', \
    'page_count': 368}, {another element} ...}
    
    >>> get_books_by_rate(6, book_dict) # No book has a rating of 6
    No books with a rating of 6 found
    {}
    """
    books_passed = {} # Key = # appended (1, 2, 3, etc.), Value = book dictionary
    i = 1 # Key value to store in books_passed dictionary
    for category, books in book_dict.items(): # Each key-value pair of the dictionary
        for book in books: # Each book in the category
            current_book_rate = book.get("rating")
            
            if current_book_rate != '' and (rate <= current_book_rate < (rate + 1)): # Ensure rating is non-empty in order to use relational operator
                # No need to account for finite precision as all float ratings have 2 significant figures
                books_passed.update({i: book}) # add book to the rating passed list
                i += 1
                for key, value in book.items(): # print the book information
                    if key == "rating" or key == "page_count": # Values not enclosed with quotation marks
                        print(key.capitalize(), ': ', value, sep='') 
                    else:
                        print(key.capitalize(), ': "', value, '"', sep='')

                print('Category: "', category, '"\n', sep='') # Since category is not in book_dict, add
                
    if not len(books_passed): # No books have that desired rating
        print("No books with a rating of", rate, "found")
    
    return books_passed # Return dictionary with books with the given rating

# Function 5 (Developed by Robert Forward (101224089))
def find_books_by_title(book_title:str, dictionary:dict) ->bool:
    """
    Returns True if the title exists in the dictionary, False if it doesn't.
    
    Written by: Robert Forward (101224089)
   
    >>>find_books_by_title("Rework", load_dataset('Google_Books_Dataset.csv'))
    The book has been found!
    True
   
    >>>find_books_by_title("The Black Box", load_dataset('Google_Books_Dataset.csv'))
    The book has been found!
    True
   
    >>>find_books_by_title("Plagueis", load_dataset('Google_Books_Dataset.csv'))
    The book has NOT been found
    False
    """
    genre_books = dictionary.values() #creates a set of values
    for i in genre_books:
        for j in i:
            temp_title = j.get('title') #finds value associated with each title
            if temp_title == book_title: #if the title is the one we want
                print('The book has been found!') #The book is in the dictionary
                return True
    print('The book has NOT been found') #The book is not in the dictionary
    return False

# Function 6 (Developed by Timothy Chang (101222138))
def get_books_by_author(author: str, book_dict: dict) -> list:
    """
    Returns and prints a list of book titles based on a given author name and
    a given dictionary of books. Author name must be the author's full name,
    any punctuation must be included.
    
    Written by: Timothy Chang (101222138)
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)
    >>> get_books_by_author("Agatha Christie", book_dict)
    The author Agatha Christie has published the following books:
    1- The Red Signal: An Agatha Christie Short Story
    2- And Then There Were None
    3- The Mysterious Affair at Styles
    ['The Red Signal: An Agatha Christie Short Story', 'And Then There Were None', 'The Mysterious Affair at Styles']

    >>> get_books_by_author("dadawdadawd", book_dict)
    The author dadawdadawd has published the following books:
    []
    """
    book_titles = [] # stores all of the book titles
    for i in book_dict: # for each category
        for x in book_dict.get(i): # for each element in each dictionary list
            if x.get("author").lower() == author.lower() and x.get("title") not in book_titles: # checks if they're equal, not case sensitive, also checks for duplicates
                book_titles.append(x.get("title")) # adds the title of the book to the list
    print("The author " + (author) + " has published the following books:")
    for i in range(len(book_titles)):
        print(str(i+1) + "- " + book_titles[i])
    return book_titles

# Function 7 (Developed by Toniloba Kumapayi (101236693))
def get_books_by_publisher(publisher_name:str, dictionary:dict) -> list:
    """
    Returns a list of books' titles for a given publisher name. Prints the books 
    information for the publisher
    
    Written by: Toniloba Kumapayi (101236693)
    
    >>>get_books_by_publisher('AMACOM',load_dataset('Google_Books_Dataset.csv'))
    Marketing (The Brian Tracy Success Library)
    Management (The Brian Tracy Success Library)
    Business Strategy (The Brian Tracy Success Library)
    Personal Success (The Brian Tracy Success Library)
    The Essentials of Finance and Accounting for Nonfinancial Managers
    Business Strategy (The Brian Tracy Success Library)
    Personal Success (The Brian Tracy Success Library)
    The Essentials of Finance and Accounting for Nonfinancial Managers
    Management (The Brian Tracy Success Library)
    
    >>>get_books_by_publisher('HarperCollins UK',load_dataset('Google_Books_Dataset.csv'))
    The Mysterious Affair at Styles
    The Red Signal: An Agatha Christie Short Story
    The Mysterious Affair at Styles
    And Then There Were None
    The Red Signal: An Agatha Christie Short Story
    Predictably Irrational: The Hidden Forces that Shape Our Decisions
    The Painted Man (The Demon Cycle, Book 1)
    After Anna
    Bring Me Back
    The Red Signal: An Agatha Christie Short Story
    And Then There Were None
    The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King
    A Feast for Crows (A Song of Ice and Fire, Book 4)
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    The Mysterious Affair at Styles
    Prince of Thorns (The Broken Empire, Book 1)
    The Vagrant (The Vagrant Trilogy)
    The Mysterious Affair at Styles
    Bring Me Back
    After Anna
    And Then There Were None
    The Painted Man (The Demon Cycle, Book 1)
    A Feast for Crows (A Song of Ice and Fire, Book 4)
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    A Feast for Crows (A Song of Ice and Fire, Book 4)
    After Anna
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    Predictably Irrational: The Hidden Forces that Shape Our Decisions
    A Feast for Crows (A Song of Ice and Fire, Book 4)
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King
    The Vagrant (The Vagrant Trilogy)
    Prince of Thorns (The Broken Empire, Book 1)
    The Painted Man (The Demon Cycle, Book 1)
    Predictably Irrational: The Hidden Forces that Shape Our Decisions
    The Mysterious Affair at Styles
    The Red Signal: An Agatha Christie Short Story
    After Anna
    And Then There Were None
    Bring Me Back
    """
    lst=[]
    for book in dictionary.keys(): # gets the values
        booklist=dictionary.get(book) 
        for books in booklist:
            if books['publisher'] == publisher_name: #checks to see if publisher name 
                book_title=books['title'] # gets the book_title for the publisher name
                lst.append(book_title) #adds the book title to the list
    print("The publisher" + ' '+ publisher_name + ' '+ "has publsihed the followng books :")
    for i in lst:
        print(i)
    return lst

# Function 8 (Developed by Karran Dhillon (101229275))
def check_category_and_title(category: str, title: str, book_dict: dict) -> bool:
    """
    Returns True if the book's "title" argument, exists in the dictionary for the given "category"
    inputted. Returns False otherwise
    
    Written by: Karran Dhillon 101229275
    
    Preconditions: category and title are string arguments (case-sensitive)
    book_dict must be a dictionary with categories as the keys
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> check_category_and_title('Fiction', "Edgedancer: From the Stormlight Archive", book_dict)
    The category "Fiction" HAS the book title "Edgedancer: From the Stormlight Archive"
    True
    
    >>> check_category_and_title('Humor', "Tall Tales and Thee Stories: The Best of Billy Connolly", \
    book_dict) # Title name does not exist in humor
    The category "Humor" does not have the book title "Tall Tales and Thee Stories: The Best of Billy Connolly"
    False
        
    >>> check_category_and_title('Non-Fiction', 'Antiques Con', book_dict) # No non-fiction category
    The category "Non-Fiction" does not have the book title "Antiques Con"
    False
    """
    for book in book_dict.get(category, []): # for each book in the given category
        # If no category key exists, the list is still iterable over an empty interval
        if book.get("title") == title: # If the title exists, the if statement is True
            print('The category "', category, '" has the book title "', title, '"', sep='') 
            return True
    
    # No book found 
    print('The category "', category, '" does not have the book title "', title, '"', sep='')
    return False

# Function 9 (Developed by Robert Forward (101224089))
def all_categories_for_book_title(book_title:str, dictionary:dict) ->list:
    """
    Returns a list of categories for the given title as a case-sensitive string
    argument
    
    Written by: Robert Forward (101224089)
   
    >>>all_categories_for_book_title("Antiques Roadkill: A Trash 'n' Treasures Mystery", load_dataset('Google_Books_Dataset.csv'))
    The book title 'Antiques Roadkill: A Trash 'n' Treasures Mystery' has the following categories:
    1- Detective
    2- Fiction
    3- Mystery
    ['Detective', 'Fiction', 'Mystery']
   
    >>>all_categories_for_book_title("We", load_dataset('Google_Books_Dataset.csv'))
    The book title 'We' has the following categories:
    1- Fiction
    2- Fantasy
    ['Fiction', 'Fantasy']
   
    >>>all_categories_for_book_title("Lost Stars", load_dataset('Google_Books_Dataset.csv'))
    The book title 'Lost Stars' is not in the dictionary
    []
   
    """
    temp_list = []
    for i in dictionary: #For every genre in the dictionary
        for j in dictionary.get(i): #For every title for the genre
            if j.get('title') == book_title: #If the title matches the one we're looking for
                temp_list.append(i) #The genre gets added to a list
    if temp_list: #If the list is not empty, the book is in the dictionary
        print('The book title ' + "'" + book_title + "'" +
                 ' has the following categories:')
    else: #If the list is empty, the book is not in the dictionary
        print('The book title ' + "'" + book_title + "'" +
                 ' is not in the dictionary')
    num_genre = 1
    for genre in temp_list:
        print(str(num_genre) + '- ' + temp_list[num_genre - 1])
        num_genre += 1
    return temp_list

# Function 10 (Developed by Timothy Chang (101222138))
def get_books_by_category(category: str, book_dict: dict) -> list:
    """
    Returns and prints a list of book titles based on a given category
    and a given dictionary of books. Category is case sensitive.
    
    Written by: Timothy Chang (101222138)
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)
    >>> get_books_by_category("Adventure", book_dict)
    The category Adventure has the following books:
    1- Sword of Destiny: Witcher 2: Tales of the Witcher
    2- A Feast for Crows (A Song of Ice and Fire, Book 4)
    3- After Anna
    4- The Way Of Shadows: Book 1 of the Night Angel
    5- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    6- Edgedancer: From the Stormlight Archive
    7- The Malady and Other Stories: An Andrzej Sapkowski Sampler
    ['Sword of Destiny: Witcher 2: Tales of the Witcher', 'A Feast for Crows (A Song of Ice and Fire, Book 4)', 'After Anna', 'The Way Of Shadows: Book 1 of the Night Angel', 
    'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 
    'Edgedancer: From the Stormlight Archive', 'The Malady and Other Stories: An Andrzej Sapkowski Sampler']
    
    >>> get_books_by_category("adventure", book_dict)
    []
    """
    
    book_titles = [] # stores all of the book titles
    if book_dict.get(category) != None: # if the category has values in it
        for i in book_dict.get(category): # go through each value and add the book title to list
            if i.get("title") not in book_titles: # make sure there's no duplicates
                book_titles.append(i.get("title"))
        print("The category " + category + " has the following books:") # print each book title
        for i in range(len(book_titles)):
            print(str(i+1) + "- " + book_titles[i])
        return book_titles
    else: # if the category is not found in the dictionary, return empty list
        print("The category " + category + " has the following books:")
        return book_titles

# Function 11 (Developed by Toniloba Kumapayi (101236693))
def get_book_by_category_and_rate(category: str,rate: int ,dictionary: dict)-> list:
    """
    Returns a list of book titles for the given category and rate interval
    
    Written by: Toniloba Kumapayi (101236693)
    
    >>>get_book_by_category_and_rate("Adventure",4, load_dataset('Google_Books_Dataset.csv')) 
    Sword of Destiny: Witcher 2: Tales of the Witcher
    A Feast for Crows (A Song of Ice and Fire, Book 4)
    After Anna
    The Way Of Shadows: Book 1 of the Night Angel
    A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
    Edgedancer: From the Stormlight Archive
    The Malady and Other Stories: An Andrzej Sapkowski Sampler

    >>>get_book_by_category_and_rate("Bussiness",100, load_dataset('Google_Books_Dataset.csv'))
    []

    >>>get_book_by_category_and_rate("Stationary",4, load_dataset('Google_Books_Dataset.csv'))
    []

    """
    lst=[]
    if category in dictionary: #indentifies the category in the dictionary
        booklist  = dictionary.get(category,[])
        # if there is no category returns empty list, to avoid error
        for book in booklist: 
            current_rate=book.get('rating') # gets the rating value from dictionary
            if current_rate !='' and (rate <= current_rate < (rate+1)):
                # satifies the criteria for rate
                lst.append(book.get('title'))
                # adds the book_title to the list
    print("The category" +  ' ' + category + ' '+ 'and' + ' rating ' +str(rate) + ' '+ "has the following books :")
    for i in lst:
        print(i)
    return lst # returns the list of books that meet the criteria for category and rate

# Function 12 (Developed by Karran Dhillon (101229275))
def get_author_categories(author: str, book_dict: dict) -> list[str]:
    """
    Returns a list of the categories the inputted "author" has written a book in
    the dictionary argument.
    
    Written by: Karran Dhillon 101229275
    
    Preconditions: author must be a string argument (case sensitive)
    book_dict must be a dictionary with categories as the keys
    
    >>> from T003_P1_load_data import load_dataset
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> book_dict = load_dataset(file_name)
    
    >>> get_author_categories("Blake Pierce", book_dict) # Several Books
    The author "Blake Pierce" has published books under the following categories:
    
            1- Thrillers
            2- Detective
            3- Mystery
            4- Fiction
    ['Thrillers', 'Detective', 'Mystery', 'Fiction']
    
    >>> get_author_categories("James Bond", book_dict) # No such author
    The author "James Bond" has published books under the following categories:
    
            No books were found
    []
            
    >>> get_author_categories("Zig Ziglar", book_dict) # Only 1 book
    The author "Zig Ziglar" has published books under the following categories:
    
            1- Business
    ['Business']
    """
    author_categories = set() # Contains all categories with author (no duplicates)
    
    for category, books in book_dict.items(): # For each category in the dictionary
        for book in books: # For each book within the category of books
            if book.get("author") == author: # Author present
                author_categories.add(category) # append to set, without duplicates
            
    print('The author "', author, '" has published books under the following categories:\n', sep='')
    if len(author_categories): # Has at least 1 book
        i = 1 # Corresponding number of books and category
        for category in author_categories: 
            print("\t", i, "- ", category, sep='')
            i += 1
    else: # No books found
        print("\tNo books were found")
        
    return list(author_categories) # Cast the set to a list
