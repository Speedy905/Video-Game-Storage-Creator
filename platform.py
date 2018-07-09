#Antonio Karlo Mijares
#November 14/15 2016
#platform.py
#CA

#4/6

#---------------------------------------------------------
#Platforms file
#---------------------------------------------------------
#Imports the required modules
from genre import gameGenre
from dictionaries_functions_variables import *
#---------------------------------------------------------

#Platforms class
class Platform(object):
    #Init function (Base function)
    def __init__(self):
        #Choices
        self.choices = {
                        '1':self.mic,
                        '2':self.nin,
                        '3':self.son,
                        '4':self.nocat,
                        '5':self.displayplat
                        }
    
    #Displays the menu
    def displayplatmenu(self):
        print('''
What sub brand are you on?
Press
1. Microsoft
2. Nintendo
3. Sony
4. No subbrand

5. Display the platforms
        ''')
    
    #Runs the platforms menu
    def runmenu(self):
        self.platforms = True
        while self.platforms:
            #Displays the menu
            self.displayplatmenu()
            #Instructs the user to input their responce
            choice = input('Enter your choice: ')
            procedure = self.choices.get(choice)
            #States if the input matches to self.choices,
            #then it runs the specified function
            #Else it displays an error
            if procedure:
                procedure()
            else:
                print('Invalid input')
    
    #Microsoft
    def mic(self):
        mic = True
        while mic:
            #Asks the user what platform is it in
            print('''
What platform does it belong to?
Please type it. Case sensitive
Or type "-Go back-"  
without quotations to go back to the previous menu
            ''')
            #Displays the list
            for mics in microsoft:
                print(mics)
            print('')
            consplat = input('Responce: ')
            #Calls the linear search function from the variables
            foundmic = linearSearch(consplat, microsoft)
            #If the item has been found, it writes to the file
            if foundmic:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Platform: ')
                    g.write(str(consplat))
                    g.write('\n')
                mic = False
                self.platforms = False
                #Calls the class function
                #Running the next step
                gameGenre().rungenre()
            else:
                #States if the typed word was below
                if consplat == '-Go back-':
                    #Goes back to the previous menu
                    mic = False
                else:
                    #Error 
                    print('Not found.')
    
    #nintendo
    def nin(self):
        nin = True
        while nin:
            #Asks the user what platform is it in
            print('''
What platform does it belong to?
Please type it. Case sensitive
Or type "-Go back-"  
without quotations to go back to the previous menu
            ''')
            #Displays the list
            for nins in nintendo:
                print(nins)
            print('')
            consplat = input('Responce: ')
            #Calls the linear search from the variables
            foundnin = linearSearch(consplat, nintendo)
            #If the item has been found, it writes to the file
            if foundnin:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Platform: ')
                    g.write(str(consplat))
                    g.write('\n')
                nin = False
                self.platforms = False
                #Calls the class function
                #Doing the next step
                gameGenre().rungenre()
            else:
                #States if the typed word was below
                if consplat == '-Go back-':
                    #Goes back to the menu
                    nin = False
                else:
                    print('Not found.')
    
    #Sony
    def son(self):
        son = True
        while son:
            #Asks the user what platform is it in
            print('''
What platform does it belong to?
Please type it. Case sensitive
Or type "-Go back-"  
without quotations to go back to the previous menu
            ''')
            #Displays the list
            for son in sony:
                print(son)
            print('')
            consplat = input('Responce: ')
            #Calls the linear search for the variables
            foundson = linearSearch(consplat, sony)
            #If the item has been found, it writes to the file
            if foundson:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Platform: ')
                    g.write(str(consplat))
                    g.write('\n')
                son = False
                self.platforms = False
                #Calls the class function
                #Doing the next step 
                gameGenre().rungenre()
            else:
                #States if the typed word was below
                if consplat == '-Go back-':
                    #Goes back to the menu
                    son = False
                else:
                    print('Not found.')
    
    #No sub brand
    def nocat(self):
        uncat = True
        while uncat:
            #Asks the user what platform is it in
            print('''
What platform does it belong to?
Please type it. Case sensitive
Or type "-Go back-"  
without quotations to go back to the previous menu
            ''')
            #Displays the list
            for un in nocategories:
                print(un)
            print('')
            consplat = input('Responce: ')
            #Calls the linear search for the variables
            foundson = linearSearch(consplat, nocategories)
            #If the item has been found, it writes to the file
            if foundson:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Platform: ')
                    g.write(str(consplat))
                    g.write('\n')
                #Writes into the file
                uncat = False
                self.platforms = False
                #Calls the class function, proceeding
                #to the next step
                gameGenre().rungenre()
            else:
                #States if the typed word was below
                if consplat == '-Go back-':
                    #Goes back to the menu
                    uncat = False
                else:
                    print('Not found.')
    
    #Displays the platforms
    def displayplat(self):
        #Displays the list
        for p in allplatforms:
            print(p)
        goback = input('Press Enter to go back.')