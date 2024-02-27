from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()

        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_fragment = []
        self.hideturtle()

    def create_a_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-230, 280)
            new_car.goto(300, random_y)
            new_car.color(random.choice(COLORS))
            self.car_fragment.append(new_car)

    def move_car(self):
        for car in self.car_fragment:
            car.back(self.car_speed)

    def level_up(self):
        self.car_speed *= MOVE_INCREMENT


