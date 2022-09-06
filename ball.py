from turtle import Turtle

# ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
       #move around the screen
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
    # bounce of the the y axis and switch the direction
    def bounce_y(self):
        self.y_move *= -1
    # if bounced of the paddles then increase the ball speed and change the direction
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
    #reset the position  of the ball and make it change directions when scoring.
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

