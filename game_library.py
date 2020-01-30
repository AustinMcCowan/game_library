#!/usr/bin/python3
# Austin McCowan
# 1/27/2020

''' Game Library program. Borrow content from big_brother.py. Will later turn into GUI, for now it is console based. '''

import pickle
import data_reboot as dr

global category_list
category_list = ["genre","title", "developer", "publisher", "system", "release date", "rating", "single/multi/either", "price", "beat it", "purchase date"]

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



def add_or_edit_game(option):
    if option in ["add", "a"]:
        # This sets the value for the new key, it compensates for deleting a game (as each entry in games has a unique key)
        for i in range(len(content.games)):
            if (i+1) not in content.games.keys():
                new_key = i+1
                break
            else:
                new_key = len(content.games)+1
                
        new_entry = []
        valid = False
        alt_category_list = category_list
        alt_category_list.append('notes')
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
        
    elif option in ["edit", "e"]:
        print("\nEditing...\n")

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

        
def remove_game():
    print("\nRemoving a game...\n")

def save_database():
    print("\nSaving Changes...\n")
    content.save()
    
def quit_app():
    print("\nQuitting...\n")
    

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
            option = input("Do you want to add or edit a game?: ")
            acceptable_answer = False
            if option not in ["add", "a", "edit", "e", "no", "n"]:  
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
                    
            elif option in "no":
                stop_loop = True
                
            else:        
                add_or_edit_game(option)
    
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