from turtle import *
sides = int(input("How many sides would you like? "))
angle = 360 / sides


for i in range(sides):
    forward(90)
    left(angle)
mainloop()
