from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# TODO 2. Move the snake
class Snake:

    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    # Snake initialized with 3 segments
    def create(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        # The 2nd segment goes where the 1st is, the 3rd to the 2nd
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        # The snake is moved up only if it is not moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # The snake is moved down only if it is not moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        # The snake is moved right only if it is not moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        # The snake is moved left only if it is not moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


