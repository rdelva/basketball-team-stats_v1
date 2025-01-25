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

        player['guardians'] = guardian_list.append(guardian_split)
        
        if(player['experience'] == 'YES'):
            player['experience'] = True
        else:
            player['experience'] = False
       
        player['height'] = int(player['height'].split(" ")[0])
        # = int(player['height']) + "inches"
        cleaned.append(player)

    #print(cleaned)
    


def balance_teams():
    print("\nBALANCE TEAMS")
    num_players_team = len(constants.PLAYERS) / len(constants.TEAMS)
    print(f"\n There are {num_players_team} players for each team")






if __name__ == "__main__":
        intro()
        clean_data()
        balance_teams()






        