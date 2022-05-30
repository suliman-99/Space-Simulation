from __future__ import annotations
from typing import List
from vpython import *
from collision import *
from object import *

from physics_calculator import calc_gravity_force_on_first_object
from terminal_scaner import *


class Enviroment:
    def __init__(self) -> Enviroment:
        self.planets_array: List[Planet] = []
        self.time_speed = 4
        self.frame_rate = 60
        self.calc_num = 50
        self.canvas = canvas(width=1350, height=600)

    def can_add_planet_check(self, pos, radius) -> bool:
        for planet in self.planets_array:
            if sphere_with_sphere_overlap_check(pos, planet.pos, radius, planet.radius) < 0:
                return False
        return True

    def scan(self) -> None:
        planet_number = scanInt(1, 10, 'Planet Number : ')
        for i in range(planet_number):
            print(f'Planet ( {i+1} ) : ')
            mass = scanFloat(
                0, 1000000000000000000, 'Mass : ')
            while True:
                pos_x = scanFloat(-1000000000000,
                                  1000000000000, 'Pos ( X ) : ')
                pos_y = scanFloat(-1000000000000,
                                  1000000000000, 'Pos ( Y ) : ')
                pos_z = scanFloat(-1000000000000,
                                  1000000000000, 'Pos ( Z ) : ')
                pos = Vector(pos_x, pos_y, pos_z)
                radius = scanFloat(1, 1000000000, 'Radius : ')
                if self.can_add_planet_check(pos, radius) == 1:
                    break
            v_x = scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( X ) : ')
            v_y = scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( Y ) : ')
            v_z = scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( Z ) : ')
            Velocity = Vector(v_x, v_y, v_z)
            self.planets_array.append(
                Planet.small_builder(mass, radius, pos, Velocity, self.canvas))
            print('-----------------------------------------------------------')

    def run(self) -> None:
        self.render()
        while True:
            rate(self.frame_rate)
            dt = self.time_speed / self.frame_rate
            self.take_input()
            self.collision()
            for i in range(self.calc_num):
                self.physics(dt/self.calc_num)
            self.render_update()

    def render(self) -> None:
        for planet in self.planets_array:
            planet.render()
        sphere(canvas=self.canvas, pos=vector(
            0, 0, 0), radius=0.5, color=color.red)

    def render_update(self) -> None:
        for planet in self.planets_array:
            planet.render_update()

    def take_input(self) -> None:
        pass

    def collision(self) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                collision(
                    self.planets_array[i], self.planets_array[i+j+1])

    def physics(self, dt: float) -> None:
        self.physics_reset()
        self.physics_calculate(dt)
        self.physics_apply(dt)

    def physics_reset(self) -> None:
        for planet in self.planets_array:
            planet.reset_force()

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
