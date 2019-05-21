from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import sp
from kivy import properties as kp
from kivy.uix.widget import Widget
from kivy.animation import Animation
from collections import defaultdict

SPRITE_SIZE = sp(20)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)

SNAKE_LENGTH = 4
SNAKE_SPEED = .1 #in seconds

ALPHA = .5

LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DOWN = 'down'

directional_values = {LEFT: [-1, 0],
                      RIGHT: [1, 0],
                      UP: [0, 1],
                      DOWN: [0, -1]}


class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])


SPRITES = defaultdict(lambda: Sprite())


class Snake(App):
    sprite_size = kp.NumericProperty(SPRITE_SIZE)

    # Snake Stuff
    head = kp.ListProperty([0, 0])
    snake = kp.ListProperty()
    length = kp.NumericProperty(SNAKE_LENGTH)
    direction = kp.StringProperty(RIGHT, options=(LEFT,
                                                  RIGHT,
                                                  UP,
                                                  DOWN))

    apple = kp.ListProperty([0, 0])

    alpha = kp.NumericProperty(0)

    def on_start(self):
        Clock.schedule_interval(self.move, SNAKE_SPEED)

    def on_head(self, *args):
        self.snake = self.snake[-self.length:] + [self.head]

    def on_snake(self, *args):
        for index, coord in enumerate(self.snake):
            sprite = SPRITES[index]
            sprite.coord = coord
            if not sprite.parent:
                self.root.add_widget(sprite)

    def move(self, *args):
        new_head = [sum(x) for x in zip(self.head, directional_values[self.direction])]
        if not self.check_in_bounds(new_head):
            return self.die()
        self.head = new_head

    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))

    def die(self):
        self.alpha = ALPHA
        Animation(alpha=0, duration=SNAKE_SPEED).start(self)

if __name__ == '__main__':
    Snake().run()
