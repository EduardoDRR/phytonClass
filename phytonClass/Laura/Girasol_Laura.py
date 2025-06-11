from turtle import *
from math import *

speed (0)  # Speed of the turtle
bgcolor("black") # Background color
goto(0,-40) # Position of the flower

#draw leaves
for i in range (12):
	for j in range (12):
		color('#ff5594'), rt(90)
		circle(150-j*2, 90), lt(90)
		circle(150-j*2, 90), rt(90)
	circle(40,24)

#draw flower center
color('black')
shape('circle')
shapesize(0.5)
fillcolor('#FFCFDE')
golden_angle = 137.508
phi = golden_angle * pi / 180

for i in range (50):
	r = 3* sqrt(i)
	theta = phi * i
	x = r * cos(theta)
	y = r * sin(theta)
	penup(), goto(x, y)
	setheading(i*golden_angle),
	pendown(), stamp()

#define point to draw the letters
def point(x, y):
	penup(), goto(x, y), pendown()
	color('black'), fillcolor('#FF0700'), 
	begin_fill(), circle(4), end_fill()

#fuction draw 'T'
def draw_T(x, y):
	position_t = [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30),
				(x+24, y+30), (x+12, y+30), (x+12, y+24), (x+12, y+18),
 				(x+12, y+12), (x+12, y+6), (x+12, y)]
	
	for pos in position_t:
		point(*pos)

#fuction draw 'Ú'
def draw_U(x,y):
	position_u = [(x,y+30), (x,y+24), (x,y+18), (x,y+12), (x,y+6),
				(x+3,y+3), (x+6,y), (x+12,y-1), (x+18,y),
				(x+21,y+3), (x+24,y+6), (x+24,y+12), (x+24,y+18),
				(x+24,y+24),(x+24,y+30), (x+12,y+36), (x+16,y+40)]
	for pos in position_u:
		point(*pos)
	
#draw TÚ	
draw_T(-27,-20)
draw_U(7,-20)

hideturtle()
done()

#
# [(x, y+30), (x+6, y+30), (x+12, y+30), (x+18, y+30),
# 				(x+24, y+30), (x+12, y+30), (x+12, y+24), (x+12, y+18),
# 				(x+12, y+12), (x+12, y+6), (x+12, y)]

# [(x,y+30), (x,y+24), (x,y+18), (x,y+12), (x,y+6),
# 				(x+3,y+3), (x+6,y), (x+12,y-1), (x+18,y),
# 				(x+21,y+3), (x+24,y+6), (x+24,y+12), (x+24,y+18),
# 				(x+24,y+24),(x+24,y+30), (x+12,y+36), (x+16,y+40)]




