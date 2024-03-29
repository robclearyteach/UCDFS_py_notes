import turtle

# Draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Write a text at the specified location (x, y)
def writeText(s, x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.write(s) # Write a string

# Draw a point at the specified location (x, y)
def drawPoint(x, y): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y)
    turtle.pendown() # Pull the pen down
    turtle.begin_fill() # Begin to fill color in a shape
    turtle.circle(3) 
    turtle.end_fill() # Fill the shape

# Draw a circle at centered at (x, y) with the specified radius
def drawCircle(x, y, radius): 
    turtle.penup() # Pull the pen up
    turtle.goto(x, y - radius)
    turtle.pendown() # Pull the pen down
    turtle.circle(radius) 
    
# Draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x, y, width, height): 
    turtle.penup() # Pull the pen up
    turtle.goto(x + width / 2, y + height / 2)
    turtle.pendown() # Pull the pen down
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)
    turtle.right(90)
    turtle.forward(height)
    turtle.right(90)
    turtle.forward(width)



# from UsefulTurtleFunctions import *               #If storing above in a module

# Draw a line from (-50, -50) to (50, 50)
drawLine(-50, -50, 50, 50)

# Write a text at (-50, -60)
writeText("Testing useful Turtle functions", -50, -60)

# Draw a point at (0, 0)
drawPoint(0, 0)

# Draw a circle at (0, 0) with radius 80
drawCircle(0, 0, 80)
    
# Draw a rectangle at (0, 0) with width 60 and height 40
drawRectangle(0, 0, 60, 40)

turtle.hideturtle()
turtle.done() 
