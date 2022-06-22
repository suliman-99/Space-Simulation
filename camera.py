from cmath import pi
from math import cos, sin
from vpython import *
from planet import Planet
from typing import List


class Camera:
    def __init__(self, canvas: canvas, planets_array: List[Planet]):
        self.canvas = canvas
        self.planets_array = planets_array
        self.planet = None
        self.idx = 0
        self.is_focused = False
        self.is_rotate = False
        self.rotate_val = 0
        self.have_initial_state = False
        self.default_pos = None
        self.default_axis = None
        self.default_center = None
        self.default_range = None

    def save_initial_state(self):
        self.have_initial_state = True
        self.default_pos = self.canvas.camera.pos
        self.default_axis = self.canvas.camera.axis
        self.default_center = self.canvas.center
        self.default_range = self.canvas.range

    def back_to_initial_state(self):
        if self.have_initial_state:
            self.is_focused = False
            self.canvas.center = self.default_center
            self.canvas.range = self.default_range
            self.canvas.camera.pos = self.default_pos
            self.canvas.camera.axis = self.default_axis

    def update(self):
        if self.is_focused:
            if not self.have_initial_state:
                self.save_initial_state()
            x = sin(self.rotate_val) * self.planet.radius * 10
            z = cos(self.rotate_val) * self.planet.radius * 10
            rotate = vector(x, 0, z)
            if self.is_rotate:
                self.rotate_val = self.rotate_val + pi / 60
            self.canvas.camera.pos = self.planet.pos.to_vpython_vector() + \
                rotate
            self.canvas.camera.axis = -rotate

    def move_right(self):
        self.idx = (self.idx + 1) % len(self.planets_array)
        self.planet = self.planets_array[self.idx]
        self.rotate_val = 0
        self.is_focused = True

    def move_left(self):
        self.idx = (self.idx - 1) % len(self.planets_array)
        self.planet = self.planets_array[self.idx]
        self.rotate_val = 0
        self.is_focused = True

    def revers_focus_state(self):
        self.is_focused = not self.is_focused

    def revers_rotate_state(self):
        self.is_rotate = not self.is_rotate
