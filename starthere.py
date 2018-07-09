#Antonio Karlo Mijares
#November 14/15 2016
#starthere.py
#CA

#STARTING FILE

#1/6

#Imports sys, then the required files
import sys,time
from startofinventory import inventoryCreation
from dictionaries_functions_variables import *
#---------------------------------------------------------
#Menu class
class Menu (object): 
    #__Init__ function (base function)
    def __init__(self):
        #Once a choice has been selected,
        #It runs a function that is connected
        #To it
        self.choices = {
                        'S': self.start,
                        's': self.start,
                        'H': self.showhelp, 
                        'h': self.showhelp, 
                        'Q': self.quitcreation,
                        'q': self.quitcreation,
                        'C': self.credits,
                        'c': self.credits
                        }
     
    #Displays the menu
    def display_menu(self):
        print('''
Welcome to the Video game Storage Creation!
Press:
S/s to Start the Creation
H/h to display Help/Instructions
Q/q to quit the creation
C/c to view the credits
''')
    
    #Runs the actual menu
    def runMenu(self):
        #Runs the menu loop
        while True:
            #Displays the menu
            self.display_menu()
            #Asks the user for a choice
            choice = input('Enter your choice: ')
            procedure = self.choices.get(choice)
            #States if the input matches to self.choices,
            #then it runs the specified function
            #Else it displays an error
            if procedure:
                procedure()
            else:
                print('Invalid input')
    
    #Starts the creation             
    def start(self):
        #Runs the function from the class
        progress1()
        inventoryCreation().runprogram()
    
    #Shows the help message
    def showhelp(self):
        print('''
This creates your 'shelf',
creating your video game collection
You can:
a) Read the text file
b) View how many games you have
c) Clear your text file
''')
        #Instructs the user to go back to the menu
        goback = input('Press Enter to go back to the menu')
        
    #Quits the program
    def quitcreation(self):
        #Displays a goodbye message
        print('''
Thank you for using the program.
Goodbye!
''')
        #Quits the program
        sys.exit() 

    #Displays the credits
    def credits(self):
        print('')
        print('Programmed by Antonio Karlo Mijares')
        #Pauses the program
        time.sleep(1)
        print('''
Coded in the Eclipse environment
using the Pydev plugin in the 
Python 3 language
        ''')
        time.sleep(1)
        print('''
Python Modules used:
a. time/sys
b. progressbar2
        ''')
        time.sleep(1)
        print('''
An ICS4U CA project
Learn more at 
https://sites.google.com/site/mrliconti/ics4u-python/ics4u-python-culminating-activity
        ''')
        time.sleep(1)
        
#--------------------#                     
#Runs the program    #
Menu().runMenu()     #
#--------------------#
                
