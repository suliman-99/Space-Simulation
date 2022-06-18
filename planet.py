from __future__ import annotations
from vector import *


class Planet:

    def __init__(self, mass: float, radius: float, pos: Vector, velocity: Vector, color: color,
                 flexibility: float, spin_hours: float, texture: string, canvas: canvas) -> None:
        self.render_object = None
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
        self.spin_hours = spin_hours

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    pos=self.pos.to_vpython_vector(), radius=self.radius, color=self.color,
                                    texture=self.texture,
                                    make_trail=False,
                                    velocity=self.velocity.to_vpython_vector(),
                                    acceleration=self.acceleration.to_vpython_vector()
                                    )
        self.velocity_arrow = self.add_arrow('velocity', color.green)
        self.acceleration_arrow = self.add_arrow('acceleration', color.red)
        if self.texture == './assets/textures/sun.jpg':
            self.shine()

    def add_arrow(self, atterbute, color):
        return attach_arrow(self.render_object, atterbute, scale=1,
                            shaftwidth=0.2*self.radius, pos=self.render_object.pos, color=color)

    def update_arrows_data(self):
        v = self.velocity
        v = v.scale_to(2*self.radius + v.length())
        self.render_object.velocity = v.to_vpython_vector()

        a = self.force / self.mass
        a = a.scale_to(2*self.radius + a.length())
        self.render_object.acceleration = a.to_vpython_vector()

    def shine(self):
        attach_light(self.render_object,
                     offset=vec(self.render_object.pos.x,
                                self.render_object.pos.y, self.render_object.pos.z),
                     color=color.yellow)

    def render_update(self, dt: float) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()
        angle = dt / (self.spin_hours * 3600)
        self.render_object.rotate(axis=vector(0, 0, 1), angle=angle)
        self.update_arrows_data()

    def set_trail_state(self, value) -> None:
        self.render_object.make_trail = value

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
