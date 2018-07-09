#Antonio Karlo Mijares
#November 14/15 2016
#genre.py
#CA

#5/6

#Genre file

#Imports the required files
from dictionaries_functions_variables import *
#---------------------------------------------------------

#Game Genre class
class gameGenre(object):
    #Init function (Base Class Function)
    def __init__(self):
        #Once a choice has been selected,
        #It runs a function that is connected
        #To it
        self.choices = {
                        'Action':self.action,
                        'Action-adventure':self.action_adventure,
                        'Adventure':self.adventure,
                        'Role-Playing':self.role_playing,
                        'Simulation':self.simulation,
                        'Strategy':self.strategy,
                        'Sports':self.sports,
                        'Other notable genres':self.others,
                        'Video game genres by purpose':self.purpose,
                        'Unknown':self.unknown,
                        'Display list':self.displaylist
                        }
    
    #Displays the genre menu
    def displaygenreMenu(self):
        #Calls the progress bar function/module
        progress2()
        print('''
What category genre is your game in?
Please type it. Case sensitive

Or type "Display list" (without quotations) 
to view the entire genre options
[Warning, Huge list.]
        ''')
        
        #Displays the list        
        for genrelist in maingenres:
            print(genrelist)
    
    #Runs the genre class
    def rungenre(self):
        self.genre = True
        while self.genre:
            #Displays the menu
            self.displaygenreMenu()
            print('')
            #Lets the user respond
            self.choice = input('Responce: ')
            go_to = self.choices.get(self.choice)
            if go_to:
                go_to()
            else:
                print('Invalid input')
    
    #Action function
    def action(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in action_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, action_sub)
            
            #If the sub genre has been found
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Action_Adventure Function
    def action_adventure(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in action_adventure_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, action_adventure_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Adventure Function
    def adventure(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--" without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in adventure_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, adventure_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Role Playing Function
    def role_playing(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in rpg_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, rpg_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Simulation function
    def simulation(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in simulation_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, simulation_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Strategy function
    def strategy(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in strategy_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, strategy_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Sportball function
    def sports(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in sports_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, sports_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Other genres function
    def others(self):
        progress1()
        sub = True
        
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in notable_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, notable_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Purpose function
    def purpose(self):
        progress1()
        sub = True
        while sub:
            print('''
What sub genre is your game in?
Please type it out. Case sensitive
Or type "--Go back--"  without quotations
to go back to the previous menu
''')
            
            #Display the list
            for options in purpose_sub:
                print(options)
            
            #Asks the user for its input
            subgen = input('Responce: ')
            #Calls the linear search for the variables
            foundsub = linearSearch(subgen, purpose_sub)
            
            #If the sub genre has been found,
            #It writes to the file
            if foundsub:
                with open(str(filename)+'.txt','a') as g:
                    g.write('Main genre: ')
                    g.write(str(self.choice))
                    g.write('\n')
                    g.write('Sub genre: ')
                    g.write(str(subgen))
                    g.write('\n')
                    #Creates a line for the new game
                    g.write('-----------------------------')
                    g.write('\n')
                #Writes into the file
                
                sub = False
                self.genre = False
            else:
                #States if user typed Go back
                #Then it goes back
                if subgen == '--Go back--':
                    sub = False
                else:
                    print('Not found. Please try again')
    
    #Unknown function (No genre)
    def unknown(self):
        #Writes into the file
        with open(str(filename)+'.txt','a') as g:
            g.write('Main genre: ')
            g.write(str(self.choice))
            g.write('\n')
            #Creates a line for the new game
            g.write('-----------------------------')
            g.write('\n')
        self.genre = False
    
    #Displays the entire rabbit hole list
    def displaylist(self):
        progress2()
        for l in genrelist:
            print(l)      
        goback = input('Press Enter to go back')