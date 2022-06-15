from __future__ import annotations

from vector import *


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                 flexibility: float, canvas: canvas, texture: string = 'sun') -> None:
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.velocity = velocity
        self.acceleration = Vector(0, 0, 0)
        self.force = Vector(0, 0, 0)
        self.color = color
        self.flexibility = flexibility
        self.canvas = canvas
        self.texture = texture

    @staticmethod
    def small_builder(mass: float, radius: float, pos: Vector, velocity: Vector, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color.white,0.2, canvas)

    @staticmethod
    def complete_builder(mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                         flexibility: float, texture: str, canvas: canvas) -> Planet:
        return Planet(mass, radius, pos, velocity, color, flexibility, canvas, texture)

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius, color=self.color,
                                    make_trail=False,
                                    texture=f'assets/textures/{self.texture}.jpg',
                                    velocity=self.velocity.to_vpython_vector()
                                    )
        if self.texture == 'sun':
            self.shine()
        # self.add_arrow('velocity')

    def add_arrow(self, atterbute):
        attach_arrow(self.render_object, atterbute, scale=3,
                     shaftwidth=0.1, pos=self.render_object.pos)

    def shine(self):
        attach_light(self.render_object,
                     offset=vec(self.render_object.pos.x,
                                self.render_object.pos.y, self.render_object.pos.z),
                     color=color.yellow)

    def render_update(self) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()

    def reset_forces(self) -> None:
        self.force = Vector(0, 0, 0)

    def add_force(self, force: Vector) -> None:
        self.force += force

    def update(self, dt: float) -> None:
        self.pos += (self.velocity * dt) + \
            (self.acceleration * ((dt ** 2) / 2))
        self.velocity += self.acceleration * dt
        self.acceleration = self.force / self.mass

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
