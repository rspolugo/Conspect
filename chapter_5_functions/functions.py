import turtle

TOP_X=0
TOP_Y=100
BASE_LEFT_X = -100
BASE_LEFT_Y = -100
BASE_RIGHT_X = 100
BASE_RIGHT_Y = -100

def main():
    turtle.hideturtle()
    line(TOP_X, TOP_Y, BASE_LEFT_X, BASE_LEFT_Y, 'red')
    line(TOP_X, TOP_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'blue')
    line(BASE_LEFT_X, BASE_LEFT_Y, BASE_RIGHT_X, BASE_RIGHT_Y, 'green')
def line(startX, startY, endX, endY, color):
    turtle.penup()
    turtle.goto(startX,startY)
    turtle.pendown()
    turtle.pencolor(color)
    turtle.goto(endX,endY)
main()