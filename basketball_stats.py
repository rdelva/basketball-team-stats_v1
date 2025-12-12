import copy
import constants




def intro_menu():

    print("BASKETBALL TEAM STATS TOOL")
    print("\n ---- MENU---- \n")
    print("Here are  your choices: \n\n A) Display Team Stats \n B) Quit \n")
    
    menu_choice = input("Enter an option: ").lower()

    if(menu_choice == "a"):
        print(" A) Panthers \n B) Bandits \n C) Warriors")
    else: 
        exit()
    
    team_choice = input("\n Enter an option: ").lower()
   
    if (team_choice == "a"):
        return "Panthers"
        
    elif (team_choice == "b"):
        return "Bandits"
    else:
        return "Warriors"   

team_choice = intro_menu()


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

player_list = clean_data()

def balance_team(player_list):
    # print(player_list)

    # determinues how many people in a team
    teams = copy.deepcopy(constants.TEAMS)
    num_players_team = int(len(player_list) / len(teams))

    #Turn the teams list into the list of dictionaries
    teams_list = [{team:[]} for team in teams ]
  

    #sort each player into Teams List

    for index, player in enumerate(player_list):
        if index <= num_players_team - 1: 
            teams_list[0]['Panthers'].append(player)
        elif index <= (num_players_team * 2) - 1:
             teams_list[1]['Bandits'].append(player)
        else: 
             teams_list[2]['Warriors'].append(player)

    return teams_list



teams_list = balance_team(player_list)

def team_stats(team_choice, teams_list):
  
    print(f'Team: {team_choice} Stats')
    print("--------------------\n")
   

    team_members = [] # stores the team_members info
    # selected_choice = is a list of dictionaries. Depending on which team you choose it will go the dictionary group that holds the team info
    selected_choice = teams_list[0][f'{team_choice}']
    for name in selected_choice:        
        print(name['name'])
        team_members.append(name['name'])

    
    #Total Players
    print(f'Total players: { len(selected_choice)}')    
 
    #Team Member List
    print(", ".join(team_members))      

    continue_option = input("Press Enter to continue...")

    if(continue_option == )     
       


team_info = team_stats(team_choice, teams_list) 
print(team_info)
def results():
    print("")

def main():
    results()
    
    
    
    
    

if __name__ == '__main__':
    main()