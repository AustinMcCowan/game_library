#!/usr/bin/python3
# Austin McCowan
# 1/27/2020

''' Game Library program. Borrow content from big_brother.py. Will later turn into GUI, for now it is console based. '''

'''
class Library(object):
    def __init__(self):
        try:
            
            PLACEHOLDER = open("PLACEHOLDER.pickle", "rb")
            self.games = pickle.load(PLACEHOLDER)
            PLACEHOLDER.close()
            
        except:
            
            raise Exception("Data failed to load")
            
        
    # updates the information in PLACEHOLDER.pickle with the current information in the program (games)
    def update(self):
        try:
            
            PLACEHOLDER = open("PLACEHOLDER.pickle", "wb")
            pickle.dump(self.games, PLACEHOLDER)
            PLACEHOLDER.close()
            
        except:
            
            raise Exception("Data failed to update")     
'''

def add_or_edit_game():
    print("adding or editing game...")

def print_info():
    print("printing info...")
    
def search_by_title():
    print("searching by title...")
    
def remove_game():
    print("removing a game...")

def save_database():
    print("saving database...")
    
def quit_app():
    print("quitting")
    
# content = Library()   

quit = False

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
        for i in range(3):
            print_info()
            
    elif user_command == "3":       
        search_by_title()
    
    elif user_command == "4":
        remove_game()
        
    elif user_command == "5":
        save_database()
        
    elif user_command == "q":
        quit_app()
        quit = True
        