import os
import sys
from typing import IO
from vpython import color , vector
from planet import Planet
from resources.config import files
from vector import Vector


def get_path(file):
    if type(file) is int:
        dirname = os.path.dirname(__file__)
        bracket = ('\\', '/')[sys.platform == 'linux']
        fpath: str = os.path.join(dirname, f'demos{bracket}{files[file]}.txt')
    else:
        fpath = file
    return fpath

def scan_from_file(environment, file) -> None:
    environment.planets_array.clear()
    inputpath = get_path(file)
    finput = open(inputpath, "r")
    planet_number = int(finput.readline())
    environment.time_scale = float(finput.readline())
    for i in range(planet_number):
        mass = float(finput.readline())
        pos_x = float(finput.readline())
        pos_y = float(finput.readline())
        pos_z = float(finput.readline())
        pos = Vector(pos_x, pos_y, pos_z)
        radius = float(finput.readline())
        v_x = float(finput.readline())
        v_y = float(finput.readline())
        v_z = float(finput.readline())
        velocity = Vector(v_x, v_y, v_z)
        color_x = float(finput.readline())
        color_y = float(finput.readline())
        color_z = float(finput.readline())
        flexibility = float(finput.readline())
        spin_hours = float(finput.readline())
        texture = finput.readline()
        if texture == 'None\n':
            texture = None
        c = vector(color_x, color_y, color_z)
        environment.planets_array.append(
            Planet(mass, radius, pos, velocity, c, flexibility, spin_hours, texture, environment.canvas))
    finput.close()


def save_as(environment, filename: str):
    file = open(f'./demos/{filename}.txt', 'w')
    save_on_file(environment, file)


def save_on_file(environment, output_file: IO) -> None:
    planet_number = environment.planets_array.__len__()
    output_file.write(f"{planet_number}\n")
    output_file.write(f"{environment.time_scale}\n")
    for planet in environment.planets_array:
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
        output_file.write(f"{planet.spin_hours}\n")
        output_file.write(f"{planet.texture}")
    output_file.close()


def get_relative_path(file_path: str) -> str:
    index = file_path.find('/assets')
    file_path = '.' + file_path[index:]
    return file_path
