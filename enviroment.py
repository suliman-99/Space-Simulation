from __future__ import annotations
from typing import List
from vpython import *
from collision import Collision
from object import *

from physics_calculator import calc_gravity_force_on_first_object
from terminal_scaner import terminal_scanner

import os

class Enviroment:
    def __init__(self) -> Enviroment:
        self.planets_array: List[Planet] = []
        self.time_speed = 4
        self.frame_rate = 60
        self.calc_num = 50

    def scan_from_file(self) -> None:
        dirname = os.path.dirname   (__file__)
        inputpath = os.path.join(dirname, 'data\\input.txt')
        input = open(inputpath, "r")
        planet_number = int(input.readline())
        for i in range(planet_number):
            mass = int(input.readline())
            pos_x = int(input.readline())
            pos_y = int(input.readline())
            pos_z = int(input.readline())
            pos = Vector(pos_x, pos_y, pos_z)
            radius = int(input.readline())
            v_x = int(input.readline())
            v_y = int(input.readline())
            v_z = int(input.readline())
            Velocity = Vector(v_x, v_y, v_z)
            self.planets_array.append(Planet(mass, radius, pos, Velocity)) 
        input.close()

    def can_add_planet_check(self, pos, radius) -> bool:
        for planet in self.planets_array:
            if Collision.sphere_with_sphere_overlap_check(pos, planet.pos, radius, planet.radius) < 0:
                return False
        return True

    def scan(self) -> None:
        planet_number = terminal_scanner.scanInt(1, 10, 'Planet Number : ')
        for i in range(planet_number):
            print(f'Planet ( {i+1} ) : ')
            mass = terminal_scanner.scanFloat(
                0, 1000000000000000000, 'Mass : ')
            while True:
                pos_x = terminal_scanner.scanFloat(-1000000000000,
                                                   1000000000000, 'Pos ( X ) : ')
                pos_y = terminal_scanner.scanFloat(-1000000000000,
                                                   1000000000000, 'Pos ( Y ) : ')
                pos_z = terminal_scanner.scanFloat(-1000000000000,
                                                   1000000000000, 'Pos ( Z ) : ')
                pos = Vector(pos_x, pos_y, pos_z)
                radius = terminal_scanner.scanFloat(1, 1000000000, 'Radius : ')
                if self.can_add_planet_check(pos, radius) == 1:
                    break
            v_x = terminal_scanner.scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( X ) : ')
            v_y = terminal_scanner.scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( Y ) : ')
            v_z = terminal_scanner.scanFloat(
                -1000000000000, 1000000000000, 'Velocity ( Z ) : ')
            Velocity = Vector(v_x, v_y, v_z)
            self.planets_array.append(Planet(mass, radius, pos, Velocity))
            print('-----------------------------------------------------------')

    def take_input(self) -> None:
        pass

    def collision(self) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                Collision.proccess_collision(
                    self.planets_array[i], self.planets_array[i+j+1])

    def physics(self, dt: float) -> None:
        self.physics_reset()
        self.physics_calculate(dt)
        self.physics_apply(dt)

    def render(self) -> None:
        for planet in self.planets_array:
            planet.render()
        sphere(canvas=my_canvas, pos=vector(
            0, 0, 0), radius=0.5, color=color.red)

    def render_update(self) -> None:
        for planet in self.planets_array:
            planet.render_update()

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
