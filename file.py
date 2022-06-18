import os
import sys
from typing import IO

from vpython import color, vector

from planet import Planet
from resources.config import files


def get_path(file):
    if type(file) is int:
        dirname = os.path.dirname(__file__)
        bracket = ('\\', '/')[sys.platform == 'linux']
        fpath: str = os.path.join(dirname, f'demos{bracket}{files[file]}.txt')
    else:
        fpath = file
    return fpath


def save_as(planets_array: list[Planet], time_scale: int, filename: str):
    file = open(f'./demos/{filename}.txt', 'w')
    save_on_file(planets_array, file, time_scale)


def save_on_file(planets_array: list[Planet], output_file: IO, time_scale: int):
    planet_number = planets_array.__len__()
    output_file.write(f"{planet_number}\n")
    output_file.write(f"{time_scale}\n")
    for planet in planets_array:
        output_file.write(f"{planet.mass}\n")
        output_file.write(f"{planet.pos.x}\n")
        output_file.write(f"{planet.pos.y}\n")
        output_file.write(f"{planet.pos.z}\n")
        output_file.write(f"{planet.radius}\n")
        output_file.write(f"{planet.velocity.x}\n")
        output_file.write(f"{planet.velocity.y}\n")
        output_file.write(f"{planet.velocity.z}\n")
        output_file.write(f"{planet.color._x}\n")
        output_file.write(f"{planet.color._y}\n")
        output_file.write(f"{planet.color._z}\n")
        output_file.write(f"{planet.flexibility}\n")
        output_file.write(f"{planet.texture}")
    output_file.close()


def get_relative_path(file_path: str) -> str:
    index = file_path.find('/assets')
    file_path = '.' + file_path[index:]
    return file_path
