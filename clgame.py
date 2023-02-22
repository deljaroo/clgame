#input("█░▒▓┐└─║║╗╝╚╔═┼")
import os, random
os.system("cls")

def go(how_much_tuple):
    GameData.player_x += how_much_tuple[0]
    GameData.player_y += how_much_tuple[1]
    if GameData.player_x < 1:
        GameData.player_x = 1
    if GameData.player_y < 1:
        GameData.player_y = 1
    max_y = len(GameData.game_map.split('\n'))
    if GameData.player_y > max_y - 2:
        GameData.player_y = max_y - 2
    max_x = len(GameData.game_map.split('\n')[GameData.player_y])
    if GameData.player_x > max_x - 2:
        GameData.player_x = max_x - 2
def goDig():
    input("That worked! (Press Enter)")
    GameData.dug_up_places.add((GameData.player_x, GameData.player_y))
def goWait():
    input("good job? (Press Enter)")

def drawMap():
    final_map = ""
    split_map = GameData.game_map.split('\n')
    for y in range(len(split_map)):
        for x in range(len(split_map[y])):
            if (x, y) == (GameData.player_x, GameData.player_y):
                final_map += GameData.player_icon
            elif (x, y) in GameData.dug_up_places:
                final_map += GameData.dug_icon
            else:
                final_map += split_map[y][x]
        final_map += '\n'
    print(final_map)


class GameData:
    game_map = """##################################################
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
#                                                #
##################################################"""
    player_x = 12
    player_y = 7
    player_icon = "┼"
    dug_icon = "▒"
    speed = 1
    area_desc = "An open field in the veldt.  Grass as far as the eyes can see."
    things_you_can_do = {
        'north': go,
        'south': go,
        'east': go,
        'west': go,
        'dig': goDig,
        'wait': goWait
    }
    how_directions_work = {
        'north': (0, -1),
        'south': (0, 1),
        'east': (1, 0),
        'west': (-1, 0)
    }
    dug_up_places = set()

alive = True
while alive:
    game_map = GameData.game_map
    player_y = GameData.player_y
    player_x = GameData.player_x
    player_icon = GameData.player_icon
    things_you_can_do = GameData.things_you_can_do
    how_many_lines = 0
    drawMap()
    print(GameData.area_desc)
    player_input = input("What's next? ")
    player_input = player_input.lower()
    if player_input in things_you_can_do:
        function_to_do = things_you_can_do.get(player_input)
        if function_to_do is go:
            function_to_do(GameData.how_directions_work.get(player_input))
        else:
            function_to_do()
    else:
        print("I don't know what that means")
        input("Press enter to continue")

    os.system('cls')

print("you've died; sorry; game over")

# display the gamestate in our "UI" -------------

# ask them what to do again -----------------

# evaluate what the player says to do

# change the gamestate based on that evaluation

# go back to top ---------------------