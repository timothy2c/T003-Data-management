# Milestone 3 Task 2
# December 9, 2021
# Version 1.0

# T003:
# Robert Forward (101224089)
# Karran Dhillon (101229275)
# Toniloba Kumapayi (101236693)
# Robert Forward (101224089)
# Timothy Chang (101222138)

# --Imports--
import csv

# --Function Definitions--
def load_dataset(file_name: str) -> dict:
    """
    Returns a dictionary about books stored in a list of dictionaries based on the "filename" string argument. 
    The keys for the dictionary are the genres of the books, as strings.
    
    Original Author: Robert Forward 101224089
    
    >>> file_name = 'Google_Books_Dataset.csv'
    >>> books = load_dataset(file_name)
    >>> print(books)
    { "Fiction":[ {"title": "Antiques Roadkill: A Trash 'n' Treasures Mystery",  
           "authors": " Barbara Allan",
           "language ": "English",  
           "rating": 3.3,  
           "publisher": " Kensington Publishing Corp.",  
           "pageCount": 288
           },
           {another element},
           ...
         ],
    "Biography":[ {"title": "The Nightshift Before Christmas: Festive hospital  
                            diaries from the author of million-copy hit",  
            "authors": " Adam Kay",
            "language": "English",  
            "rating": 4.7,  
            "publisher": "Pan Macmillan",
            "pageCount": 112
            },
            {another element},
            ...
            ],
            ...
    }
    """
    file = open(file_name, "r")
    reader = csv.reader(file)
    header = next(reader) #These will be the key parameters for the dictionary
    
    genres_set = set() #Creates an empty set to store the genres
    info_list = [] # Creates an empty list to store the nested dictionaries
    book_dict = {} # Lists of Nested Dictionaries will be stored here
    
    for row in reader: # For each row in the csv file, a new dictionary is added
        genres_set.add(row[6]) # Adds the genre to the set; there are no duplicates
        if len(row[3]): # if non-empty, convert to float
            row[3] = float(row[3])
            
        info_list.append({header[1]:row[1], # title
                          header[2]:row[2], # author
                          header[7]:row[7], # language
                          header[3]:row[3], # rating
                          header[4]:row[4], # publisher
                          header[6]:row[6], # genre
                          header[5]:int(row[5])}) # page_count
        
            
    for i in genres_set: # For each genre in the genre set, a new list will be created
        temp_list = [] # Temporary list to hold each genre's list
        
        for j in info_list: #For each dictionary nested in the list
            if j.get(header[6]) == i: #If the genre in the list is the same as the genre in the set, the genre is deleted from the list
                    del j[header[6]]  # remove genre 
                    if j not in temp_list: # filters through duplicates
                        temp_list.append(j) #The dictionary is then appended to the list
        
        book_dict[i] = temp_list #The list becomes the value for specififed key
    file.close()

    return book_dict
