__author__ = 'AnirudhSridhar'
#!/usr/bin/python           # This is client.py file
import socket               # Import socket module
from blackjack import *
from player import *
from dealer import *
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.

s.connect((host, port))


disp_cards_p(p_a,p_c)
disp_cards_d(d_a,d_c)
p=sumval_p(p_b,p_d)
play_player(p,0)
s.send(str(p))

s.close                     # Close the socket when done
