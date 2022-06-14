from __future__ import annotations

from typing import List
from collision import *
from gui.controls import Controls
from object import *
from physics_calculator import *
from file import get_path
from terminal_scaner import *

from resources.config import COSMOLOGICAL_TIME


class Environment:
    def __init__(self) -> None:
        self.planets_array: List[Planet] = []
        self.time_speed = COSMOLOGICAL_TIME
        self.frame_rate = 30
        self.calc_num = 30
        self.canvas = canvas(width=1350, height=600)

    def change_time_flow(self, value) -> None:
        self.time_speed = value * COSMOLOGICAL_TIME

    def can_add_planet_check(self, pos, radius) -> bool:
        for planet in self.planets_array:
            if sphere_with_sphere_overlap_check(pos, planet.pos, radius, planet.radius) < 0:
                return False
        return True

    def scan_from_file(self, file) -> None:
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
                Planet.small_builder(mass, radius, pos, velocity, self.canvas))
        finput.close()

    def clear_data(self) -> None:
        self.planets_array.clear()

    def add_planet(self, mass, radius, pos, velocity) -> None:
        self.planets_array.append(Planet.small_builder(mass, radius, pos, velocity, self.canvas))

    def add_planets(self, planets) -> None:
        self.planets_array.extend(planets)

    def scan(self) -> None:
        planet_number = scan_int(1, 10, 'Planet Number : ')
        for i in range(planet_number):
            print(f'Planet ( {i + 1} ) : ')
            mass = scan_float(
                0, 1000000000000000000, 'Mass : ')
            while True:
                pos_x = scan_float(-1000000000000,
                                   1000000000000, 'Pos ( X ) : ')
                pos_y = scan_float(-1000000000000,
                                   1000000000000, 'Pos ( Y ) : ')
                pos_z = scan_float(-1000000000000,
                                   1000000000000, 'Pos ( Z ) : ')
                pos = Vector(pos_x, pos_y, pos_z)
                radius = scan_float(1, 1000000000, 'Radius : ')
                if self.can_add_planet_check(pos, radius) == 1:
                    break
            v_x = scan_float(
                -1000000000000, 1000000000000, 'Velocity ( X ) : ')
            v_y = scan_float(
                -1000000000000, 1000000000000, 'Velocity ( Y ) : ')
            v_z = scan_float(
                -1000000000000, 1000000000000, 'Velocity ( Z ) : ')
            velocity = Vector(v_x, v_y, v_z)
            self.planets_array.append(
                Planet.small_builder(mass, radius, pos, velocity, self.canvas))
            print('-----------------------------------------------------------')

    def run(self) -> None:
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
        sphere(canvas=self.canvas, pos=vector(
            0, 0, 0), radius=0.5, color=color.red)
        control_panel = Controls(self)
        control_panel.render()

    def render_update(self) -> None:
        for planet in self.planets_array:
            planet.render_update()

    def take_input(self) -> None:
        pass

    def collision(self) -> None:
        for planet in self.planets_array:
            planet.reset_friction_forces()
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
        for planet in self.planets_array:
            for other in self.planets_array:
                if planet == other:
                    continue
                planet.add_force(
                    calc_gravity_force_on_first_object(planet.mass, other.mass, planet.pos, other.pos))

    def physics_apply(self, dt: float) -> None:
        for planet in self.planets_array:
            planet.update(dt)
