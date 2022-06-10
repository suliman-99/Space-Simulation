from __future__ import annotations

from physics_calculator import *
from testing.debug import debug_mode
from vector import *


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                 friction_coefficient: float, flexibility: float, canvas: canvas) -> None:
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.acceleration = Vector(0, 0, 0)
        self.force = Vector(0, 0, 0)
        self.color = color
        self.friction_coefficient = friction_coefficient
        self.flexibility = flexibility
        self.canvas = canvas
        self.friction_force = Vector(0, 0, 0)

    @staticmethod
    def small_builder(mass: float, radius: float, pos: Vector, velocity: Vector, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color.white, 0.5, 0.2, canvas)

    @staticmethod
    def complete_builder(mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                         friction_coefficient: float, flexibility: float, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color, friction_coefficient, flexibility, canvas)

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius, color=self.color,
                                    make_trail=debug_mode)

    def render_update(self) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()

    def reset_forces(self) -> None:
        self.force = Vector(0, 0, 0)

    def reset_friction_forces(self) -> None:
        self.friction_force = Vector(0, 0, 0)

    def add_force(self, force: Vector) -> None:
        self.force += force

    def add_friction_force(self, friction_force: float) -> None:
        self.friction_force += friction_force

    def update(self, dt: float) -> None:
        self.update_pos(dt)
        self.update_velocity(dt)
        self.update_acceleration()

    def update_pos(self, dt: float) -> None:
        self.pos = calc_pos(self.pos, self.velocity, self.acceleration, dt)

    def update_velocity(self, dt: float) -> None:
        self.velocity = calc_velocity(self.velocity, self.acceleration, dt)

    def update_acceleration(self) -> None:
        self.acceleration = calc_acceleration(
            self.mass, self.force + self.friction_force)

    def set_acceleration(self, acceleration: Vector):
        self.acceleration = acceleration

    def add_acceleration(self, acceleration: Vector):
        self.acceleration += acceleration

    def set_velocity(self, velocity: Vector):
        self.velocity = velocity

    def add_velocity(self, velocity: Vector):
        self.velocity += velocity

    def set_pos(self, pos: Vector):
        self.pos = pos

    def add_pos(self, pos: Vector):
        self.pos += pos
