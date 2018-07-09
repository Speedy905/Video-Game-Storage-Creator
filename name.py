#Antonio Karlo Mijares
#November 14/15 2016
#name.py
#CA

#3/6

#Imports the required files
from platform import Platform
from dictionaries_functions_variables import *

#A function that asks the user the name of the game
def newGame():
    #Instructs the user to input the name
    nameofgame = input('Type in the name of your game: ')
    #Appends the input in the list
    name.append(nameofgame)       
    #Sorts the list
    name.sort()
    #Opens the file
    with open(str(filename)+'.txt','a') as g:
        #Writes the info into the file
        g.write('Video Game: ')
        g.write(str(nameofgame))
        g.write('\n')

    #Calls the class function
    #Running the next step
    Platform().runmenu()
