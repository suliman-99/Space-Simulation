from vpython import *
from object import *

# (-1) : overlap - (0) : toutch - (1) : far


class Collision:
    @classmethod
    def sphere_with_sphere_overlap_check(cls, pos1: Vector, pos2: Vector, radius1: float, radius2: float) -> int:
        if (pos1-pos2).length() == (radius1+radius2):
            return 0
        if (pos1-pos2).length() < (radius1+radius2):
            return -1
        return 1
