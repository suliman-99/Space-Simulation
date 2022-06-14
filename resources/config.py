import sys
from itertools import cycle

from vpython import color

files = [
    'Collision 1_1 (Recommended)',
    'Collision 1',
    'Collision 2',
    'Collision 3 (Recommended)',
    'Collision 4',
    'Collision Type Test',
    'Earth_Moon',
    'old',
    'Tow Around Each Other (Not Stable)',
    'Tow Around Each Other (Stable)'
]

object_colors = cycle([
    color.white,
    color.red,
    color.blue,
    color.cyan,
    color.green,
    color.magenta,
    color.orange,
    color.purple,
    color.yellow,
])

button_colors = cycle([
    'white',
    'red',
    'blue',
    'cyan',
    'green',
    'magenta',
    'orange',
    'purple',
    'yellow',
])

MAXIMIZE = ('-topmost', '-zoomed')[sys.platform == 'linux']
FULLSCREEN = '-fullscreen'
MAX_SPEED = 50
MIN_SPEED = -2
FRICTION_COEFFICIENT: float = 0.5
FLEXIBILITY: float = 0.2
