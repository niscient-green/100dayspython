# Classes that create and hold cars (move, display, collision detection)

# Import packages
from turtle import Turtle
import config as c
import random


# The collection of cars
class CarManager:
    def __init__(self):
        # Create starting cars
        self.cars = []
        for _ in range(c.CAR_NUM_START):
            self.cars.append(Car())

    # Level up all cars in speed, add more cars
    def level_up(self):
        for _ in range(c.CAR_NUM_INCREMENT):
            self.cars.append(Car())
        for car in self.cars:
            car.car_speed += c.CAR_MOVE_INCREMENT

    # Move all cars forward
    def move_all_cars(self):
        for car in self.cars:
            car.move_car()

    # Check if any of the cars have collided with player
    def check_collision(self, player):
        collision = False
        for car in self.cars:
            if ((car.xcor() - c.CAR_COLLISION_X) < player.xcor() < (car.xcor() + c.CAR_COLLISION_X)) and (
                    (car.ycor() - c.CAR_COLLISION_Y) < player.ycor() < (car.ycor() + c.CAR_COLLISION_Y)):
                collision = True
        return collision

# An individual car
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(c.CAR_COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=c.CAR_WIDTH, stretch_len=c.CAR_HEIGHT)
        self.start_x = c.SCREEN_WIDTH_PAD + random.randint(0, c.SCREEN_WIDTH)
        # Check for car at existing y location, change y if collision
        self.start_y = random.randint(-c.SCREEN_HEIGHT_PAD + 60, c.SCREEN_HEIGHT_PAD - 60)
        self.goto(x=self.start_x, y=self.start_y)
        self.car_speed = c.CAR_MOVE_START
        self.setheading(c.WEST)

    # Move the car forward
    def move_car(self):
        self.clear()
        self.forward(self.car_speed)
        if self.xcor() < -c.SCREEN_WIDTH_PAD:
            self.goto(x=self.start_x, y=self.start_y)
