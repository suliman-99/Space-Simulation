import os
import sys
from typing import IO

from resources.config import files


def get_path(file):
    if type(file) is int:
        dirname = os.path.dirname(__file__)
        bracket = ('\\', '/')[sys.platform == 'linux']
        fpath: str = os.path.join(dirname, f'demos{bracket}{files[file]}.txt')
    else:
        fpath = file
    return fpath


def save_on_file(planets_array, output_file: IO):
    planet_number = planets_array.__len__()
    output_file.write(f"{planet_number}\n")
    for planet in planets_array:
        output_file.write(f"{planet.mass}\n")
        output_file.write(f"{planet.pos.x}\n")
        output_file.write(f"{planet.pos.y}\n")
        output_file.write(f"{planet.pos.z}\n")
        output_file.write(f"{planet.radius}\n")
        output_file.write(f"{planet.velocity.x}\n")
        output_file.write(f"{planet.velocity.y}\n")
        output_file.write(f"{planet.velocity.z}\n")
    output_file.close()
