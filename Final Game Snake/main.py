from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import sp
from kivy import properties as kp
from kivy.uix.widget import Widget
from kivy.animation import Animation
from collections import defaultdict
from random import randint
from kivy.uix.boxlayout import BoxLayout

done = False

SPRITE_SIZE = sp(20)
COLS = int(Window.width / SPRITE_SIZE)
ROWS = int(Window.height / SPRITE_SIZE)
Window.size = (800, 660)  # --- Adds space for score display

SNAKE_LENGTH = 4
SNAKE_SPEED = [.1, .05, .025, 100]  # in seconds

difficulty = 0

ALPHA = .5

LEFT = 'left'
UP = 'up'
RIGHT = 'right'
DOWN = 'down'


directional_values = {LEFT: [-1, 0],
                      RIGHT: [1, 0],
                      UP: [0, 1],
                      DOWN: [0, -1]}

directional_keys = {'a': LEFT,
                    'd': RIGHT,
                    'w': UP,
                    's': DOWN}

directional_groups = {LEFT: 'horizontal',
                      UP: 'vertical',
                      RIGHT: 'horizontal',
                      DOWN: 'vertical'}


class Sprite(Widget):
    coord = kp.ListProperty([0, 0])
    bgcolor = kp.ListProperty([0, 0, 0, 0])


SPRITES = defaultdict(lambda: Sprite())

# The Intro This Always crashes for some reason


class Intro(App):
    def on_start(self, *args):
        Intro().stop()

# The Main Game


class Fruit(Sprite):
    pass


class Snake(App):

    sprite_size = kp.NumericProperty(SPRITE_SIZE)

    # Snake Stuff
    head = kp.ListProperty([0, 0])
    snake = kp.ListProperty()
    length = kp.NumericProperty(SNAKE_LENGTH)
    block_input = kp.BooleanProperty(False)
    direction = kp.StringProperty(RIGHT, options=(LEFT,
                                                  RIGHT,
                                                  UP,
                                                  DOWN))

    buffer_direction = kp.StringProperty(RIGHT, options=(LEFT,
                                                         RIGHT,
                                                         UP,
                                                         DOWN,
                                                         ''))

    # Other Stuff
    score = 0
    fruit = kp.ListProperty([0, 0])
    fruit_sprite = kp.ObjectProperty(Fruit)

    alpha = kp.NumericProperty(0)

    def on_start(self):
        self.fruit_sprite = Fruit()
        self.fruit = self.new_fruit_location
        self.head = self.new_head_location
        Clock.schedule_interval(self.move, SNAKE_SPEED[difficulty])
        Window.bind(on_keyboard=self.key_handler)

    def key_handler(self, _, __, ___, key, ____):
        try:
            self.try_change_direction(directional_keys[key])
        except KeyError:
            pass

    def try_change_direction(self, new_direction):
        if directional_groups[new_direction] != directional_groups[self.direction]:
            if self.block_input:
                self.buffer_direction = new_direction
            else:
                self.direction = new_direction
                self.block_input = True

    def on_head(self, *args):
        self.snake = self.snake[-self.length:] + [self.head]

    def on_snake(self, *args):
        for index, coord in enumerate(self.snake):
            sprite = SPRITES[index]
            sprite.coord = coord
            if not sprite.parent:
                self.root.add_widget(sprite)

    def on_fruit(self, *args):
        self.fruit_sprite.coord = self.fruit
        if not self.fruit_sprite.parent:
            self.root.add_widget(self.fruit_sprite)

    @property
    def new_head_location(self):  # starts the snake's location
        return [randint(4, dim-5) for dim in [COLS, ROWS]]

    @property
    def new_fruit_location(self):  # starts the snake's location
        while True:
            fruit = [randint(0, dim-1) for dim in [COLS, ROWS]]
            if fruit not in self.snake and fruit != self.fruit:
                return fruit

    def move(self, *args):
        self.block_input = False
        new_head = [sum(x) for x in zip(self.head, directional_values[self.direction])]
        if not self.check_in_bounds(new_head) or new_head in self.snake:
            return self.die()
        if new_head == self.fruit:
            self.length += 1
            self.fruit = self.new_fruit_location
            self.score += 1
            print(self.score)
        if self.buffer_direction:
            self.try_change_direction(self.buffer_direction)
            self.buffer_direction = ''
        self.head = new_head

    def check_in_bounds(self, pos):
        return all(0 <= pos[x] < dim for x, dim in enumerate([COLS, ROWS]))

    def die(self):
        self.root.clear_widgets()
        self.alpha = ALPHA
        self.fruit = self.new_fruit_location
        Animation(alpha=0, duration=SNAKE_SPEED[difficulty]).start(self)
        self.snake.clear()
        self.length = SNAKE_LENGTH
        self.head = self.new_head_location
        Snake().stop()
    def build(self):
        return SnakeLayout()

class SnakeLayout(BoxLayout):
    pass


if __name__ == '__main__':
    Snake().run()
    done = True
