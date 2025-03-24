import basketball_stats

# Intro page for the basketball app

def intro():
    print("BASKETBALL TEAM STATS TOOL \n")
    print ("---- MENU----\n")
    print("Here are your choices: \n 1) Display Team Stats \n 2) Quit")
    print("\n\n")
    choice = int(input("Enter an option > "))
    
    if choice == 1:                       
        basketball_stats.display_team_choices() 
        #team_choice = int(input("Enter an option:"))        
        #basketball_stats.display_team_stats(number = team_choice)    
    elif choice == '2':
         print("Ending Program ... Goodbye")
         exit()
    else:
        print("Ending Program ... Goodbye")
        exit()









intro()



        