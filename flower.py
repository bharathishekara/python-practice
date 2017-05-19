import turtle

def draw_triangle(some_turtle):
    for i in range(1,3):
        some_turtle.forward(100)
        some_turtle.left(123)
        some_turtle.forward(100)
        
        
def draw_art():

    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue")
    brad.speed(2)
    draw_triangle(brad)
##    for i in range(1,37):
##        draw_triangle(brad)
##        brad.right(10)

    
    


    window.exitonclick()
    
draw_art()












