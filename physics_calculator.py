from vector import *


g = 6.6743 * (10**-11)


def calc_acceleration(m: float, f: Vector) -> Vector:
    return f/m


def calc_velocity(v: Vector, a: Vector, dt: float) -> Vector:
    return v + a*dt


def calc_pos(pos: Vector, v: Vector, a: Vector, dt: float) -> Vector:
    return pos + (v*dt) + (a*((dt**2)/2))


def calc_momentum(m: float, v: Vector) -> Vector:
    return v*m


def calc_kinetic_energy(m: float, v: Vector) -> float:
    return (v.length()**2)*m/2


def calc_collision_1d_v1(m1: float, m2: float, v1: Vector, v2: Vector, cr: float) -> float:
    return (cr*m2*(v2-v1)+m1*v1+m2*v2)/(m1+m2)


def calc_collision_v1(m1: float, m2: float, pos1: Vector, pos2: Vector, v1: Vector, v2: Vector, cr: float) -> Vector:
    un = (pos1-pos2).norm()
    v1n = v1.projection_on(un)
    v2n = v2.projection_on(un)
    v1n_len = v1n.length()
    v2n_len = v2n.length()
    v1n_len_last = calc_collision_1d_v1(m1, m2, v1n_len, v2n_len, cr)
    v1n_last = un*v1n_len_last
    v1t_last = v1-v1n
    v1_last = v1n_last + v1t_last
    return v1_last


def calc_gravity(m1: float, m2: float, d: float) -> float:
    return g*m1*m2/(d**2)


def calc_gravity_force_on_first_object(m1: float, m2: float, pos1: Vector, pos2: Vector) -> Vector:
    return (pos2-pos1).scale_to(calc_gravity(m1, m2, (pos2-pos1).length()))
