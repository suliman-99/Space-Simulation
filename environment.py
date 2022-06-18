from __future__ import annotations

from typing import List
from gui.controls import Controls
from planet import *
from physics import *
from file import get_path


class Environment:
    def __init__(self) -> None:
        self.planets_array: List[Planet] = []
        self.time_scale = 1
        self.time_speed = 1
        self.frame_rate = 30
        self.calc_num = 30
        self.canvas = canvas(width=1300, height=550)
        self.is_active = True
        self.has_buttons = False

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
        self.time_scale = int(finput.readline())
        self.set_time_speed(1)
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
            color_x = float(finput.readline())
            color_y = float(finput.readline())
            color_z = float(finput.readline())
            flexibility = float(finput.readline())
            spin_hours = float(finput.readline())
            texture = finput.readline()
            if texture == 'None\n':
                texture = None
            c = color.white
            c.x = color_x
            c.y = color_y
            c.z = color_z
            self.planets_array.append(
                Planet(mass, radius, pos, velocity, c, flexibility, spin_hours, texture, self.canvas))
        finput.close()

    def clear_trails(self):
        for planet in self.planets_array:
            planet.render_object.clear_trail()

    def arrows_stop(self):
        for planet in self.planets_array:
            planet.velocity_arrow.stop()
            planet.acceleration_arrow.stop()

    def arrows_start(self):
        for planet in self.planets_array:
            planet.velocity_arrow.start()
            planet.acceleration_arrow.start()

    def render_delete(self):
        for planet in self.planets_array:
            planet.render_object.visible = False

    def run(self) -> None:
        initilize_textures()
        self.render()
        while self.is_active:
            rate(self.frame_rate)
            dt = self.time_speed / self.frame_rate
            self.take_input()
            for i in range(self.calc_num):
                self.collision()
                self.physics(dt / self.calc_num)
            self.render_update(dt)
        self.is_active = True
        self.render_delete()
        self.clear_trails()
        self.scan_from_file('./demos/current_demo.txt')
        self.run()

    def render(self) -> None:
        if not self.has_buttons:
            control_panel = Controls(self)
            control_panel.render()
            self.has_buttons = True
        for planet in self.planets_array:
            planet.render()

    def render_update(self, dt: float) -> None:
        for planet in self.planets_array:
            planet.render_update(dt)

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
