import constants
import copy

def clean_data(players):
"""
The function modifies some the data from the
constants.py file, that will later be passed to the function. 
"""
    
    clean_players = players
    
    for player in clean_players:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split(" and ")
        
        if player['experience'] == "NO":            
            player['experience'] = False
            
        elif player['experience'] == "YES":         
            player['experience'] = True
    
    return (clean_players)              


def balance_teams(teams, players):
"""
Balance the teams with an equal number of players per team and an equal number of experienced/inexperienced players. 
"""
    
    num_players = int((len(players) / len(teams)) / 2)
    count = 0
        
    experienced = []
    inexperienced = []
    
    for player in players:
        if player['experience'] == True:
            experienced.append(player)
        
        elif player['experience'] == False:
            inexperienced.append(player)
    
    balanced_teams = {}
    
    for team in teams:
        balanced_teams[team] = experienced[count:num_players+count] + inexperienced[count:num_players+count]
        count += num_players
        
    
    return (balanced_teams)


def avarage_height(team):
"""
Calculating and returning the team's avarage height. 
"""
    
    list_of_heights = []
    num_players = 0 
    
    for player in team:
        list_of_heights.append(player['height'])
        num_players += 1

    return round(sum(list_of_heights) / num_players, 1)
    

def name_players(team):
"""
Returning a string with the player names. 
"""

    list_of_names = []
    
    for player in team:
        list_of_names.append(player['name'])

    return (", ".join(list_of_names))
    

def name_guardians(team):
"""
Returning a string with the guardian names.
"""

    list_of_guardians = []
    
    for guardians in team:
        list_of_guardians += guardians['guardians']

    return (", ".join(list_of_guardians))

  
def experience(team):
"""
Calculate and return the number of experienced and inexperienced players. 
"""

    num_experienced = 0
    num_inexperienced = 0
    
    for player in team:
        if player['experience'] == True:
            num_experienced += 1
        else:
            num_inexperienced += 1
        
    return num_experienced, num_inexperienced


def select_team():
"""
Allowing the user to choose the team they would like to see the stats for.
"""
    
    while True:
        print(" Teams: \n\n 1: Panthers\n 2: Bandits\n 3: Warriors")
        
        try:
            selected_team = int(input("\n Input the integer that corresponds with the team of your choosing: "))
                                
        except ValueError:   
            print ("\n Please choose an integer within the range 1 - 3. \n")
            continue
                   
        else: 
            if selected_team < 1 or selected_team > 3:
                print ("\n Please choose an integer within the range 1 - 3. \n")
                continue
                
            else:
                return constants.TEAMS[selected_team-1]
               
    
def main_program():
"""
The main program displaying all the information about the teams. 
A small menu to tie it all together into a user experience.
"""
    
    data_copy = copy.deepcopy(constants.PLAYERS)
    clean_players = clean_data(data_copy)
    balanced_teams = balance_teams(constants.TEAMS, clean_players)
         
    print("\n      BASKETBALL TEAM STATS TOOL  \n         ------------------\n\nPlease follow the instructions below\n")
    
    while True:
        print(" 1: Display Team Stats \n 2: Quit Program\n")
        
        try: 
            choise = int(input(" Choose an option from the menu above: "))
            print("")
        
        except ValueError: 
            print("\n Please choose either 1 or 2. Integers only. \n") 
            continue
        
        else:
            if choise == 1:
                team = select_team()
                experienced, inexperienced = experience(balanced_teams[team])                            
                                                
                print ("\n Team: {}".format(team))
                print (" ---------------")
                print (" Total players: ",(len(balanced_teams[team])))
                print (" Total experienced: {}".format(experienced))
                print (" Total inexperienced: {}".format(inexperienced))
                print (" Average height: {} ".format(avarage_height(balanced_teams[team])))
                print ("\n Players:\n {}".format(name_players(balanced_teams[team])))
                print ("\n Guardians:\n {}".format(name_guardians(balanced_teams[team])))
                print (" ---------------\n")
                                                                  
            elif choise == 2:
                print(" Thank you. Enjoy your day.\n")
                exit()

            else:
                print("Please choose either 1 or 2. Integers only. \n")
                
                
if __name__ == '__main__':
      main_program()
