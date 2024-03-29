from __future__ import annotations
from typing import List
from resources.sound import *
from gui.controls import Controls
from core.physics import *
from core.file import *
import core.camera as cam


class Environment:
    def __init__(self) -> None:
        self.planets_array: List[Planet] = []
        self.time_speed = 1
        self.time_scale = 1
        self.frame_rate = 30
        self.calc_num = 30
        self.canvas = canvas(width=1300, height=550)
        self.camera = cam.Camera(self.canvas, self.planets_array)
        self.control = Controls(self.canvas)
        self.first_render = True
        self.have_to_refresh = False

    def set_trail_state(self, value) -> None:
        for planet in self.planets_array:
            planet.render_object.make_trail = value

    def set_velocity_arrows_state(self, value) -> None:
        for planet in self.planets_array:
            planet.velocity_arrow.visible = value

    def set_acceleration_arrows_state(self, value) -> None:
        for planet in self.planets_array:
            planet.acceleration_arrow.visible = value

    def clear_trails(self):
        for planet in self.planets_array:
            planet.render_object.clear_trail()

    def clear_render(self):
        self.clear_trails()
        self.set_velocity_arrows_state(False)
        self.set_acceleration_arrows_state(False)
        for planet in self.planets_array:
            planet.render_object.visible = False

    def refresh(self):
        self.have_to_refresh = False
        self.clear_render()
        scan_from_file(self,'./demos/current_demo.txt')
        self.run()

    def run(self) -> None:
        initilize_textures()
        self.render()
        while not self.have_to_refresh:
            rate(self.frame_rate)
            dt = self.time_speed * self.time_scale / self.frame_rate
            for _ in range(self.calc_num):
                self.collision()
                self.physics(dt / self.calc_num)
            self.take_input()
            self.render_update(dt)
        self.refresh()

    def render(self) -> None:
        if self.first_render:
            self.control.render()
            self.first_render = False
        for planet in self.planets_array:
            planet.render()

    def render_update(self, dt: float) -> None:
        for planet in self.planets_array:
            planet.render_update(dt, self.time_scale)
        self.camera.update()

    def take_input(self) -> None:
        control = self.control
        if control.have_to_refresh:
            self.have_to_refresh = True
            control.have_to_refresh = False
        if control.have_to_save_state:
            save_as(self, 'saved_state')
            control.have_to_save_state = False
        if control.is_paused:
            self.time_speed = 0
        else:
            self.time_speed = control.slider_value
        if control.have_to_clear_trails:
            self.clear_trails()
            control.have_to_clear_trails = False
        self.set_trail_state(control.show_trail)
        self.set_velocity_arrows_state(control.show_velocity)
        self.set_acceleration_arrows_state(control.show_acceleration)
        if control.have_to_move_right:
            self.camera.move_right()
            control.have_to_move_right = False
        if control.have_to_move_left:
            self.camera.move_left()
            control.have_to_move_left = False
        if control.have_to_back_to_initial_state:
            self.camera.back_to_initial_state()
            control.have_to_back_to_initial_state = False
        if control.have_to_revers_focus_state:
            self.camera.revers_focus_state()
            control.have_to_revers_focus_state = False
        if control.have_to_revers_rotate_state:
            self.camera.revers_rotate_state()
            control.have_to_revers_rotate_state = False
        if control.have_to_mute:
            mute()
            control.have_to_mute = False

    def collision(self) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                collision(
                    self.planets_array[i], self.planets_array[i + j + 1])

    def physics(self, dt: float) -> None:
        self.reset_forces()
        self.calculate_forces()
        self.apply_forces(dt)

    def reset_forces(self) -> None:
        for planet in self.planets_array:
            planet.reset_forces()

    def calculate_forces(self) -> None:
        for i in range(self.planets_array.__len__() - 1):
            for j in range(self.planets_array.__len__() - i - 1):
                apply_gravity(
                    self.planets_array[i], self.planets_array[i + j + 1])

    def apply_forces(self, dt: float) -> None:
        for planet in self.planets_array:
            planet.update(dt)


def initilize_textures():
    scene.visible = False
    scene.waitfor("textures")
    scene.visible = True
