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
    return ((cr*m2*(v2-v1))+(m1*v1)+(m2*v2))/(m1+m2)


def calc_collision(m1: float, m2: float, pos1: Vector, pos2: Vector, v1: Vector, v2: Vector, cr: float) -> tuple[Vector, Vector]:
    un = (pos2-pos1).norm()
    v1n_len = v1.dot(un)
    v2n_len = v2.dot(un)
    if v1n_len < v2n_len:
        return v1, v2
    v1n_len_last = calc_collision_1d_v1(m1, m2, v1n_len, v2n_len, cr)
    v2n_len_last = calc_collision_1d_v1(m2, m1, v2n_len, v1n_len, cr)
    v1n_last = un*v1n_len_last
    v2n_last = un*v2n_len_last
    v1t_last = v1-v1.projection_on(un)
    v2t_last = v2-v2.projection_on(un)
    v1_last = v1n_last + v1t_last
    v2_last = v2n_last + v2t_last
    return v1_last, v2_last


def calc_gravity(m1: float, m2: float, d: float) -> float:
    return g*m1*m2/(d**2)


def calc_gravity_force_on_first_object(m1: float, m2: float, pos1: Vector, pos2: Vector) -> Vector:
    return (pos2-pos1).scale_to(calc_gravity(m1, m2, (pos2-pos1).length()))


def calc_friction(pos1: Vector, pos2: Vector, velocity1: Vector, velocity2: Vector, force1: Vector, force2: Vector, friction_coefficient1: float, friction_coefficient2: float) -> tuple[Vector, Vector]:
    un = (pos2 - pos1).norm()
    dv = velocity1 - velocity2
    c = friction_coefficient1*friction_coefficient2
    f1n_length = force1.dot(un)
    f2n_length = force2.dot(un)
    if f1n_length <= f2n_length:
        return Vector(0, 0, 0), Vector(0, 0, 0)
    fn_length = f1n_length - f2n_length
    friction_force_length = c * fn_length
    # if friction_force_length > dv.norm():
    #     return -dv, +dv
    f1 = -friction_force_length*dv.norm()
    f2 = +friction_force_length*dv.norm()
    return f1, f2
