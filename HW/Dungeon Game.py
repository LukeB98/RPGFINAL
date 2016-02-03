import random
CELLS = [
(0, 0), (0, 1), (0, 2),
(1, 0), (1, 1), (1, 2),
(2, 0), (2, 1), (2, 2)]
'''
GRID = [
	"|X|"
	"| |"
]
Final_grid = []
for tuple in CELLS:
	if tuple == player:
		Final_grid.append(GRID[0])
	else:
		Final_grid.append(GRID[1])
		'''
def get_locations():
	monster = monsterx, monstery = random.choice(CELLS)
	door = doorx, doory = random.choice(CELLS)
	player = playerx, playery = random.choice(CELLS)
	# monster = random
	# door = random
	# start = random
	if monster == door or monster == player or door == player:
		get_locations()
	else:
		global monster,door,player
		
	# if monster, door, or start are the same, do it again

	# return monster, door, start

def move_player(player, move):
	if move == "LEFT":
		playerx -= 1
	elif move == "RIGHT":
		playerx += 1
	elif move == "UP":
		playery -= 1
	elif move == "DOWN":
		playery += 1
	# Get the player's current location
	# If move is LEFT, y - 1
	# If move is RIGHT, y + 1
	# If move is UP, x - 1
	# If move is DOWN, x + 1
	return player
def get_moves(player):
	MOVES = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	if playery == 0:
		MOVES.remove("LEFT")
	if playerx == 0:
		MOVES.remove("UP")
	if playery == 2:
		MOVES.remove("RIGHT")
	if playerx == 2:
		MOVES.remove("DOWN")
	# if player's y is 0, remove LEFT
	# if player's x is 0, remove UP
	# if player's y is 2, remove RIGHT
	# if player's x is 2, remove DOWN
	return MOVES
cycle = 0
while True:
	cycle += 1
	if cycle == 1:
		print("Welcome to the dungeon!")
	
	print("You're currently in room {}".format(str(player))) # fill in with player position
	print("You can move {}".format(get_moves(player))) # fill in with available moves
	print("Enter QUIT to quit")

move = input("> ")
move = move.upper()

if move == 'QUIT':
break

# If it's a good move, change the player's position
# If it's a bad move, don't change anything
# If the new player position is the door, they win!
# If the new player position is the monster, they lose!
# Otherwise, continue