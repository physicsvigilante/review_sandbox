"""Independent Kelvin image-charge reference for corrected M37a review #02.

Physics derived separately from the observer and its standalone JSON checker:
one grounded metal sphere with one exterior point source in linear vacuum.
The conductor's net charge is the image charge.  The force excludes the
source's own field; U is HALF q times induced reaction potential.
"""
from math import fsum, hypot, pi

EPS = 8.8541878128e-12

def reference(q, a, center, position, velocity, eps=EPS):
    r = tuple(position[i]-center[i] for i in range(3))
    d = hypot(*r)
    assert a > 0 and d > a and eps > 0 and q != 0
    n = tuple(r_i/d for r_i in r)
    vr = fsum(velocity[i]*n[i] for i in range(3))
    # Exact Kelvin image equivalent to the grounded conducting sphere.
    q_im = -q*a/d
    image_displacement = a*a/d
    separation = d-image_displacement
    k = 1/(4*pi*eps)
    scalar_force = k*q*q_im/separation**2
    potential_from_induced_image = k*q_im/separation
    U = .5*q*potential_from_induced_image
    dqdt = q*a*vr/d**2
    return dict(distance=d,radial_speed=vr,metal_charge=q_im,
        charge_rate=dqdt,current=-dqdt,force_scalar=scalar_force,
        force=tuple(scalar_force*z for z in n),energy=U,
        reaction_potential=potential_from_induced_image)
