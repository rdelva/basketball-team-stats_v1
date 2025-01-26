import copy
import constants #contains 2 constant lists called TEAMS and PLAYERS



def intro():
    print("BASKETBALL TEAM STATS TOOL\n")
    print ("---- MENU ----\n")
    print("Here are your choices: \n A) Display Team Stats \n B) Quit")
    print("\n")
    choice = input("Enter an option > ")
    
    if choice.lower() == 'a':
        display_team_stats()        
    elif choice.lower() == 'b':
         print("Ending Program ... Goodbye")
         exit()
    else:
        print("Ending Program ... Goodbye")
        exit()
         
          

      

def  display_team_stats():
    print("Team Stats")
    #print(constants.PLAYERS)

      

def clean_data():
    print('CLEAN DATA:')        
    players_copy = copy.deepcopy(constants.PLAYERS)
    teams_copy = copy.deepcopy(constants.TEAMS)
    players_new =  {} #created players_new to store cleaned data
    cleaned = []
 

    
    for player in players_copy:
       
        player['name'] 

        guardian_split = player['guardians'].split("and")
        guardian_list = []

        player['guardians'] = guardian_split
        
        if(player['experience'] == 'YES'):
            player['experience'] = True
        else:
            player['experience'] = False
       
        player['height'] = int(player['height'].split(" ")[0])
        # = int(player['height']) + "inches"
        cleaned.append(player)

    #print(cleaned)
    balance_teams(cleaned)
    


def balance_teams(team_players):
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    players_list = len(constants.PLAYERS)
    
    team = copy.deepcopy(constants.TEAMS)
    print("\nBALANCE TEAMS")  
    print(f"\n There are {num_players_team} players for each team")

    for player in team_players:
        print(player)

    # for index, player in enumerate(team_players):
    #     if index <= 0 and index >= 5:
    #         team['Panthers'].append(player)
    #     elif index <= 6 and index >= 12:
    #         team['Bandits'].append(player)
    #     else:
    #         team['Warriors'].append(player)      

    print(team)
            






if __name__ == "__main__":
        intro()
        clean_data()
      






        