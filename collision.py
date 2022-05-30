from os import unlink
from vpython import *
from object import *

# -1 : overlap
# 0 : toutch
# 1 : far


def sphere_with_sphere_overlap_check(pos1: Vector, pos2: Vector, radius1: float, radius2: float) -> int:
    if (pos1-pos2).length() == (radius1+radius2):
        # touch
        return 0
    if (pos1-pos2).length() < (radius1+radius2):
        # Overlap
        return -1
    # Far
    return 1


def collision(planet1: Planet, planet2: Planet) -> None:
    collision_correction(planet1, planet2)
    collision_resolution(planet1, planet2)


def collision_correction(planet1: Planet, planet2: Planet) -> None:
    if sphere_with_sphere_overlap_check(planet1.pos, planet2.pos, planet1.radius, planet2.radius) <= 0:
        un = planet2.pos - planet1.pos
        un_len = un.length()
        correcting = planet1.radius + planet2.radius - un_len
        c1 = ((-correcting*planet2.mass) /
              (planet1.mass+planet2.mass))*un.norm()
        c2 = ((correcting*planet1.mass) /
              (planet1.mass+planet2.mass))*un.norm()
        planet1.add_pos(c1)
        planet2.add_pos(c2)


def collision_resolution(planet1: Planet, planet2: Planet) -> None:
    if sphere_with_sphere_overlap_check(planet1.pos, planet2.pos, planet1.radius, planet2.radius) <= 0:
        v1_new, v2_new = calc_collision(
            planet1.mass, planet2.mass, planet1.pos, planet2.pos, planet1.velocity, planet2.velocity, max(planet1.flexibility*planet2.flexibility))
        planet1.set_velocity(v1_new)
        planet2.set_velocity(v2_new)
