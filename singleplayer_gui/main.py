import pygame, sys 
import numpy as np

pygame.init()
ofct = 0
player = 1
RED = (255, 0, 0)
YELLOW = (255,255,51)
BG_COLOR = (0, 128, 255)
BLACK = (0,0,0)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
WIDTH = 700
HEIGHT = 700
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = 100
CIRCLE_RADIUS = 30
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Connect 4' )
screen.fill( BG_COLOR )

red = "x"
yellow = "o"
empty = " "
game = None
run = True

row1 = [empty,empty,empty,empty,empty,empty]
row2 = [empty,empty,empty,empty,empty,empty]
row3 = [empty,empty,empty,empty,empty,empty]
row4 = [empty,empty,empty,empty,empty,empty]
row5 = [empty,empty,empty,empty,empty,empty]
row6 = [empty,empty,empty,empty,empty,empty]
row7 = [empty,empty,empty,empty,empty,empty]

def getgame(row,value):
	global ofct
	if value == 1:
		playeritem = red
	elif value == 2:
		playeritem = yellow
	row = getrow(row)
	v = vcheck(row,playeritem)
	d = dcheck(row,playeritem)
	h = hcheck(row,playeritem)
	# ending game if a check returns True
	if v == True or d == True or h ==True:
		return(["won",value])
	elif ofct == 7:
		return("draw")
	else:
		return("cont")

def hcheck(row,value):
	names = [row1,row2,row3,row4,row5,row6,row7]
	haswon = False
	count = 0
	# making a horizontal list using verticle lists
	for i in row:
		if i == empty:
			position = count-1
			break
		elif i != empty:
			position = count
		count += 1
	column = []
	for i in names:
		column.append(i[position])
	#running verticle check on the newly created list
	return(vcheck(column,value))

#verticle check
def vcheck(lis,value):
	haswon = False
	matches = 0
	#checking values below to look for a 4 of the same type
	for i in lis:
		if matches == 4:
			haswon = True
		elif i == value:
			matches += 1
		elif i == empty:
			continue
		elif i != value:
			matches = 0
	if matches == 4:
		haswon = True
	return(haswon)

#diagonal check
def dcheck(row,value):
	haswon = False
	count = 0
	for i in row:
		if i == empty:
			position = count-1
			break
		elif i != empty:
			position = count
		count += 1
	row[position] = "f"
	# creating 2d array of the board using NumPy
	matrix = np.array([row1,row2,row3,row4,row5,row6,row7])
	#making diagonal list using 2d array
	diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
	diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
	lis = ([n.tolist() for n in diags])
	l1 = None
	l2 = None
	#getting list with last inserted value
	for i in lis:
		for x in i:
			if x == "f":
				if l1 == None:
					l1 = i
				elif l1 != None:
					l2 = i
	#running verticle check on the list we just made
	count = 0
	if l1 != None:
		for i in l1:
			if i == "f":
				l1[count] = value
			count += 1
		count = 0
		if l2 != None:	
			for i in l2:
				if i == "f":
					l2[count] = value
				count += 1
		l1 = vcheck(l1,value)
		if l2 != None:
			l2 = vcheck(l2,value)
		if l1 == True:
			haswon = True
		elif l2 == True:
			haswon = True
	row[position]=value
	return(haswon)

def getrow(rownum):
	try:
		names = [row1,row2,row3,row4,row5,row6,row7]
		return(names[rownum])
	except:
		return(False)

def insert(row,value):
	if value == 1:
		value = red
	elif value == 2:
		value = yellow
	stat = ("overflow pls try differnt row")
	row = getrow(row)
	if row == False:
		stat = "invalid input try again"
	# replacing the empty value with user input
	elif row != False:
		for index, i in enumerate(row):
			if i == empty:
				row[index]=value
				#returning overflow 
				if row[5] != empty:
					stat = "overflow"
				elif row[5] == empty:
					stat = True
				break
	return(stat)

def drawcircles(player):
	col = 0
	row = 0
	if player == 1:
		CIRCLE_COLOR = RED
	if player == 2:
		CIRCLE_COLOR = YELLOW
	while col < 7:
		pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, 0 )
		col += 1

def getrowstatus(val):
	names = [row1,row2,row3,row4,row5,row6,row7]
	row = names[val]
	if row[5] != empty:
		return(True)
	else:
		return(False)

def drawboard():
	global game,winner
	names = [row1,row2,row3,row4,row5,row6,row7]
	position = 5
	# making columns using rows
	rows= []
	while position >= 0:
		column=[]
		for i in names:
			column.append(i[position])
		rows.append(column)
		position-=1
	row = 1
	for val in rows:
		col = -1
		for i in val:
			col += 1
			if i == empty:
				continue
			elif i == red:
				CIRCLE_COLOR = RED
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, 0 )
			elif i == yellow:
				CIRCLE_COLOR = YELLOW
				pygame.draw.circle( screen, CIRCLE_COLOR, (int( col * SQUARE_SIZE + SQUARE_SIZE//2 ), int( row * SQUARE_SIZE + SQUARE_SIZE//2 )), CIRCLE_RADIUS, 0 )
		row += 1
	if game == "won":
		if winner == 1:
			player = "player1"
		elif winner == 2:
			player = "player2"
		font = pygame.font.Font("comic.ttf", 90)
		text = font.render(f"{player} wins", 1, BLACK)
		screen.blit(text, (100,300))
	if game == "draw":
		font = pygame.font.Font("comic.ttf", 90)
		text = font.render("game is draw", 1, BLACK)
		screen.blit(text, (100,300))
	pygame.display.update()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		if event.type == pygame.MOUSEBUTTONDOWN and run == True :

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if getrowstatus(clicked_col) == False:
				ins = insert(clicked_col,player)
				if ins == "overflow":
					ofct += 1
				game = getgame(clicked_col,player)
				if game == "cont":
					pass
				elif game == "draw":
					run = False
				else:
					run = False
					winner = game[1]
					game = game[0]
				player = player % 2 + 1
	drawboard()
	drawcircles(player)
	pygame.display.update()