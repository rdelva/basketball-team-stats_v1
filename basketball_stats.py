import copy
import constants #contains 2 constant lists called TEAMS and PLAYERS


# Reads the existing player data from the PLAYERS constats
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

    balance_teams(cleaned_player_list)

# This function will blance the players across three teams: Panthers, Bandits, and Warriors.
def balance_teams(player_list):
    # determines how many people in a team
    num_players_team = int(len(constants.PLAYERS) / len(constants.TEAMS))
    teams = copy.deepcopy(constants.TEAMS) # Duplicate Team list

    
    #turn the Teams list into a list of dictionaries
    #[{key:value] for temp_vars(s) in iterable}
    
    # team_list = {team:"" for team in teams}
    team_list = [{team:[]} for team in teams]
   

    # team_list[index]['Panthers'] = []
    # print(team_list[index]['Panthers'])
    # Puts the player list into 3 teams 
    for index, player in enumerate(player_list):
        if index >=0 and index <= 5:
            team_list[0]['Panthers'].append(player)
        elif index >= 6 and index <= 11:
            team_list[1]['Bandits'].append(player)
        else:
            team_list[2]['Warriors'].append(player)

    # print(team_list) 
    display_team_stats(teams)
    return team_list
    

def display_team_choices():
    teams = copy.deepcopy(constants.TEAMS)
    for index, team in enumerate(teams, 1):  
        print(f'{index}) {team}')


def display_team_stats():



def main():    
    clean_data()
    display_team_stats()
   
   


if __name__ == "__main__":
    main()