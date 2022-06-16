from vector import *
from planet import Planet

g = 6.6743 * (10 ** -11)


def apply_gravity(planet1: Planet, planet2: Planet) -> None:
    u = planet2.pos - planet1.pos
    grav = g * planet1.mass * planet2.mass / (u.length() ** 2)
    planet1.add_force(u.scale_to(grav))
    planet2.add_force(u.scale_to(-grav))


def collision(planet1: Planet, planet2: Planet) -> None:
    if (planet1.pos - planet2.pos).length() <= planet1.radius + planet2.radius:
        collision_correction(planet1, planet2)
        collision_resolution(planet1, planet2)


def collision_correction(planet1: Planet, planet2: Planet) -> None:
    un = planet2.pos - planet1.pos
    correcting = planet1.radius + planet2.radius - un.length()
    c1 = ((-correcting*planet2.mass) /
          (planet1.mass+planet2.mass))*un.norm()
    c2 = ((correcting*planet1.mass) /
          (planet1.mass+planet2.mass))*un.norm()
    planet1.add_pos(c1)
    planet2.add_pos(c2)


def collision_resolution(planet1: Planet, planet2: Planet) -> None:
    un = (planet2.pos - planet1.pos).norm()
    v1_len = planet1.velocity.dot(un)
    v2_len = planet2.velocity.dot(un)
    if v1_len < v2_len:
        return
    cr = planet1.flexibility * planet2.flexibility

    v1_len_new = ((cr * planet2.mass * (planet2.velocity - planet1.velocity)) + (planet1.mass *
                  planet1.velocity) + (planet2.mass * planet2.velocity)) / (planet1.mass + planet2.mass)
    v2_len_new = ((cr * planet1.mass * (planet1.velocity - planet2.velocity)) + (planet1.mass *
                  planet1.velocity) + (planet2.mass * planet2.velocity)) / (planet1.mass + planet2.mass)

    v1 = un * v1_len
    v2 = un * v2_len

    v1_new = un * v1_len_new
    v2_new = un * v2_len_new

    planet1.add_velocity(v1_new - v1)
    planet2.add_velocity(v2_new - v2)
