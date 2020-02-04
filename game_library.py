#!/usr/bin/python3
# Austin McCowan
# 1/27/2020

''' Game Library program. Borrow content from big_brother.py. Will later turn into GUI, for now it is console based. '''

import pickle
import data_reboot as dr

global category_list
category_list = ["genre","title", "developer", "publisher", "system", "release date", "rating", "single/multi/either", "price", "beat it", "purchase date"]
global alt_category_list
alt_category_list = category_list
alt_category_list.append('notes')

class Library(object):
    def __init__(self):
        
        # Try and open the pickle file and grab contents
        try: 
            datafile = open("game_lib.pickle", "rb")
            self.games = pickle.load(datafile)
            
        # If unable to grab content, run the function inside of data_reboot.py. Then try loading content again.    
        except:            
            dr.fix_it()
            print("Data failed to load; Grabbing original content")
            datafile = open("game_lib.pickle", "rb")
            self.games = pickle.load(datafile)
        
        # Close datafile    
        datafile.close()
            
    # updates the information in game_lib.pickle with the current information in the program (games)
    def save(self):
        try:
            datafile = open("game_lib.pickle", "wb")
            pickle.dump(self.games, datafile)
            datafile.close()
            
        except:
            
            raise Exception("Data failed to save")     



def add_game():
    # This sets the value for the new key, it compensates for deleting a game (as each entry in games has a unique key)
    for i in range(len(content.games)):
        if (i+1) not in content.games.keys():
            new_key = i+1
            break
        else:
            new_key = len(content.games)+1
            
    new_entry = []
    valid = False
    while not valid:
        # Input content
        for i in range(12):
            category_input = input("Please give the "+alt_category_list[i]+": ")
            new_entry.append(category_input)
        print("\nYour results: \n", new_entry)
        
        # Asks user if the data inputted is correct
        acceptable_answer = False
        while acceptable_answer != True:
            repeat_choice = input("Is this correct? ")
            if repeat_choice.lower() in "yes":
                valid = True
                acceptable_answer = True
            elif repeat_choice.lower() in "no":
                new_entry = []
                acceptable_answer = True
            else:
                print("Please give a yes or no")
                continue
            
    content.games[new_key] = new_entry    

def edit_game():
    print("\nHere is the library: ")
    for key in content.games.keys():
        print(key, "-", content.games[key][1])
        print("")
        
    alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')    
    edit_key = int(input("which game do you want to change?: "))
    
    for i in range(12):
        print("\nCurrent "+alt_category_list[i]+": "+content.games[edit_key][i])
        edit_input = input("Please give a new "+alt_category_list[i]+": ")
        empty_check = True
        for i in range(len(alphabet)):
            if alphabet[i] in edit_input:
                empty_check = False
            
        if empty_check == True:
            pass
        else:
            content.games[edit_key][edit_input]

def print_info(game):
    print("----------------------------")
    print("Genre:", content.games[game][0])
    print("Title:", content.games[game][1])
    print("Developer:", content.games[game][2])
    print("Publisher:", content.games[game][3])
    print("System:", content.games[game][4])
    print("Release Date:", content.games[game][5])
    print("Rating:", content.games[game][6])
    print("Single/Multi/Either:", content.games[game][7])
    print("Price:", content.games[game][8])
    print("Beat it?:", content.games[game][9])
    print("Purchase Date:", content.games[game][10])
    print("Notes:", content.games[game][11])
    print("----------------------------")
 
def search_by(category, term):
    category_value = None
    if category.lower() == "genre":
        category_value = 0
    elif category.lower() == "title":
        category_value = 1
    elif category.lower() == "developer":
        category_value = 2
    elif category.lower() == "publisher":
        category_value = 3
    elif category.lower() == "system":
        category_value = 4
    elif category.lower() == "release date":
        category_value = 5
    elif category.lower() == "rating":
        category_value = 6
    elif category.lower() == "single/multi/either":
        category_value = 7
    elif category.lower() == "price":
        category_value = 8
    elif category.lower() == "beat it":
        category_value = 9
    elif category.lower() == "purchase date":
        category_value = 10
    

    search_success = False
    for game in content.games:
        if term.lower() in content.games[game][category_value].lower():
            print_info(game)
            search_success = True
    if search_success == False:
        print("\nNothing found...\n")

# Remove a game        
def remove_game():
    print("---------------\n")
    for key in content.games.keys():
        print(key, "-", content.games[key][1])
        print("")
    
    valid = False
    while not valid:
        try:
            game_to_remove = int(input("What game would you like to remove? "))
                
        # Something other than a number was entered    
        except:
            retry_check = input("\nSomething other than a number was inputted, do you want to retry? ")
            if retry_check.lower() in "yes":
                continue
            else:
                valid = True
                continue
            
        # An invalid number has been entered
        if game_to_remove not in content.games.keys():
            retry_check = input("\nThere is no game at this number, do you want to retry? ")
            if retry_check.lower() in "yes":
                continue
            else:
                valid = True
                continue
         
        # Confirm the user wants to remove the game   
        else:
            confirm_validation = input("\nAre you sure you want to remove this game?: ")
            if confirm_validation.lower() in "yes":
                print("removing game\n")
                temp_dictionary = content.games
                try:
                    # Dominic's Code that will compensate for holes being created. WILL BUG IF HOLES ALREADY EXIST
                    for key in range(1, len(content.games)+1):
                        if key >= game_to_remove and key != len(content.games):
                            content.games[key] = content.games[key+1]
                        if key == len(content.games):
                            content.games.pop(key)
                except:
                    # If anything goes wrong, simply just remove the selected game at its location. failsafe 
                    content.games = temp_dictionary
                    content.games.pop(game_to_remove)
                    
            # Asks the user if they want to remove another game
            retry_check = input("Would you like to remove another game? ")
            if retry_check.lower() in "yes":
                continue
            else:
                valid = True
                continue
        
            

def save_database():
    print("\nSaving Changes...\n")
    content.save()
    
def quit_app():
    print("\nPreparing to Quit...\n")
    validation = input("Would you like to save changes? ")
    valid_end = False
    while valid_end != True:
        if validation.lower() in "yes":
            save_database()
            valid_end = True
        elif validation.lower() in "no":
            valid_end = True
        else:
            print("Please give a yes or no")
            continue
        
    

# Initial stuff that needs to be added before main program    
content = Library()   
quit = False

# Main
while quit != True: 
    print("")
    print('''Choosable actions:
             1) Add/Edit Game
             2) Print All Games
             3) Search By Category
             4) Remove a Game
             5) Save Database
             Q) Quit\n''')
    
    user_command = input("Please choose an option: ")
    
    # Add or edit
    if user_command == "1":
        stop_loop = False
    
        while stop_loop != True:
            option = input("\nDo you want to add or edit a game?: ")
            acceptable_answer = False
            if option.lower() not in ["add", "a", "edit", "e", "no", "n"]:  
                while acceptable_answer != True:
                    print("--inputted invalid option--")
                    repeat_choice = input("Try again? ")
                    if repeat_choice.lower() in "yes":
                        acceptable_answer = True                   
                    elif repeat_choice.lower() in "no":
                        stop_loop = True
                        acceptable_answer = True
                    else:
                        print("Please give a yes or no")
                        continue
                    
            elif option.lower() in "no":
                stop_loop = True
                
            elif option.lower() in ["add", "a"]:
                add_game()
                
            elif option.lower() in ["edit", "e"]:
                edit_game()
                
    # Print all    
    elif user_command == "2":
        for game in content.games:
            print_info(game)
    
    # Search by        
    elif user_command == "3":
        stop_search = False
        while stop_search != True:
            acceptable_answer = False   
            print("Capable choices: ", category_list)
            search_category = input("Please input a category to search: ")
            
            if search_category.lower() not in category_list:
                print("\n--Category given is either mispelled or does not exist--\n")
                
                # Check for retry
                while acceptable_answer != True:
                    repeat_choice = input("Try again? ")
                    if repeat_choice.lower() in "yes":
                        acceptable_answer = True
                        
                    elif repeat_choice.lower() in "no":
                        stop_search = True
                        acceptable_answer = True
                        
                    else:
                        print("Please give a yes or no")
                        continue
            else:
                search_term = input("Please input a search term for " + search_category + ": ")
                search_by(search_category, search_term)
             
            # Check if user wants to reattempt  
            while acceptable_answer != True:
                repeat_choice = input("Search again? ")
                if repeat_choice.lower() in "yes":
                    acceptable_answer = True                   
                elif repeat_choice.lower() in "no":
                    stop_search = True
                    acceptable_answer = True
                else:
                    print("Please give a yes or no")
                    continue
     
    # Remove
    elif user_command == "4":
        remove_game()
    
    # Save    
    elif user_command == "5":
        save_database()
    
    # Quit    
    elif user_command.lower() == "q":
        quit_app()
        quit = True