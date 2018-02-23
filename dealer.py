import random
import math
from db1 import *

i = random.randint(0, 51)
j = random.randint(0, 51)
k = random.randint(0, 51)
l = random.randint(0, 51)

card1 = str(x[i])
value1 = str(y[i])
card2 = str(x[j])
value2 = str(y[j])
card3 = str(x[k])
value3 = str(y[k])
card4 = str(x[l])
value4 = str(y[l])

d_a = card1[2:-2]
d_b = int(value1[1:-1])
d_c = card2[2:-2]
d_d = int(value2[1:-1])

d_hit1 = card3[2:-2]
d_hit1v = int(value3[1:-1])
d_hit2 = card4[2:-2]
d_hit2v = int(value4[1:-1])
d_hitv = [d_hit1v, d_hit2v]
d_hit = [d_hit1, d_hit2]

def sumval_d(x, y):
    return x+y

def disp_cards_d(m,n):
    print "dealer cards\n"+str(m)+" *"

def disp1(m,n):
    print "dealer cards\n"+str(m)+" "+str(n)
