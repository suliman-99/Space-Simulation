from __future__ import annotations
from physics_calculator import *
from vector import *


my_canvas = canvas(width=1350, height=600)


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector) -> Planet:
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.acceleration = Vector(0, 0, 0)
        self.force = Vector(0, 0, 0)

    def render(self):
        self.render_object = sphere(canvas=my_canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius)

    def reset_force(self) -> None:
        self.force = Vector(0, 0, 0)

    def add_force(self, force: Vector) -> None:
        self.force += force

    def update(self, dt: float) -> None:
        self.update_pos(dt)
        self.update_velocity(dt)
        self.update_acceleration()

    def render_update(self) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()

    def update_pos(self, dt: float) -> None:
        self.pos = calc_pos(
            self.pos, self.velocity, self.acceleration, dt)

    def update_velocity(self, dt: float) -> None:
        self.velocity = calc_velocity(self.velocity, self.acceleration, dt)

    def update_acceleration(self) -> None:
        self.acceleration = calc_acceleration(self.mass, self.force)

    def set_velocity_from_collision(self, velocity: Vector):
        self.velocity = velocity

    def set_pos(self, pos: Vector):
        self.pos = pos

    def add_pos(self, pos: Vector):
        # print(self.pos)
        self.pos += pos
        # print(self.pos)
