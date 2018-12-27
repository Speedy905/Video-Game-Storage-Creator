#Antonio Karlo Mijares
#November 14/15 2016
#dictionaries_functions_variables.py
#CA

#Creates base dictionaries/function/variable for 
#the inventory creation

#6/6

#Progress bar modules
import progressbar
import time

name = []
#Sets the default filename
filename = ('games')

#---------------------------------------------------------
#Platforms
nocategories = ['Combined Platforms','PC','Not listed',
                'Mobile']

nintendo = ['Nintendo Wii','Nintendo Wii U']

microsoft = ['Xbox 360','Xbox One']

sony = ['Playstation 3','Playstation 4']

#Appends them into a 2D Array
allplatforms = [nocategories,nintendo,microsoft,sony]

#---------------------------------------------------------

#---------------------------------------------------------
#Genres aka rabbit hole
maingenres = ['Action','Action-adventure','Adventure',
              'Role-Playing','Simulation','Strategy',
              'Sports','Other notable genres',
              'Video game genres by purpose','Unknown']


action_sub = ['Platform','Shooter',
              "Fighting games and beat'em ups",
              'Stealth']

action_adventure_sub = ['Survival Horror','Metroidvania']

adventure_sub = ['Text adventures','Graphic adventures']

rpg_sub = ['Action RPG','MMORPG','Roguelikes','Tactical RPG',
           'Sandbox RPG','Cultural differences','Choices',
           'Fantasy']

simulation_sub = ['Construction and management simulation',
                  'Life simulation','Vehicle simulation']

strategy_sub = ['4X game','Artillery game','Real-time strategy',
                'Real-time tactics',
                'Multiplayer online battle arena',
                'Tower defense','Turn-based strategy',
                'Turn-based tactics','Wargame',
                'Grand strategy wargame']

sports_sub = ['Racing','Sports game','Competitive',
              'Sports-based fighting']

notable_sub = ['MMO','Casual game','Music game','Party game',
               'Programming game','Logic game','Trivia game',
               'Board game/Card game']

purpose_sub = ['Advergame','Art game','Casual game','Christian game',
               'Educational game','Electronic game','Exergame',
               'Serious game']

#Appends them into a 2D Array
genrelist = [action_sub,action_adventure_sub,adventure_sub,
             rpg_sub,simulation_sub,strategy_sub,sports_sub,
             notable_sub,purpose_sub]
#---------------------------------------------------------

#Linear search
def linearSearch(item,list):
    found = False
    current_pos = 0
    while current_pos < len(list) and not found:
        #States if the item has been found
        if list[current_pos] == item:
            #Sets the variable to true
            found = True
        current_pos = current_pos + 1
    return found

#Progress bar 1
#def progress1():
    #Sets the max value
 #   with progressbar.ProgressBar(max_value=10) as bar:
  #      for i in range(10):
   #         time.sleep(0.1)
            #Updates the screen
    #        bar.update(i)

#Progress bar 2
#def progress2():
 #   bar = progressbar.ProgressBar()
  #  for i in bar(range(100)):
   #     time.sleep(0.02)
