from IPython.display import SVG
import random


class Painting:
    DIRECTIONS = ["right", "down", "left", "up"]
    COL_WIDHT = 40
    MAIN_TEMPLATE = '''
    <svg width="{width:d}" height="{height:d}">
        <style>
            svg{{
                font-color:black;
                font-size:20;
                background-image: url(painting.png);
                background-repeat: no-repeat;
                background-size: {width:d}px {height:d}px;
            }}
            rect{{
                fill:transparent;
                stroke: black;
            }}
            rect.painted{{
                fill:red;
                stroke:purple;
            }}
            text.number{{
                fill:red;
                font-size: 16;
            }}
        </style>
        {content}
    </svg>
    '''
    SQUARE_TEMPLATE = '<rect x="{x}" y="{y}" width="40" height="40" class="{kind}"/>'

    def __init__(self):
        self.size = random.randrange(5, 20, 2)
        self.row_position = 0
        self.column_position = 0
        self.direction = "right"
        self.painted_squares = []

    def _create_svg(self):
        result = []
        for row in range(self.size):
            for column in range(self.size):
                result += [self.SQUARE_TEMPLATE.format(x=column * self.COL_WIDHT, y=row * self.COL_WIDHT,
                                                       kind="painted" if (row, column) in self.painted_squares else '')]

        return self.MAIN_TEMPLATE.format(width=self.size * self.COL_WIDHT, height=self.size * self.COL_WIDHT,
                                         content="\n".join(result))

    def view(self):
        return SVG(self._create_svg())

    def paint(self):
        self.painted_squares.append((self.row_position, self.column_position))

    def turn_left(self):
        index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[index - 1]

    def turn_right(self):
        index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(index + 1) % 4]

    def move_forward(self, n=1):
        for _ in range(n):
            if self.direction == 'up':
                self.row_position -= 1
            if self.direction == 'down':
                self.row_position += 1
            if self.direction == 'left':
                self.column_position -= 1
            if self.direction == 'right':
                self.column_position += 1
