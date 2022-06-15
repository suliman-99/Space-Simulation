from __future__ import annotations

from physics_calculator import *
from resources.config import TRAIL_MODE
from vector import *


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                 friction_coefficient: float, flexibility: float, canvas: canvas, texture: string = 'sun') -> None:
        self.render_object = None
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
        self.texture = texture

    @staticmethod
    def small_builder(mass: float, radius: float, pos: Vector, velocity: Vector, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color.white, 0.5, 0.2, canvas)

    @staticmethod
    def complete_builder(mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                         friction_coefficient: float, flexibility: float, texture: str, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color, friction_coefficient, flexibility, canvas, texture)

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius, color=self.color,
                                    texture=f'assets/textures/{self.texture}.jpg',
                                    make_trail=TRAIL_MODE,
                                    velocity=self.velocity.to_vpython_vector()
                                    )
        if self.texture == 'sun':
            self.shine()

    def add_points_trail(self, freq=3):
        attach_trail(self.render_object, type='points', radius=0.03, pps=freq)

    def add_arrow(self, atterbute):
        attach_arrow(self.render_object, atterbute, scale=3,
                     shaftwidth=0.1, pos=self.render_object.pos)

    def shine(self):
        attach_light(self.render_object,
                     offset=vec(self.render_object.pos.x, self.render_object.pos.y, self.render_object.pos.z),
                     color=color.yellow)

    def render_update(self) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()
        # self.render_object.make_trail = TRAIL_MODE
        # self.add_arrow('velocity')

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
