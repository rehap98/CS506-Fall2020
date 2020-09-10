import turtle

# There were probably easier museums to draw, but I've always wanted to visit the
# Louvre so our city should have it!

def draw_museum():
    s = turtle.Screen()
    drawing = turtle.Turtle()
    draw_main(drawing)
    draw_door(drawing)
    draw_triangle(drawing)

def draw_triangle(drawing):
    drawing.penup()
    drawing.right(80)
    drawing.forward(30)
    drawing.right(100)
    drawing.pendown()
    drawing.fillcolor("#808080")
    drawing.begin_fill()
    drawing.forward(120)
    drawing.right(120)
    drawing.forward(120)
    drawing.right(120)
    drawing.forward(120)
    drawing.end_fill()

def draw_main(drawing):
    drawing.fillcolor("#b38d59")
    drawing.begin_fill()
    drawing.forward(270)
    drawing.left(90)
    drawing.forward(180)
    drawing.left(90)
    drawing.forward(230)
    drawing.right(90)
    drawing.forward(50)
    drawing.left(90)
    drawing.forward(80)
    drawing.left(90)
    drawing.forward(50)
    drawing.right(90)
    drawing.forward(230)
    drawing.left(90)
    drawing.forward(180)
    drawing.left(90)
    drawing.forward(270)
    drawing.end_fill()

def draw_door(drawing):
    drawing.fillcolor("#714e1b")
    drawing.left(90)
    drawing.forward(35)
    drawing.right(90)
    drawing.forward(20)
    drawing.right(90)
    drawing.forward(35)
    drawing.left(90)

