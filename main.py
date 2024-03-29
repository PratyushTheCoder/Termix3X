from os import path, getcwd, system, listdir, chdir, mkdir
from random import randint
from sys import exit, argv
import json


if path.exists(getcwd() + "/termix.json"):
    with open("./termix.json") as f:
        config=json.load(f)
        version=config['version']
        musicdir=config['musicdir']
        play=config['play']
        f.close()

else:
    print("""
         _,-'"'-._
       .'         `-._
     .'  _   _  _   _  `.
    | @ | | | | | | | | |  |
     '-._| | | | | | | |_.-'
       `-._| | | | | |_.-'
         `-._| | |_.-'
            `-._.-'

    Termix(4.0.1) - Music for your CLI\n""")
    print("Termix config file not found creating one...")
    musicdir=input("Please enter the directory path of your music folder: ")
    play=input("Please specify the play command: ")
    configTemplate = {"version":"4.0.1","musicdir":f"{musicdir}","play":f"{play}"}
    with open(getcwd() + "/termix.json", "w+") as f:
        json.dump(configTemplate,f) 
        f.close()
    exit(0)

def termix():
    chdir(musicdir)
    if path.exists(getcwd()+'/player.json'):
        with open("./player.json", "+r") as f:
            lastplayed=json.load(f)['lastplayed']
            f.close()
    else:
        print("Player config file not found creating one...")
        lastplayed={'lastplayed':""}
        with open('./player.json','w+') as f:
            json.dump(lastplayed,f)
            f.close()
    print(f"""
         _,-'"'-._
       .'         `-._
     .'  _   _  _   _  `.
    | @ | | | | | | | | |  |
     '-._| | | | | | | |_.-'
       `-._| | | | | |_.-'
         `-._| | |_.-'
            `-._.-'

    Termix({version}) - Music for your CLI\n
Please select a option to continue...\n
1. Select a playlist to play from 
2. Continue from last played ({lastplayed})
3. I am feeling luck today
4. Create a new Playlist
5. Quit 
""")
    playlists=listdir(getcwd())
    r=[
        'ignore',
        'player.json',
        'termix.log'
    ]
    for i in r:
        playlists.remove(i)
    try:
        action = int(input("Choice: "))

        if action == 1:
            print("")
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

        elif action==3:
            print()
            i=randint(0,len(playlists))
            chdir(getcwd()+f'/{playlists[i]}')
            print(f'Playing from {playlists[i]}')
            print()
            system(play)

        elif action==4:
            print()
            name=input("Please enter the name for the new playlist: ")
            mkdir(getcwd()+f'/{name}')
            chdir(getcwd()+f'/{name}')
            print(f"Playlist named {name} created")
            
        else:
            print()
            print("Exitting...")
            exit(0)
    except Exception as e:
        with open('./termix.log','w+') as f:
            f.write(str(e))
            f.close()
        print()
        print('Error occured')
        exit(1)

if len(argv) > 1:
    if argv[1]=="reconfig":
        musicdir=input("Please enter the directory path of your music folder: ")
        play=input("Please specify the play command: ")
        configTemplate = {"version":"3.4.5","musicdir":f"{musicdir}","play":f"{play}"}
        with open(getcwd() + "/termix.json", "w+") as f:
            json.dump(configTemplate,f) 
            f.close()
    else:
        termix()
else:
    termix()
