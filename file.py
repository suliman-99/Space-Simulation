import os
import sys

from resources.config import files


def get_path(file):
    if type(file) is int:
        dirname = os.path.dirname(__file__)
        bracket = ('\\', '/')[sys.platform == 'linux']
        fpath: str = os.path.join(dirname, f'demos{bracket}{files[file]}.txt')
    else:
        fpath = file
    return fpath


def save_on_file(planets_array):
    planet_number = planets_array.__len__()
    dirname = os.path.dirname(__file__)
    bracket = ('\\', '/')[sys.platform == 'linux']
    outputpath: str = os.path.join(dirname, f'demos{bracket}last.txt')
    foutput = open(outputpath, "w")
    foutput.write(f"{planet_number}\n")
    for planet in planets_array:
        foutput.write(f"{planet.mass}\n")
        foutput.write(f"{planet.pos.x}\n")
        foutput.write(f"{planet.pos.y}\n")
        foutput.write(f"{planet.pos.z}\n")
        foutput.write(f"{planet.radius}\n")
        foutput.write(f"{planet.velocity.x}\n")
        foutput.write(f"{planet.velocity.y}\n")
        foutput.write(f"{planet.velocity.z}\n")
    foutput.close()
