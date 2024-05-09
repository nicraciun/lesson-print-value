import turtle
t = turtle.Turtle()

colors = {'red', 'blue', 'green', 'black'}

def drawSquare(t,x,y,size,fill_color):

    t.penup() # Pickup turtle
    t.goto(x,y) # Move Turtle
    t.pendown() # Drop turtle
    t.fillcolor(fill_color)
    t.begin_fill()  # Shape Fill begin
    for square in range(0,4):
        t.forward(size) # move forward
        t.right(90) # turn 90 degrees
    t.end_fill() # Shape Fill End

def drawBoard():

    square_color = turtle.textinput("Color Selection", "Enter a color:") # Set color to be user defined
    square_color = 'white' if square_color == 'black' else square_color # Changed here
    pos_x = turtle.numinput("Position Selection", "Enter a Position for X") # Set position x to be user defined
    pos_y = turtle.numinput("Position Selection", "Enter a Position for Y") # Set position y to be user defined
    box_size = turtle.numinput("Box Size Selection", "Enter a Box Size (1-50)") # Set box size to be user defined
    for squareOne in range(0,8): # Create a chess board dimension
        for squareTwo in range(0,8):
            drawSquare(t,pos_x+squareTwo*box_size,pos_y+squareOne*box_size,box_size,square_color if (squareTwo+squareOne)%2 == 0 else 'black') # Changed Here

drawBoard() # Call drawBoard Function

turtle.done()