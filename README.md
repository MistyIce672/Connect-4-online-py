<p align="center">
  <img src="https://i.imgur.com/gIrTND7.png">
  <img src="https://i.imgur.com/mZaIpg1.png">
</p>

# Python connect four online/offline 
has an offline and online version
uses ngrok for over the web gameplay

## **Features** : 
-automatic separate checks for verticle horizontal and diagonal wins
-server-side and client-side scripts
-server will log and display each move

## Basic Usage offline (no GUI)
1) use requirements.txt to install modules  `pip install -r requirements.txt`
2) run main.py `python main.py` from the singleplayer folder
3) "!" shows the location of the last move

### Basic Usage offline (GUI)
1) use requirements.txt to install modules  `pip install -r requirements.txt`
2) run main.py `python main.py` from singleplayer_gui folder
3) the circles on top will show the player turn 

## Basic Usage online (no GUI)
1) use requirements.txt to install modules  `pip install -r requirements.txt` (NumPy is only needed for server script)
2) run server.py `python server.py`  from multiplayer folder
3) run `ngrock TCP 55555` to host over the internet [ngrock documentation](https://ngrok.com/docs)
4) run the client `python client.py` from the multiplayer folder
5) to connect over the internet type the address and IP provided by ngrok [ngrock documentation](https://ngrok.com/docs)
5) to connect to the localhost use IP `127.0.0.1` and port `55555`
6) once 2 clients connect game will begin 
7) "!" shows the location of the last move

### Basic Usage online (GUI)
1) use requirements.txt to install modules  `pip install -r requirements.txt` (NumPy is only needed for server script)
2) run server.py `python server.py`  from multiplayer_gui folder
3) run `ngrock TCP 55555` to host over the internet [ngrock documentation](https://ngrok.com/docs)
3) running multiplayer GUI on ngrok is not recommended due to a performance issue 
4) run the client `python client.py` from the multiplayer_gui folder
5) to connect over the internet type the address and IP provided by ngrok [ngrock documentation](https://ngrok.com/docs)
5) to connect to the local host press enter twice without typing IP or port
6) once 2 clients connect game will begin 
7) if circles on the top are grey you are waiting for the opponent to make a move

## bugs/issues

performance issue on multiplayer GUI when waiting for the server to respond window will become un responsive
if you know fix for this please let me know

## Setup

ngrok authtoken must be setup
[ngrock documentation](https://ngrok.com/docs)

the file is good to go by default but u can change some variables to ur liking

by default server will run on IP = "127.0.0.1" (localhost) post = 55555 can be changed on the top of the server-side script not necessary unless the port is already in use

variables such as the player representations can be changed on the top of main.py

## Structure

the online version is based on `main.py` read through the functions of main.py to understand client.py

the game runs and is stored on the server

the client has a dummy version of the game for printing 

client requires network.py to work 

## download

download size should be roughly 80 MB

## Resources

network.py originally by [tech with tim](https://youtu.be/McoDjOCb2Zo)
**ngrock**
ngrock is a tool for making local ports publicly available 
ngrock is used in place of port forwarding 
ngrock is an easy alternative to port warding
ngrock has more features read abt them [here](https://ngrok.com/docs))

## help
contact me on discord MistyIce#2351  
