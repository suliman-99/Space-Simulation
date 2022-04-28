from __future__ import annotations
from math import *
from numpy import *


class Vector:

    def __init__(self, x, y, z,):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'[{self.x} , {self.y} , {self.z}]'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other):
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other, self.z*other)

    def __truediv__(self, other):
        return Vector(self.x/other, self.y/other, self.z/other)

    def dot(self, other: Vector) -> float:
        return self.x*other.x+self.y*other.y+self.z*other.z

    def cross(self, other: Vector) -> Vector:
        return Vector(self.y*other.z-self.z*other.y, self.z*other.x-self.x*other.z, self.x*other.y-self.y*other.x)

    def length(self) -> float:
        return sqrt(self.x**2+self.y**2+self.z**2)

    def scale_to(self, new_length: float) -> Vector:
        var = new_length/self.length()
        return Vector(self.x*var, self.y*var, self.z*var)

    def norm(self) -> Vector:
        return self.scale_to(1)

    def is_normed(self) -> bool:
        return self.length() == 1

    def projection_on(self, other: Vector) -> Vector:
        return other*(other.dot(self)/other.length()**2)

    def projection_length_on(self, other: Vector) -> float:
        return other.dot(self)/other.length()
