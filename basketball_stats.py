import copy
import constants


# importing the teams dictionary and players dictionary 

def clean_data():
    
    teams = copy.deepcopy(constants.TEAMS)
    print(teams)

def main():
    print("Hi")
    clean_data()

if __name__ == '__main__':
    main()