import numpy as np
import os

red = "x"
blue = "o"
empty = " "
p1name = "player 1"
p2name = "player 2"
player = "player1"
ofct = 0
gameover = False
row1 = [empty,empty,empty,empty,empty,empty]
row2 = [empty,empty,empty,empty,empty,empty]
row3 = [empty,empty,empty,empty,empty,empty]
row4 = [empty,empty,empty,empty,empty,empty]
row5 = [empty,empty,empty,empty,empty,empty]
row6 = [empty,empty,empty,empty,empty,empty]
row7 = [empty,empty,empty,empty,empty,empty]

#functions
#horizontal check	
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

# returns row when the index is given
#used to convert user input into usable row data
def getrow(rownum):
	try:
		names = [row1,row2,row3,row4,row5,row6,row7]
		rownum -= 1
		return(names[rownum])
	except:
		return(False)

#inserts values into rows and handles overflow
def insert(row,value):
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

#prints the current state of the board
def printbd(rownum):
	#making and printing pointer to show where last value was added
	pointer = [" "," "," "," "," "," "," "]
	pointer[rownum-1] = "!"
	names = [row1,row2,row3,row4,row5,row6,row7]
	position = 5
	print(pointer)
	# making columns using rows
	while position >= 0:
		column=[]
		for i in names:
			column.append(i[position])
		print(column)
		position-=1

#main code
#making command shell clear
os.system('cls')
while gameover == False:

	# changing player data
	if player == "player1":
		playername = p1name
		playeritem = red
	if player == "player2":
		playername = p2name
		playeritem = blue

	#getting inputs
	rinput = int(input(f"{playername} input row 1 to 7: "))
	ins = insert(rinput,playeritem)
	#handling wrong inputs
	while ins != True:
		if ins == "overflow":
			break
		print(ins)
		rinput = int(input(f"{playername} input row 1 to 7: "))
		ins = insert(rinput,playeritem)
	#handling overflow
	if ins == "overflow":
			ofct += 1
			if ofct == 7:
				#making game draw if board is full
				print("Game ended as a draw due to board being full")
				break

	# printing board state and running checks
	printbd(rinput)
	row = getrow(rinput)
	v = vcheck(row,playeritem)
	d = dcheck(row,playeritem)
	h = hcheck(row,playeritem)
	# ending game if a check returns True
	if v == True or d == True or h ==True:
		print(f"{playername} wins!")
		break

	#changing player
	if player == "player1":
		player = "player2"
	elif player == "player2":
		player = "player1"