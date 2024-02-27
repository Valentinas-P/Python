import turtle

SNAKE_X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.fragments = []
        self.create_snake()

    def create_snake(self):
        for position in SNAKE_X_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake_fragment = turtle.Turtle("square")
        snake_fragment.color("white")
        snake_fragment.penup()
        snake_fragment.goto(position)
        self.fragments.append(snake_fragment)

    def reset(self):
        for frag in self.fragments:
            frag.goto(1000, 1000)
        self.fragments.clear()
        self.create_snake()

    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.fragments[-1].position())

    def move(self):
        for frag_num in range(len(self.fragments) - 1, 0, -1):
            new_x = self.fragments[frag_num - 1].xcor()
            new_y = self.fragments[frag_num - 1].ycor()
            self.fragments[frag_num].goto(new_x, new_y)
        self.fragments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.fragments[0].heading() != DOWN:
            self.fragments[0].setheading(UP)

    def down(self):
        if self.fragments[0].heading() != UP:
            self.fragments[0].setheading(DOWN)

    def left(self):
        if self.fragments[0].heading() != RIGHT:
            self.fragments[0].setheading(LEFT)

    def right(self):
        if self.fragments[0].heading() != LEFT:
            self.fragments[0].setheading(RIGHT)
