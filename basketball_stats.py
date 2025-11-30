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
    # print(player_list)

    # determinues how many people in a team
    teams = copy.deepcopy(constants.TEAMS)
    num_players_team = len(player_list) / len(teams)

    #Turn the teams list into the list of dictionaries
    teams_list = [{team:[]} for team in teams ]
    print(type(teams))
    print(teams_list)

    #sort each player into Teams List
    

    for index, player in enumerate(player_list):
        if index <= 5: 
            teams_list[0]['Panthers'].append(player)
        elif index <=11:
             teams_list[1]['Bandits'].append(player)
        else: 
             teams_list[2]['Warriors'].append(player)

    print(teams_list)
        







    





    


def main():
     player_list = clean_data()
     balance_team(player_list)

if __name__ == '__main__':
    main()