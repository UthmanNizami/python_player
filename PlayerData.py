import json

# show_players receives a list of players into variable named "players"  It then goes through the players and displays them.
#
# 1.  open a file called "players.dat".  If the file already exists, append to the file.  If it doesn't, it should create a new file.  
#     You should write the players first name, last name, and recent score to the file.

def save_players():
    f = open("players.dat", "w")
    for player in PlayerList:
        f.write(json.dumps(player) + '\n')
    f.close()


def show_players():
    for player in PlayerList:
        print("Player's first name: {}".format(player["first"]))
        print("Player's last name: {}".format(player["last"]))
        print("Player's recent score: {}".format(player["recentScore"]))
        print("Player's address: {}".format(player["address"]))
    return


def read_and_load_players():
    #print("The player list is: {}".format(PlayerList))

    still_reading = True
    f = open("players.dat", "r")

    while still_reading:
        player = f.readline()
        if not player:
            still_reading = False
            break
        
        player = json.loads(player)
        PlayerList.append(player)
    
    f.close()

    # expected output ""Contents of PlayerData: { "first": <first name>, "last": <last name>, "score": <entered score>}"
    return

PlayerList = []
# Ask the user if they want to create new players or if they want to laod the existing saved players.
# If the user wants to add new players then go ahead and ask for new players as usual.
# If the user wants to load existing players then run the function read_and_load_players()
load = False
print("Do you want to load the existing players or add new players?")
load = input("Enter 'existing' to load existing players or 'new' to create new players: ")
if load == "existing":
    read_and_load_players()
elif load == "new":
    add = False
    while add != "":
        PlayerData = {}
        add = input("Press enter to stop adding players. \nEnter the players first name: ")
        if add != "":
            PlayerData["first"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players last name: ")
        if add != "":
            PlayerData["last"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players recent score: ")
        if add != "":
            PlayerData["recentScore"] = add
        else:
            break
        add = input("Press enter to stop adding players. \nEnter the players address: ")
        if add != "":
            PlayerData["address"] = add
        PlayerList.append(PlayerData)
    save_players()

show_players()


#read_and_load_players()



    # PlayerInfo1 = {
    #     "FirstName": "Khurram",
    #     "LastName": "Nizami",
    #     "CurrentScore": 3000,
    #     "BackPack": [{ "strength": 30, "durability": 5, "name": "Master Sword"}],
    #     "equipped": BackPack[0]        
    # }