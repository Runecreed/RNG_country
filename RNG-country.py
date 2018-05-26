from easygui import *

import os
import sys
import math

import random
from PIL import Image, ImageDraw
from pathlib import Path, PureWindowsPath


dirpath = os.getcwd()
print("current directory is : " + dirpath)
foldername = os.path.basename(dirpath)
print("Directory name is : " + foldername)
scriptpath = os.path.realpath(__file__)
print("Script path is : " + scriptpath)


colors = [(230, 25, 75),
          (60, 180, 75),
          (255, 225, 25),
          (0, 130, 200),
          (245, 130, 48),
          (145, 30, 180),
          (70, 240, 240)
          ]

color_names = ["red", "green", "yellow", "blue", "orange", "purple", "cyan"]

# directory = r'D:\Documents\Kevin Prive\Programming\Projects\Atom Workspace\Python'

player_list = []
nextPlayerIndex = 0         # Start with the first player

country_list = ['England',
                "France",
                "Germany",
                "Italy",
                "Austria",
                "Russia",
                "Turkey"]

province_list = [
    ("Africa", [197, 810, 233, 840]),
    ("Albania", [591, 710, 602, 725]),
    ("Ankara", [867, 694, 886, 715]),
    ("Apulia", [518, 698, 533, 712]),
    ("Armenia", [968, 721, 986, 734]),
    ("Belgium", [363, 468, 381, 483]),
    ("Berlin", [493, 430, 511, 452]),
    ("Bohemia", [503, 505, 521, 519]),
    ("Brest", [279, 494, 292, 506]),
    ("Budapest", [581, 596, 604, 610]),
    ("Bulgaria", [677, 681, 692, 695]),
    ("Burgundy", [362, 555, 374, 569]),
    ("Clyde", [267, 295, 284, 307]),
    ("Constantinople", [746, 732, 763, 749]),
    ("Denmark", [448, 355, 465, 371]),
    ("Edinburg", [306, 299, 326, 311]),
    ("Finland", [661, 184, 685, 196]),
    ("Galicia", [651, 507, 671, 527]),
    ("Gascony", [271, 569, 287, 583]),
    ("Greece", [618, 733, 635, 747]),
    ("Holland", [386, 446, 399, 458]),
    ("Iceland", [237, 59, 263, 78]),
    ("Ireland", [224, 345, 239, 362]),
    ("Kiel", [441, 436, 462, 454]),
    ("Liverpool", [286, 379, 303, 397]),
    ("Livonia", [648, 393, 664, 412]),
    ("London", [307, 413, 323, 426]),
    ("Marseilles", [338, 609, 358, 623]),
    ("Moscow", [728, 375, 749, 395]),
    ("Munich", [427, 507, 448, 521]),
    ("Napoli", [505, 713, 518, 725]),
    ("Norway", [472, 215, 491, 234]),
    ("Paris", [303, 532, 318, 546]),
    ("Picardy", [325, 480, 343, 492]),
    ("Piemonte", [400, 602, 418, 615]),
    ("Portugal", [96, 681, 114, 697]),
    ("Prussia", [544, 413, 565, 429]),
    ("Roma", [464, 681, 481, 694]),
    ("Ruhr", [413, 477, 428, 496]),
    ("Rumania", [707, 586, 723, 602]),
    ("Petersburg", [752, 256, 774, 272]),
    ("Serbia", [607, 655, 625, 676]),
    ("Smyrna", [861, 755, 875, 769]),
    ("Spain", [178, 689, 199, 709]),
    ("Stevastopol", [811, 514, 835, 534]),
    ("Stilesia", [530, 463, 552, 477]),
    ("Sweden", [537, 212, 559, 235]),
    ("Switz", [402, 558, 417, 571]),
    ("Syria", [916, 820, 933, 842]),
    ("Trieste", [548, 610, 567, 624]),
    ("Tunisia", [392, 844, 415, 856]),
    ("Tuscany", [446, 646, 462, 663]),
    ("Tyrolia", [496, 545, 512, 560]),
    ("Ukraine", [721, 510, 741, 524]),
    ("Venezia", [447, 610, 463, 628]),
    ("Vienna", [543, 540, 560, 554]),
    ("Wales", [270, 407, 287, 424]),
    ("Warsaw", [628, 448, 650, 463]),
    ("York", [311, 386, 327, 397]),
]
#
# province_list = [
#     ("Ankara", [867, 694, 886, 715]),       # list of tuples, [0][0] is name, [0][1][0] is x1 coord, etc.
#     ("Belgium", []),
#     ("Berlin",
#     ("Brest", []),
#     ("Budapest", []),
#     ("Bulgaria", []),
#     ("Constantinople", []),
#     ("Denmark", []),
#     ("Edinburgh", []),
#     ("Greece",
#     ("Holland", []),
#     ("Kiel",
#     ("Liverpool", []),
#     ("London",
#     ("Marseilles", []),
#     ("Moscow",
#     ("Munich", []),
#     ("Naples", []),
#     ("Norway", []),
#     ("Paris", []),
#     ("Portugal", []),
#     ("Rome",
#     ("Rumania", []),
#     ("Saint Petersburg", []),
#     ("Serbia",
#     ("Sevastopol", []),
#     ("Smyrna",
#     ("Spain", []),
#     ("Sweden", []),
#     ("Trieste", []),
#     ("Tunis",
#     ("Venice", []),
#     ("Vienna", []),
#     ("Warsaw", []),
#     ("Clyde", []),
#     ("Yorkshire", []),
#     ("Wales",
#     ("Picardy", []),
#     ("Gascony", []),
#     ("Burgundy", []),
#     ("North Africa", []),
#     ("Ruhr",
#     ("Prussia", []),
#     ("Silesia", []),
#     ("Piedmont", []),
#     ("Tuscany", []),
#     ("Apulia",
#     ("Tyrolia", []),
#     ("Galicia", []),
#     ("Bohemia", []),
#     ("Finland", []),
#     ("Livonia", []),
#     ("Ukraine", []),
#     ("Albania", []),
#     ("Armenia", []),
#     ("Syria"
# ]

water_territories = [
    "North Atlantic Ocean",
    "Mid Atlantic Ocean",
    "Norweigian Sea",
    "North Sea",
    "English Channel",
    "Irish Sea",
    "Heligoland Blight",
    "Skagerrak",
    "Baltic Sea",
    "Gulf of Bothnia",
    "Berents Sea",
    "Western Mediterranean",
    "Gulf of Lyonsn",
    "Tyrrhenian Sea",
    "Ionian Sea",
    "Adriatic Sea",
    "Aegean Sea",
    "Eastern Mediterranean",
    "Black Sea"
]
supply_territories = [
    "Ankara",
    "Belgium",
    "Berlin",
    "Brest",
    "Budapest",
    "Bulgaria",
    "Constantinople",
    "Denmark",
    "Edinburgh",
    "Greece",
    "Holland",
    "Kiel",
    "Liverpool",
    "London",
    "Marseilles",
    "Moscow",
    "Munich",
    "Naples",
    "Norway",
    "Paris",
    "Portugal",
    "Rome",
    "Rumania",
    "Saint Petersburg",
    "Serbia",
    "Sevastopol",
    "Smyrna",
    "Spain",
    "Sweden",
    "Trieste",
    "Tunis",
    "Venice",
    "Vienna",
    "Warsaw"
]

#
# def get_random_color(pastel_factor=0.5):
#     return [math.floor(100*(x + pastel_factor) / (1.0 + pastel_factor)) for x in [random.uniform(0, 1.0) for i in [1, 2, 3]]]
#
#
# def color_distance(c1, c2):
#     return sum([abs(x[0] - x[1]) for x in zip(c1, c2)])
#
#
# def generate_new_color(existing_colors, pastel_factor=0.5):
#     max_distance = None
#     best_color = None
#     for i in range(0, 100):
#         color = get_random_color(pastel_factor=pastel_factor)
#         if not existing_colors:
#             return color
#         best_distance = min([color_distance(color, c)
#                              for c in existing_colors])
#         if not max_distance or best_distance > max_distance:
#             max_distance = best_distance
#             best_color = color
#     return best_color


def distributeCountry():
    global nextPlayerIndex
    # make a copy of the list, empty it continually.
    myList = province_list

    if not player_list:
        print("add players first")
        return

    while len(myList) > 0:       # keep going till empty

        if nextPlayerIndex is len(player_list) - 1:       # update to next player
            nextPlayerIndex = 0
        else:
            nextPlayerIndex = nextPlayerIndex + 1

        # current player to assign stuff to
        player = player_list[nextPlayerIndex]['name']

        chosen_country = random.randint(
            0, len(myList) - 1)  # assign random country
        # grab the country tuple and delete it from the list of choices
        country = myList.pop(chosen_country)

        player_list[nextPlayerIndex]['countries'].append(country)

        print(player, "has been given ", country[0])       # say it


# take the player list, get the countries assigned to them, paint them in the desired color


def paintCountries():
    map =  os.path.join(dirpath, 'map.jpg')
    im = Image.open(map)
    draw = ImageDraw.Draw(im)
    for player in player_list:
        color = player['color']
        for country in player['countries']:
            coord = country[1]
            draw.ellipse(xy=coord, fill=tuple(color))
    del draw
    im.save(os.path.join(dirpath, 'mapDrawn.jpg'), "JPEG")

# write to stdout


def addPlayer(name):
    if(name in player_list):
        "name already taken"
        return
    player_list.append({"name": name, 'countries': []})


def getPlayerList():
    return str("\n \t \t \t ".join([player['name'] for player in player_list]))


def getPlayerCountries(name):
    pass


# GUI
def GUI():
    msgbox("Welcome to the RNG Country thingy")

    name = enterbox("Add a player!")
    addPlayer(name)
    title = "RNG MACHINE"
    choices = ["Add Player", "Continue"]

    while boolbox("Do you want to add more players?? \n \n Curerent players are: \n \t \t \t " + getPlayerList(), choices=choices):
        playerName = enterbox("Add a player!")
        addPlayer(playerName)

    else:
        # generate colors for all players
        for index, player in enumerate(player_list):
            # grab a color from the predefined set (at most 7)
            color = colors[index]
            player['color'] = color  # assign it

        choices = ["The 7 Countries", "All the Provinices"]
        if (boolbox("What do you want to distribute?", choices=choices)):
            theList = country_list
        else:
            theList = province_list

        distributeCountry()
        paintCountries()

        msgbox(
            "Distribution Finished! The following players have been given these countries:")
        for index, player in enumerate(player_list):
            msg1= str(player['name']) + '(' + color_names[index].upper() + ")"
            msg2 = "\n".join([x[0] for x in player['countries']])
            codebox(msg=msg1, text=msg2)
        msgbox(msg="Your Layout", image="mapDrawn.jpg")

GUI()

# GOTTA MAKE SURE EVERYONE GETS SUPPLY DEPOS THOUGH
