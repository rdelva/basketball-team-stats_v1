import constants



def intro():
    print("Here are your choices: \n A) Display Team Stats \n B)Quit")
    print("\n")
    choice = input("Enter an option: ")

    if choice.lower() == 'A':
        display_team_stats()
    elif choice.lower() == 'B':
         print("Ending Program ... Goodbye")
         
          

      

def  display_team_stats():
    print("Team Stats")
      

def clean_data():
    print('clean_data')        


if __name__ == "__main__":
        intro()
        display_team_stats()
        clean_data()





        