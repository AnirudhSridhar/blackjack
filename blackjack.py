import random
import math
from db1 import *
from player import *
from dealer import *

def play_player(p, b):
	if p == 21:
		print("blackjack")
		return 21
	elif p > 21:
		print("bust")
		print("dealer wins")
	else:
		f = input("hit or stay")
		if f == "hit":
			x = b
			p = p + p_hitv[x]
			b = b + 1
			print(p)
			play_player(p,b)
		elif f == "stay":
			print(p)
		else:
			print("Incorrect Input")

def dealer_player(d, b):
	disp1(d_a, d_c)
	if d == 21:
		print("blackjack")
	elif d > 21:
		print("bust")
		print("player wins")
	else:
		f = input("hit or stay")
		if f == "hit":
			x = b
			d = d + d_hitv[x]
			b = b+1
			print(d)
			dealer_player(d,b)
		elif f == "stay":
			print d
		else:
			print("Incorrect Input")
					
def win(p,d):
	if (p<=21)&(d<=21):
		if p > d:
			print "player wins"
		if p == d:
			print "both win"
		if p < d:
			print "dealer wins"
