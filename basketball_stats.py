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


def main():
     player_list = clean_data()
     balance_team(player_list)

if __name__ == '__main__':
    main()