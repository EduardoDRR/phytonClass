from turtle import *
import colorsys 
import math
speed(0)
bgcolor("black")
goto(-16, 47)
h = 0
for i in range(10):
	for j in range(14):
		c= colorsys.hsv_to_rgb(0.125 , 1, 1)
		color('#ff5594')
		rt(90)
		circle(150-j*6-90)
	lt(90)
	circle(150-j*6,90)
	rt(180)
	circle(40, 24)
	color("black")
	shape("turtle")
	fillcolor("#ffe0e9")

phi = 137.508 * (math.pi/ 180.0)
for i in range (50):
	r = 0.5 * math.sqrt(i)
	theta = i*phi
	x = r * math.cos(theta)
	y = r * math.sin(theta)
	penup()
	goto(x, y)
	setheading(i * 137.508)
	pendown()
	stamp()
done()



