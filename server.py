import socket
from _thread import *
import pickle
import numpy as np

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
server = "127.0.0.1"
port = 55555

def hcheck(row,value):
	names = [row1,row2,row3,row4,row5,row6,row7]
	haswon = False
	count = 0
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
	return(vcheck(column,value))

def vcheck(lis,value):
	haswon = False
	matches = 0
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
	matrix = np.array([row1,row2,row3,row4,row5,row6,row7])
	diags = [matrix[::-1,:].diagonal(i) for i in range(-3,4)]
	diags.extend(matrix.diagonal(i) for i in range(3,-4,-1))
	lis = ([n.tolist() for n in diags])
	l1 = None
	l2 = None
	for i in lis:
		for x in i:
			if x == "f":
				if l1 == None:
					l1 = i
				elif l1 != None:
					l2 = i
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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

connected = set()
games = {}
idCount = 0
p = 1
glblp = 1
t = 1
lm = "none"
winner = "none"
ofct = 0

def threaded_client(conn, p):
    global idCount,glblp,t,lm,winner,ofct
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            lis = data.split(",")
            if data == "waiting":
            	if glblp == 1:
            		conn.send("wait".encode("ascii"))
            	elif glblp == 2:
            		print("start")
            		conn.send("start".encode("ascii"))
            if data == "wft":
            	if p == t:
            		conn.send("ut".encode("ascii"))
            	elif p != t:
            		conn.send("nut".encode("ascii"))
            if data == "getlm":
            	if winner == "draw":
            		conn.send(f"{lm},draw".encode("ascii"))
            	if winner != "none":
            		conn.send(f"{lm},loose".encode("ascii"))
            	else:
            		conn.send(f"{lm},cnt".encode("ascii"))
            if len(lis) > 1:
            	if lis[0] == "move":
            		print('move')
            		if p == 1:
            			value = "x"
            		if p == 2:
            			value = "o"
            		sc = insert(int(lis[1]),value)
            		if sc == "overflow":
            			ofct += 1
            			if ofct == 7:
            				winner = "draw"
            		print("sc",sc)
            		printbd(int(lis[1]))
            		row = getrow(int(lis[1]))
            		playeritem = value
            		v = vcheck(row,playeritem)
            		d = dcheck(row,playeritem)
            		h = hcheck(row,playeritem)
            		if v == True or d == True or h ==True:
            			winner = p
            		lm = lis[1]
            		if winner == "draw":
            			conn.send(f"True,{lm},draw".encode("ascii"))
            		if winner != "none":
            			conn.send(f"True,{lm},win".encode("ascii"))
            		else:
            			conn.send(f"True,{sc},cnt".encode("ascii"))
            		if t == 1:
            			t = 2
            		elif t == 2:
            			t = 1

        except error as e:
            print(e)

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()



while True:
    conn, addr = s.accept()
    if p == 2:
    	glblp = 2
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, p,))
    if p == 1:
    	print("p changed")
    	p = 2
def hcheck(row,value):
	names = [row1,row2,row3,row4,row5,row6,row7]
	haswon = False
	count = 0
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
	return(vcheck(column,value))