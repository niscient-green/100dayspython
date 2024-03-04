# Import packages
from turtle import Turtle

# Set globals
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Define the Snake class
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create()
        self.head = self.snake_body[0]

    def create(self):
        # Create snake body - starts at 3 squares at (0, 0)
        for _ in range(3):
            self.new_segment()

    # Move the snake
    def move(self):
        # Move all segments except the head
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            preceding_position = self.snake_body[segment_number - 1].position()
            self.snake_body[segment_number].goto(preceding_position[0], preceding_position[1])

        # Move the head
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def new_segment(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        snake_length = len(self.snake_body)
        if snake_length > 0:
            last_segment = self.snake_body[-1]
            new_segment_xcor = last_segment.xcor() - 20
            new_segment_ycor = last_segment.ycor()
            new_segment.goto(new_segment_xcor, new_segment_ycor)
        self.snake_body.append(new_segment)

    def is_collided(self):
        for segment in self.snake_body:
            if segment == self.head:
                pass
            elif self.head.distance(segment) < 10:
                return True
        return False
