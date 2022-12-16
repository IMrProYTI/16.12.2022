from turtle import *

SCALE = 20
speed(0)

def myForward(n):
	global SCALE
	forward(n * SCALE)

def myCord(n):
    return n * SCALE

pd()
for _ in range(4):
	myForward(7)
	right(90)
	myForward(7)
	right(90)
	myForward(7)
	right(90)
pu()

for x in range(-1, 9):
	for y in range(-8, 2):
		goto(myCord(x), myCord(y))
		dot(5, 'red')
