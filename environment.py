from __future__ import annotations

from typing import List
from gui.controls import Controls
from planet import *
from physics import *
from file import get_path


class Environment:
    def __init__(self) -> None:
        self.planets_array: List[Planet] = []
        self.time_scale = 86400
        self.time_speed = self.time_scale 
        self.frame_rate = 30
        self.calc_num = 30
        self.canvas = canvas(width=1300, height=550)

    def set_time_speed(self, value) -> None:
        self.time_speed = value * self.time_scale 

    def set_trail_state(self, value) -> None:
        for planet in self.planets_array:
            planet.set_trail_state(value)

    def can_add_planet(self, pos: Vector, radius: float) -> bool:
        for planet in self.planets_array:
            if (planet.pos - pos).length() < planet.radius + radius:
                return False
        return True

    def scan_from_file(self, file) -> None:
        self.planets_array.clear()
        inputpath = get_path(file)
        finput = open(inputpath, "r")
        planet_number = int(finput.readline())
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
            self.planets_array.append(
                Planet(mass, radius, pos, velocity, color.white, 0.2, 'sun', self.canvas))
        finput.close()

    def run(self) -> None:
        initilize_textures()
        self.render()
        while True:
            rate(self.frame_rate)
            dt = self.time_speed / self.frame_rate
            self.take_input()
            for i in range(self.calc_num):
                self.collision()
                self.physics(dt / self.calc_num)
            self.render_update()

    def render(self) -> None:
        for planet in self.planets_array:
            planet.render()
        control_panel = Controls(self)
        control_panel.render()

    def render_update(self) -> None:
        for planet in self.planets_array:
            planet.render_update()

    def take_input(self) -> None:
        pass

    def collision(self) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                collision(
                    self.planets_array[i], self.planets_array[i + j + 1])

    def physics(self, dt: float) -> None:
        self.physics_reset()
        self.physics_calculate(dt)
        self.physics_apply(dt)

    def physics_reset(self) -> None:
        for planet in self.planets_array:
            planet.reset_forces()

    def physics_calculate(self, dt: float) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                apply_gravity(
                    self.planets_array[i], self.planets_array[i + j + 1])

    def physics_apply(self, dt: float) -> None:
        for planet in self.planets_array:
            planet.update(dt)


def initilize_textures():
    scene.visible = False
    scene.waitfor("textures")
    scene.visible = True
