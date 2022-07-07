from email import message
import json

# show_players receives a list of players into variable named "players"  It then goes through the players and displays them.
#
# 1.  open a file called "players.dat".  If the file already exists, append to the file.  If it doesn't, it should create a new file.  
#     You should write the players first name, last name, and recent score to the file.
#
# TODO:  Encrypt player data before saving it to a file
from cryptography.fernet import Fernet

def load_key():
    """
    Loads the key named `secret.key` from the current directory.
    """
    return open("secret.key", "rb").read()


def save_players():
    f = open("players.dat", "wb")
    secret_key = load_key()
    e = Fernet(secret_key)
    json_players = json.dumps(PlayerList)
    # TODO:  Encrypt the json_player string and then store the encrypted string in the file.
    message = json_players.encode()
    json_players = e.encrypt(message)
    f.write(json_players)
    f.close()

def load_key():
    return open("secret.key", "rb").read()

def decrypt_message(message):
    key = load_key()
    f = Fernet(key)
    message = f.decrypt(message)
    decoded_message = message.decode()

    print(decoded_message)
    return decoded_message

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
    f = open("players.dat", "rb")
    players = f.read()
    decrypted_players = decrypt_message(players)
    print("players is {}".format(decrypted_players))
    PlayerList = json.loads(decrypted_players)
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