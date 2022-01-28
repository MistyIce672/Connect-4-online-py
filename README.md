<p align="center">
  <img src="https://imgur.com/a/TK1pBzk">
</p>

# Python connect four online/offline 
has an offline and online version
uses ngrok for over the web gameplay

## **Features** : 
-automatic separate checks for verticle horizontal and diagonal wins
-server-side and client-side scripts

## Basic Usage offline
1) use requirements.txt to install modules  `pip install -r requirements.txt`
2) run main.py `python main.py`
3) "!" shows the location of the last move

## Basic Usage online
1) use requirements.txt to install modules  `pip install -r requirements.txt` (NumPy is only needed for server script)
2) run server.py `python main.py` 
3) run `ngrock TCP 55555` to host over the internet [ngrock documentation](https://ngrok.com/docs)
4) run the client `python client.py`
5) to connect over the internet type the address and IP provided by ngrok [ngrock documentation](https://ngrok.com/docs)
6) once 2 clients connect game will begin 
7) "!" shows the location of the last move

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

## Resources

network.py originally by [tech with tim](https://youtu.be/McoDjOCb2Zo)
**ngrock**
ngrock is a tool for making local ports publicly available 
ngrock is used in place of port forwarding 
ngrock is an easy alternative to port warding
ngrock has more features read abt them [here](https://ngrok.com/docs))

## help
contact me on discord MistyIce#2351  