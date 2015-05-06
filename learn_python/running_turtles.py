import turtle

def draw_triangle(some_turtle):
  for i in range(1,4):
     some_turtle.right(60)
     
def draw_art():
     window = turtle.Screen()
     window.bgcolor("blue")
     brad = turtle.Turtle()
     brad.speed(2)
     for i in range(1,37):
        draw_triangle(brad)
        brad.right(10)
     window.exitonclick()

draw_art()
