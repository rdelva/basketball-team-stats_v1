import copy
import constants


# importing the teams dictionary and players dictionary 

def clean_data():
    
   

    players = copy.deepcopy(constants.PLAYERS)
    
    # Clean Players Data
    for player in players:
        player['name']
        guardian_split = player['guardians'].split("and")
        player['guardians'] = guardian_split

        if(player['experience'] == 'YES'):
            player['experience'] = True
        else: 
            player['experience'] = False

        player['height'] = int(player['height'].split(" ")[0])

    return players

def balance_team(player_list):
    print(player_list)

    # determinues how many people in a team
    teams = copy.deepcopy(constants.TEAMS)
    num_players_team = len(player_list) / len(teams)

    #Turn the teams list into the list of dictionaries
    team_list = {team:[] for team in teams}
    print(team_list)


    # #Put the player list into three teams
    # for index, player in enumerate(player_list):
    #     if index > 0 and index <= num_players_team - 1:



    





    




def main():
     player_list = clean_data()
     balance_team(player_list)

if __name__ == '__main__':
    main()