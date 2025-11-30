import basketball_stats

def intro_menu():

    print("BASKETBALL TEAM STATS TOOL")
    print("\n ---- MENU---- \n")
    print("Here are  your choices: \n\n A) Display Team Stats \n B) Quit")
    
    menu_choice = input("Enter an option").lower()

    if(menu_choice == "a"):
        print(" A) Panthers \n B) Bandits \n C) Warriors\n")
    
    team_choice = input("Enter an option").lower()

    if (team_choice == "a"):
        return "Panthers"
    elif (team_choice == "b"):
        return "Bandits"
    else:
        return "Warriors"   




team_choice = intro_menu()