__author__ = 'AnirudhSridhar'
#!/usr/bin/python           # This is server.py file

import socket               # Import socket module
import random
from dealer import *
from blackjack import *
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
while True:

   c, addr = s.accept()
   disp_cards_d(d_a,d_c)
   d=sumval_d(d_b,d_d)
   disp1(d_a,d_c)
   p=int(c.recv(1024))
   dealer_player(d,0)
   win(p,d)
   c.close()                # Close the connection