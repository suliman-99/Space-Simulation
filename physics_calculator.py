# from Errors import *


def calc_acceleration(mass, force):
    # if mass <= 0:
    #     return div_on_zero
    return force/mass


def calc_velocity(velocity, acceleration, dt):
    return velocity + acceleration*dt


def calc_pos(pos, velocity, acceleration, dt):
    return pos + (velocity*dt) + (acceleration**2)*dt/2


def calc_momentum(mass, velocity):
    return velocity*mass


def calc_kinetic_energy(mass, velocity):
    return (velocity**2)*mass/2






