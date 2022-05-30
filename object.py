from __future__ import annotations
<<<<<<< HEAD
from pygame import Color
from vpython import *
=======
>>>>>>> 5fefd0f5d70e06ee57809bf4f3fec29e10ee949f
from physics_calculator import *
from vector import *


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector, color: Color, friction: float, flexibility: float, canvas: canvas) -> Planet:
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.acceleration = Vector(0, 0, 0)
        self.force = Vector(0, 0, 0)
        self.color = color
        self.friction = friction
        self.flexibility = flexibility
        self.canvas = canvas

    @staticmethod
    def small_builder(mass: float, radius: float, pos: Vector, velocity: Vector, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color.white, 0.1, 0.2, canvas)

    @staticmethod
    def complete_builder(mass: float, radius: float, pos: Vector, velocity: Vector, color: Color, friction: float, flexibility: float, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color, friction, flexibility, canvas)

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius, color=self.color, make_trail=True)

    def render_update(self) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()

    def reset_force(self) -> None:
        self.force = Vector(0, 0, 0)

    def add_force(self, force: Vector) -> None:
        self.force += force

    def update(self, dt: float) -> None:
        self.update_pos(dt)
        self.update_velocity(dt)
        self.update_acceleration()

    def update_pos(self, dt: float) -> None:
        self.pos = calc_pos(
            self.pos, self.velocity, self.acceleration, dt)

    def update_velocity(self, dt: float) -> None:
        self.velocity = calc_velocity(self.velocity, self.acceleration, dt)

    def update_acceleration(self) -> None:
        self.acceleration = calc_acceleration(self.mass, self.force)

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
