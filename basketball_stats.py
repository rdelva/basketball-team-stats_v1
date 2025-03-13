import copy
import constants #contains 2 constant lists called TEAMS and PLAYERS


#Reads the existing player data from the PLAYERS constats
def clean_data():
    players_copy = copy.deepcopy(constants.PLAYERS)
    teams_copy = copy.deepcopy(constants.TEAMS)
    cleaned_player_list = []


    for player in players_copy:
        player['name']
        
        guardian_split = player['guardians'].split("and")
        player['guardians'] = guardian_split

        if(player['experience'] == 'YES'):
            player['experience'] = True
        else:
            player['experience'] = False

        player['height'] = int(player['height'].split(" ")[0])

        cleaned_player_list.append(player)

    return cleaned_player_list

def main():
    print("Hello from inside main")
    print(clean_data())


if __name__ == "__main__":
    main()