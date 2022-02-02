import pygame, sys 
import numpy as np
from network import Network

pygame.init()
turn = "nut"
ofct = 0
player = 1
RED = (255, 0, 0)
YELLOW = (255,255,51)
BG_COLOR = (0, 128, 255)
BLACK = (0,0,0)
GRAY = (160,160,160)
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
waiting = True

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
	CIRCLE_COLOR = GRAY
	col = 0
	row = 0
	if player == 1:
		CIRCLE_COLOR = RED
	if player == 2:
		CIRCLE_COLOR = YELLOW
	if waiting == True:
		CIRCLE_COLOR = GRAY
	if turn == "nut":
		CIRCLE_COLOR = GRAY
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
	global game,winner,player
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
	if waiting == True:
		font = pygame.font.Font("comic.ttf", 60)
		textw = font.render(f"waiting for player 2", 1, BLACK)
		screen.blit(textw, (100,300))
	if game == "won":
		if winner == 1:
			player = "you"
		elif winner == 2:
			player = "enemy"
		font = pygame.font.Font("comic.ttf", 90)
		text = font.render(f"{player} wins", 1, BLACK)
		screen.blit(text, (100,300))
	if game == "draw":
		font = pygame.font.Font("comic.ttf", 90)
		text = font.render("game is draw", 1, BLACK)
		screen.blit(text, (100,300))
	pygame.display.update()

#creating connectiion and getting player
ip = str(input("Enter ip leave blank for local host: "))
if ip == "":
	ip = "127.0.0.1"
	print("starting on local host")
port = input("Enter port: ")
try:
	port = int(port)
except:
	port = 55555
	print("starting on port 55555")
n = Network(ip,port)
player = int(n.getP())
if player == 2:
	waiting == False

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Connect 4' )
screen.fill( BG_COLOR )

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif waiting == True:	
			stat = n.send("waiting")
			if stat == "start":
				waiting = False
				turn = "nut"
				screen.fill( BG_COLOR )
		#getttin turn
		elif turn == "nut":
			turn = n.send("wft")
			if turn == "ut":
				lm = n.send("getlm")
				print(lm)
				wrl = lm.split(",")[1]
				lm = lm.split(",")[0]
				if lm != "none":
					if player == 1:
						enemy = 2
					if player == 2:
						enemy = 1
					sc = insert(int(lm)-1,enemy)
					if wrl == "loose":
						print("you lose")
						game = "won"
						winner = 2
						run = False
					elif wrl == "draw":
						print("board is full game is draw")
						game = "draw"
						run = False
					elif wrl == "cnt":
						continue

		#waiting for player 2
		elif event.type == pygame.MOUSEBUTTONDOWN and run == True and turn=="ut":

			mouseX = event.pos[0] # x
			mouseY = event.pos[1] # y

			clicked_row = int(mouseY // SQUARE_SIZE)
			clicked_col = int(mouseX // SQUARE_SIZE)

			if getrowstatus(clicked_col) == False:
				print(clicked_col)
				sc = n.send(f'move,{clicked_col+1}')
				ins = insert(clicked_col,player)
				ins = sc.split(",")
				if ins[2] == "win":
					run = False
					game = "won"
					winner = 1
				if ins[2] == "draw":
					run = False
					game = "draw"
				turn = "nut"
				if ins == "overflow":
					ofct += 1
	drawboard()
	drawcircles(player)
	pygame.display.update()