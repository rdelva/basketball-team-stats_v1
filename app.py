import copy
import constants #contains 2 constant lists called TEAMS and PLAYERS



def intro():
    print("Here are your choices: \n A) Display Team Stats \n B) Quit")
    print("\n")
    choice = input("Enter an option: ")
    
    if choice.lower() == 'a':
        display_team_stats()        
    elif choice.lower() == 'bcl':
         print("Ending Program ... Goodbye")
    else:
        print("Ending Program ... Goodbye")
         
          

      

def  display_team_stats():
    print("Team Stats")
    #print(constants.PLAYERS)

      

def clean_data():
    print('CLEAN DATA:')        
    players_copy = copy.deepcopy(constants.PLAYERS)
    teams_copy = copy.deepcopy(constants.TEAMS)
    players_new =  {} #created players_new to store cleaned data

    for player in players_copy:
        # player['name'] = player.name
        # player['guardians'] = player.guardians
        if(player['experience'] == 'YES'):
            player['experience'] = True
        else:
            player['experience'] = False
       
        player['height'] = int(player['height'].split(" ")[0])
        # = int(player['height']) + "inches"

    print(player)





if __name__ == "__main__":
        intro()
        clean_data()






        