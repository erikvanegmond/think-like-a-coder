from IPython.display import SVG
import random


class Painting:
    directions = ["right", "down", "left", "up"]
    CWIDTH = 40
    main_template = '''
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
    square_template = '<rect x="{x}" y="{y}" width="40" height="40" class="{kind}"/>'

    def __init__(self):
        self.size = random.randrange(5, 20, 2)
        self.r_pos = 0
        self.c_pos = 0
        self.direction = "right"
        self.painted_squares = []

    def _create_svg(self):
        result = []
        for r in range(self.size):
            for c in range(self.size):
                result += [self.square_template.format(x=c * self.CWIDTH, y=r * self.CWIDTH,
                                                       kind="painted" if (r, c) in self.painted_squares else '')]

        return self.main_template.format(width=self.size * self.CWIDTH, height=self.size * self.CWIDTH,
                                         content="\n".join(result))

    def view(self):
        return SVG(self._create_svg())

    def paint(self):
        self.painted_squares.append((self.r_pos, self.c_pos))

    def turn_left(self):
        index = self.directions.index(self.direction)
        self.direction = self.directions[index - 1]

    def turn_right(self):
        index = self.directions.index(self.direction)
        self.direction = self.directions[(index + 1) % 4]

    def move_forward(self):
        if self.direction == 'up':
            self.r_pos -= 1
        if self.direction == 'down':
            self.r_pos += 1
        if self.direction == 'left':
            self.c_pos -= 1
        if self.direction == 'right':
            self.c_pos += 1
