#input("█░▒▓┐└─║║╗╝╚╔═┼")
import os, random
os.system("cls")

master_list_of_first_names = []
with open(r"C:\Users\Joel\programming class\first names.csv", 'r') as opened_file:
	for line in opened_file:
		split_line = line.split(',')
		master_list_of_first_names.append(split_line[1])
		master_list_of_first_names.append(split_line[4])
master_list_of_last_names = []
with open(r"C:\Users\Joel\programming class\last names.csv", 'r') as opened_file:
	for line in opened_file:
		split_line = line.split(',')
		master_list_of_last_names.append(split_line[1])

def multiplyArrayByNumber(array, number):
	result = []
	for i in array:
		result.append(i * number)
	return result

def outOfBounds(location_vector):
	"""
		return False if this is a valid location to move based on boundaries
	"""
	x, y = location_vector
	if x<1:
		return True
	if y<1:
		return True
	if y>len(GameData.game_map.split('\n'))-2:
		return True
	if x>len(GameData.game_map.split('\n')[GameData.player_y])-2:
		return True
	return False
def inPit(location_vector):
	"""
		return False if this is a valid location to move based on pits
	"""
	return location_vector in GameData.dug_up_places

def randomName():
	return random.choice(master_list_of_first_names) + " " + random.choice(master_list_of_last_names)
def getTreasure():
	return ("", 0)

def go(direction_vector, speed):
	if speed==0:
		return False
	movement_vector = list(i*speed for i in direction_vector)
	location_vector = (GameData.player_x + movement_vector[0], GameData.player_y + movement_vector[1])
	if outOfBounds(location_vector) or inPit(location_vector):
		return go(direction_vector, speed-1)
	GameData.player_x += movement_vector[0]
	GameData.player_y += movement_vector[1]
	return True
def goDig():
	what_you_dug_up = random.randint(0, 1)
	what_to_say = ""
	if what_you_dug_up==0: # found body
		GameData.bodies_found += 1
		description = randomName()
		what_to_say = "You found the body of " + description
	if what_you_dug_up==1: # found treasure
		description, value = getTreasure()
		GameData.net_worth += value
		what_to_say = "You found " + description
	input(what_to_say + " (Press Enter)")
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
	game_map = """╔════════════════════════════════════════════════╗
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
║                                                ║
╚════════════════════════════════════════════════╝"""
	player_x = 12
	player_y = 7
	bodies_found = 0
	net_worth = 0
	player_icon = "┼"
	dug_icon = "▒"
	speed = 3
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
			function_to_do(GameData.how_directions_work.get(player_input), GameData.speed)
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