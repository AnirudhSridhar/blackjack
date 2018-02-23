import random
import math
from db1 import *

i = random.randint(0,51)
j = random.randint(0,51)
k = random.randint(0,51)
l = random.randint(0,51)

card1 = str(x[i])
value1 = str(y[i])
card2 = str(x[j])
value2 = str(y[j])
card3 = str(x[k])
value3 = str(y[k])
card4 = str(x[l])
value4 = str(y[l])

p_a = card1[2:-2]
p_b = int(value1[1:-1])
p_c = card2[2:-2]
p_d = int(value2[1:-1])

p_hit1 = card3[2:-2]
p_hit1v = int(value3[1:-1])
p_hit2 = card4[2:-2]
p_hit2v = int(value4[1:-1])
p_hitv = [p_hit1v,p_hit2v]
p_hit = [p_hit1,p_hit2]

def sumval_p(x,y):
    s_p=x+y
    return s_p
    print s_p

def disp_cards_p(m,n):
    print "player cards\n"+str(m)+" "+str(n)
