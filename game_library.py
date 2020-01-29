#!/usr/bin/python3
# Austin McCowan
# 1/27/2020

''' Game Library program. Borrow content from big_brother.py. Will later turn into GUI, for now it is console based. '''

import pickle
import data_reboot as dr

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


def add_or_edit_game():
    print("\nAdding or editing game...\n")

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
    
def search_by_title():
    print("\nSearching by title...\n")
    
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
    
    print('''Choosable actions:
             1) Add/Edit Game
             2) Print All Games
             3) Search By Title
             4) Remove a Game
             5) Save Database
             Q) Quit\n''')
    
    user_command = input("Please choose an option: ")
    
    if user_command == "1":
        add_or_edit_game()
    
    elif user_command == "2":
        for game in content.games:
            print_info(game)
            
    elif user_command == "3":
        search_title = input("Please input a title to search")
        search_by_title()
    
    elif user_command == "4":
        remove_game()
        
    elif user_command == "5":
        save_database()
        
    elif user_command.lower() == "q":
        quit_app()
        quit = True