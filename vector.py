from __future__ import annotations
from math import *
import string
from numpy import *
from vpython import *


class Vector:

    def __init__(self, x, y, z,) -> Vector:
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> string:
        return f'[{self.x} , {self.y} , {self.z}]'

    def __pos__(self) -> Vector:
        return Vector(+self.x, +self.y, +self.z)

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: Vector) -> bool:
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __iadd__(self, other: Vector) -> Vector:
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __isub__(self, other: Vector) -> Vector:
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other: float) -> Vector:
        return Vector(self.x*other, self.y*other, self.z*other)

    def __rmul__(self, other: float) -> Vector:
        return Vector(self.x*other, self.y*other, self.z*other)

    def __imul__(self, other: float) -> Vector:
        return Vector(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other: float) -> Vector:
        return Vector(self.x/other, self.y/other, self.z/other)

    def __rtruediv__(self, other: float) -> Vector:
        return Vector(self.x/other, self.y/other, self.z/other)

    def __itruediv__(self, other: float) -> Vector:
        return Vector(self.x/other, self.y/other, self.z/other)

    def dot(self, other: Vector) -> float:
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self, other: Vector) -> Vector:
        return Vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)

    def length(self) -> float:
        return sqrt(self.x**2+self.y**2+self.z**2)

    def scale_to(self, new_length: float) -> Vector:
        if self.length() == 0:
            return Vector(0, 0, 0)
        var = new_length/self.length()
        return Vector(self.x*var, self.y*var, self.z*var)

    def norm(self) -> Vector:
        return self.scale_to(1)

    def is_normed(self) -> bool:
        return self.length() == 1

    def projection_on(self, other: Vector) -> Vector:
        if other.length() == 0:
            return Vector(0, 0, 0)
        return other*(other.dot(self)/other.length()**2)

    def projection_length_on(self, other: Vector) -> float:
        if other.length() == 0:
            return Vector(0, 0, 0)
        return other.dot(self)/other.length()

    def to_vpython_vector(self) -> vector:
        return vector(self.x, self.y, self.z)
