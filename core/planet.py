from __future__ import annotations
from core.vector import *


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
        self.velocity_arrow = None
        self.acceleration_arrow = None

    def shine(self):
        attach_light(self.render_object,
                     offset=vec(self.render_object.pos.x,
                                self.render_object.pos.y,
                                self.render_object.pos.z),
                     color=color.yellow)

    def render(self):
        self.render_object = sphere(canvas=self.canvas,
                                    radius=self.radius,
                                    pos=self.pos.to_vpython_vector(),
                                    color=self.color,
                                    texture=self.texture,
                                    make_trail=False)
        self.velocity_arrow = arrow(color=color.green)
        self.acceleration_arrow = arrow(color=color.red)
        if self.texture == './assets/textures/sun.jpg':
            self.shine()

    def update_arrows_data(self, time_scale):
        self.velocity_arrow.pos = (
            self.pos + self.velocity.scale_to(self.radius)).to_vpython_vector()
        self.velocity_arrow.axis = self.velocity.to_vpython_vector() * time_scale * 3
        if self.velocity.length() > 0.2 * self.radius:
            v = 0.2 * self.radius
        else:
            v = 0.1 * self.velocity.length()

        self.velocity_arrow.shaftwidth = v
        self.velocity_arrow.headwidth = 2*v
        self.velocity_arrow.headlength = 3*v

        self.acceleration_arrow.pos = (
            self.pos + self.acceleration.scale_to(self.radius)).to_vpython_vector()
        self.acceleration_arrow.axis = self.acceleration.to_vpython_vector() * \
            time_scale * 3
        if self.acceleration.length() > 0.2 * self.radius:
            v = 0.2 * self.radius
        else:
            v = 0.1 * self.acceleration.length()

        self.acceleration_arrow.shaftwidth = v
        self.acceleration_arrow.headwidth = 2*v
        self.acceleration_arrow.headlength = 3*v

    def render_update(self, dt: float, time_scale) -> None:
        self.render_object.pos = self.pos.to_vpython_vector()
        angle = dt / (self.spin_hours * 3600)
        self.render_object.rotate(axis=vector(0, 0, 1), angle=angle)
        self.update_arrows_data(time_scale)

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
