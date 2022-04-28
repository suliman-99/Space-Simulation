# from Errors import *
from vector import *


def calc_a(m, f):
    # if mass <= 0:
    #     return div_on_zero
    return f/m


def calc_v(v, a, dt):
    return v + a*dt


def calc_p(p, v, a, dt):
    return p + (v*dt) + (a*((dt**2)/2))


def calc_momentum(m, v):
    return v*m


def calc_kinetic_energy(m: float, v: Vector):
    return (v.length()**2)*m/2


def calc_collision_1_d_v1(m1: float, m2: float, v1: Vector, v2: Vector, cr: float)


return (cr*m2*(v2-v1)+m1*v1+m2*v2)/(m1+m2)


def calc_collision_v1(m1: float, m2: float, p1: Vector, p2: Vector, v1: Vector, v2: Vector, cr: float):
    un = (p1-p2).norm()
    v1n = v1.projection_on(un)
    v2n = v2.projection_on(un)
    v1n_len = v1n.length()
    v2n_len = v2n.length()
    v1n_len_last = calc_collision_1_d_v1(m1, m2, v1n_len, v2n_len, cr)
    v1n_last = un*v1n_len_last
    v1t_last = v1-v1n
    v1_last = v1n_last + v1t_last
    return v1_last
