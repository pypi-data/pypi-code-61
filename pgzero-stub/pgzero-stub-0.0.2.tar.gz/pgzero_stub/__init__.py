from pgzero import music
from pgzero import screen as pgzero_screen
from pgzero.actor import Actor
from pgzero.clock import clock
from pygame import display
from pgzero.rect import ZRect as rect

WIDTH = 800
HEIGHT = 600

screen = pgzero_screen.Screen(display.set_mode((WIDTH, HEIGHT), 0))


class Keyboard():
    def __init__(self, *args, **kwargs):
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.space = False


keyboard = Keyboard()
__all__ = [
    'Actor',
    'clock',
    'keyboard',
    'music',
    'screen',
    'WIDTH',
    'HEIGHT',
    'rect',
]

__version__ = '0.0.2'
