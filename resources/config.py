import sys


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

MAXIMIZE = ('-topmost', '-zoomed')[sys.platform == 'linux']
FULLSCREEN = '-fullscreen'
COSMOLOGICAL_TIME = 0.3
MAX_SPEED = 20
MIN_SPEED = -2
