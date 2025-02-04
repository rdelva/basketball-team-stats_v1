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
    print("\nBALANCE TEAMS")  

    # Finds out how many players should be on each team
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    
    #amount of players
    players_list = len(constants.PLAYERS)
    
    #list of teams
    teams = copy.deepcopy(constants.TEAMS)

    #turn the Teams list into a list of dictionaries
    #[{key:value] for temp_vars(s) in iterable}
    # team_list = {team:"" for team in teams}
    team_list = [{team:[]} for team in teams]
    player_list = []

    print(team_list)

    # team_list[index]['Panthers'] = []
    # print(team_list[index]['Panthers'])
     
    for index, player in enumerate(team_players):
        if index >=0 and index <= 5:
            team_list[0]['Panthers'].append(player)
        elif index >= 6 and index <= 11:
            team_list[1]['Bandits'].append(player)
        else:
            team_list[2]['Warriors'].append(player)
    
   

    print(team_list[2]['Warriors'])
    #Assign each player to a team






   






if __name__ == "__main__":
        intro()
        clean_data()
      






        