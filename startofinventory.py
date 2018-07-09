#Antonio Karlo Mijares
#November 14/15 2016
#startofinventory.py
#CA

#The file where the magic happens

#2/6

#Imports time, then the required files
import time
from name import *
from dictionaries_functions_variables import *
#Inventory Creation/Item Class
class inventoryCreation(object):
    #Init function (base function)
    def __init__(self):
        #Menu choices
        self.choices = {
                        '1':self.runSteps,
                        '2':self.goback_menu,
                        '3':self.viewname,
                        '4':self.viewgames,
                        '5':self.clearfile
                        }
    #Creates the new file
    def createFile(self):
        with open(str(filename)+'.txt','a') as g:
            pass
           
    #Displays the menu
    def displayInProgramMenu(self):
        print('''
Press 
1. Add in a new game
2. Go back to the menu
3. Look at the names of your current games
4. View your text file 
5. Clear your text file
''')
    
    #Runs the inventory creation steps
    def runSteps(self):
        #Calls the class function
        inventoryCreation().createFile()
        newGame()
    
    #Goes back to the menu
    def goback_menu(self):
        self.progmenu = False
    
    #Inventory 'Menu'
    def runprogram(self):
        self.progmenu = True
        while self.progmenu:
            #Displays the menu
            self.displayInProgramMenu()
            #Instructs the user to enter a responce
            choice = input('Responce: ')
            action = self.choices.get(choice)
            #States if the input matches to self.choices,
            #then it runs the specified function
            #Else it displays an error
            if action:
                action()
            else:
                print('Invalid input')
                
    #Displays the current games (names only)
    def viewname(self): 
        #Takes the length of the name list
        self.number = len(name)
        #----------------------------------------------       
        #States if the length is less than 0,
        #Displays a message, saying that the list
        #is empty
        #otherwise, it displays the games and how many
        #in the list
        #----------------------------------------------
        if self.number <= 0:
            print('You have no games.')
        else:
            for games in name:
                print(games)
            print('You currently have ' +str(self.number)+' game/s')
    
    #Displays the text file
    def viewgames(self):
        #Takes the length of the name list
        self.number = len(name)   
        #----------------------------------------------       
        #States if the length is less than 0,
        #Displays a message, saying that the list
        #is empty
        #otherwise, it displays the games and how many
        #in the list
        #----------------------------------------------
        if self.number <= 0:
            print('There is nothing in your text file/no games')
        else:
            print('Your games:')
            print('')
            with open(str(filename)+'.txt','r') as g:
                for line in g:
                    print(line,end='')
    
    #Clears the file
    def clearfile(self):
        clearmenu = True
        while clearmenu:
            #Displays a warning message
            print('''
WARNING!!!!!
THIS WILL TOTALLY ERASE EVERYTHING THAT IS IN YOUR FILE!
ARE YOU SURE YOU WANT TO PROCEED? (y/n)
            ''')
            #Lets the user input the responce
            responce = input('Responce: ')
            #States if user types y
            if responce == 'y' or responce == 'Y':
                #Clears the file
                with open(str(filename)+'.txt','w') as g:
                    #Calls the progressbar function/module
                    progress2()
                    print('File cleared')
                    #Clears the name list
                    name.clear()
                    return name
                clearmenu = False
            #States if user types n
            elif responce == 'n' or responce == 'N':
                clearmenu = False
            #Else statement/Error
            else:
                print('Invalid input')