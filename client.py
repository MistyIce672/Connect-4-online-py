from network import Network
import os

smthing = True
red = "x"
blue = "o"
empty = " "
row1 = [empty,empty,empty,empty,empty,empty]
row2 = [empty,empty,empty,empty,empty,empty]
row3 = [empty,empty,empty,empty,empty,empty]
row4 = [empty,empty,empty,empty,empty,empty]
row5 = [empty,empty,empty,empty,empty,empty]
row6 = [empty,empty,empty,empty,empty,empty]
row7 = [empty,empty,empty,empty,empty,empty]
r1 = False
r2 = False
r3 = False
r4 = False
r5 = False
r6 = False
r7 = False

def getvd(player):
	loop = True
	num = int(input(f"player {player} input row 1 to 7: "))
	if num > 0 and num < 8 and iof(num) == False:
		loop = False
	while loop == True:
		if num < 1 or num > 7:
			print("invalid input try again")
		elif iof(num) != False:
			print("row is full try again")
		if num > 0 and num < 8 and iof(num) == False:
			loop = False
			break
		num = int(input(f"player {player} input row 1 to 7: "))
	return(num)

def mf(rownum):
	global r1,r2,r3,r4,r5,r6,r7
	if rownum == 1:
		r1 = True
	if rownum == 2:
		r2 = True
	if rownum == 3:
		r3 = True
	if rownum == 4:
		r4 = True
	if rownum == 5:
		r5 = True
	if rownum == 6:
		r6 = True
	if rownum == 7:
		r7 = True

def iof(rownum):
	names = [r1,r2,r3,r4,r5,r6,r7]
	rownum -= 1
	return(names[rownum])

def getrow(rownum):
	try:
		names = [row1,row2,row3,row4,row5,row6,row7]
		rownum -= 1
		return(names[rownum])
	except:
		return(False)

def insert(row,value):
	stat = ("overflow pls try differnt row")
	row = getrow(row)
	if row == False:
		stat = "invalid input try again"
	elif row != False:
		for index, i in enumerate(row):
			if i == empty:
				row[index]=value
				if row[5] != empty:
					stat = "overflow"
				elif row[5] == empty:
					stat = True
				break
	return(stat)

def printbd(rownum):
	pointer = [" "," "," "," "," "," "," "]
	pointer[rownum-1] = "!"
	names = [row1,row2,row3,row4,row5,row6,row7]
	position = 5
	print(pointer)
	while position >= 0:
		column=[]
		for i in names:
			column.append(i[position])
		print(column)
		position-=1
	print("\n")

def main(player):
	global smthing
	print("You are player", player)
	run = True
	while run == True:
		waiting = True
		while waiting ==True:
			try:
				stat = n.send("wft")
				if stat == "nut":
					continue
				if stat == "ut":
					waiting = False
					lm = n.send("getlm")
					wrl = lm.split(",")[1]
					lm = lm.split(",")[0]
					if lm != "none":
						log = insert(int(lm),blue)
						if log == "overflow":
							mf(move)
						printbd(int(lm))
						if wrl == "loose":
							print("you lose")
							run = False
							smthing = False
						elif wrl == "draw":
							print("board is full game is draw")
							run = False
							smthing = False
						elif wrl == "cnt":
							continue
			except error as e:
				print(e)
				print("erroe while waiting")
		if run == False:
			break
		move = getvd(player)
		sc = n.send(f'move,{move}')
		log = insert(move,red)
		printbd(move)
		if log == "overflow":
			mf(move)
		if sc.split(",")[2] == "win":
			run = False
			smthing = False
			print("you win")
		elif sc.split(",")[2] == "cnt":
			continue
		elif sc.split(",")[2] == "draw":
			run = False
			smthing = False
			print("board is full game is draw")

def menu_screen():
    print("waiting for player 2 to join")
    waiting = True
    while waiting == True:
    	try:
    		stat = n.send("waiting")
    		if stat != "wait":
    			waiting = False
    	except:
    		print("error while getting status")
    main(player)

while smthing == True:
	ip = str(input("Enter ip: "))
	port = int(input("Enter port: "))
	os.system('cls')
	n = Network(ip,port)
	player = int(n.getP())
	if player == 1:
		menu_screen()
	if player == 2:
		main(player)from network import Network
import pickle
smthing = True

def getrow(rownum):
	try:
		names = [row1,row2,row3,row4,row5,row6,row7]
		rownum -= 1
		return(names[rownum])
	except:
		return(False)

def insert(row,value):
	stat = ("overflow pls try differnt row")
	row = getrow(row)
	if row == False:
		stat = "invalid input try again"
	elif row != False:
		for index, i in enumerate(row):
			if i == empty:
				row[index]=value
				if row[5] != empty:
					stat = "overflow"
				elif row[5] == empty:
					stat = True
				break
	return(stat)

def printbd(rownum):
	pointer = [" "," "," "," "," "," "," "]
	pointer[rownum-1] = "!"
	names = [row1,row2,row3,row4,row5,row6,row7]
	position = 5
	print(pointer)
	while position >= 0:
		column=[]
		for i in names:
			column.append(i[position])
		print(column)
		position-=1

red = "x"
blue = "o"
empty = " "
row1 = [empty,empty,empty,empty,empty,empty]
row2 = [empty,empty,empty,empty,empty,empty]
row3 = [empty,empty,empty,empty,empty,empty]
row4 = [empty,empty,empty,empty,empty,empty]
row5 = [empty,empty,empty,empty,empty,empty]
row6 = [empty,empty,empty,empty,empty,empty]
row7 = [empty,empty,empty,empty,empty,empty]

def main(player):
	global smthing
	print("You are player", player)
	run = True
	while run == True:
		waiting = True
		while waiting ==True:
			try:
				stat = n.send("wft")
				if stat == "nut":
					continue
				if stat == "ut":
					waiting = False
					lm = n.send("getlm")
					print(lm)
					wrl = lm.split(",")[1]
					lm = lm.split(",")[0]
					if lm != "none":
						sc = insert(int(lm),blue)
						printbd(int(lm))
						if wrl == "loose":
							print("you lose")
							run = False
							smthing = False
						elif wrl == "draw":
							print("board is full game is draw")
							run = False
							smthing = False
						elif wrl == "cnt":
							continue
			except error as e:
				print(e)
				print("erroe while waiting")
		if run == False:
			break
		move = int(input(f"player {player} input row 1 to 7: "))
		sc = n.send(f'move,{move}')
		log = insert(move,red)
		printbd(move)
		if sc.split(",")[2] == "win":
			run = False
			smthing = False
			print("you win")
		elif sc.split(",")[2] == "cnt":
			continue
		elif sc.split(",")[2] == "draw":
			run = False
			smthing = False
			print("board is full game is draw")
def menu_screen():
    print("waiting for player 2 to join")
    waiting = True
    while waiting == True:
    	try:
    		stat = n.send("waiting")
    		if stat != "wait":
    			waiting = False
    	except:
    		print("error while getting status")
    main(player)
while smthing == True:
	n = Network()
	player = int(n.getP())
	if player == 1:
		menu_screen()
	if player == 2:
		main(player)
