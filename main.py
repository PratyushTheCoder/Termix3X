from os import path, getcwd, system, listdir, chdir
from sys import exit
import json


if path.exists(getcwd() + "/termix.json"):
    with open("./termix.json") as f:
        config=json.load(f)
        version=config['version']
        musicdir=config['musicdir']
        play=config['play']

else:
    print("Player config file not found creating one...")
    musicdir=input("Please enter the directory path of your music folder: ")
    play=input("Please specify the play command: ")
    configTemplate = {"version":"3.4.5","musicdir":f"{musicdir}","play":f"{play}"}
    with open(getcwd() + "/termix.json", "w+") as f:
        json.dump(configTemplate,f) 

  
chdir(musicdir)

if path.exists(getcwd()+'/player.json'):
    with open("./player.json", "+r") as f:
        lastplayed=json.load(f)['lastplayed']
else:
    print("Player config file not found creating one...")
    lastplayed={'lastplayed':""}
    with open('./player.json','w+') as f:
        json.dump(lastplayed,f)

print(f"""Welcome to Termix3X ({version})\n
Please select a option to continue...\n
1. Select a playlist to play from 
2. Continue from last played ({lastplayed})
3. I am feeling luck today
4. Create a new Playlist
5. Quit 
""")

action = int(input("Choice: "))

if action == 1:
    print("")
    playlists=listdir(getcwd())
    playlists.remove("ignore")
    playlists.remove("player.json")
    # print(playlists)
    i=1
    for playlist in playlists:
       print(f'{i}. {playlist}')
       i+=1
    print()
    choice=int(input("Choice: "))
    lastplayed={'lastplayed':f"{playlists[choice-1]}"}
    with open('./player.json','w+') as f:
        json.dump(lastplayed,f)
    chdir(getcwd()+f"/{playlists[choice-1]}")
    # print(getcwd())
    print()
    system(play)

elif action==2:
    chdir(getcwd()+f'/{lastplayed}')
    print()
    system(play)
    
else:
    print()
    print("Exitting...")
    exit(0)
    
        