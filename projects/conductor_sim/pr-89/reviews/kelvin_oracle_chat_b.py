"""Chat B independent SI reference; authored 2026-11-18 for PR89.
No production imports. Values are computed by a fictitious image source,
not by calling the observer or its reference checker.

q_image=-q*a/d, b=a*a/d. Gauss' law gives Qmetal=q_image.
The source excludes its self field: F=k*q*q_image/(d-b)**2 * n.
Reaction potential is k*q_image/(d-b). Charging the induced response from
zero gives U=(1/2)*q*phi_reaction, also obtained by integrating -F from infinity.
The material ground-terminal current is -dQmetal/dt, not dU/dt.
"""
from math import fsum, hypot, pi

EPS = 8.8541878128e-12


def reference(q, a, center, position, velocity, eps=EPS):
    displacement = tuple(position[i] - center[i] for i in range(3))
    distance = hypot(*displacement)
    assert a > 0 and distance > a and eps > 0 and q != 0
    normal = tuple(s / distance for s in displacement)
    radial_speed = fsum(velocity[i] * normal[i] for i in range(3))
    image_charge = -q * a / distance
    image_offset = a * a / distance
    separation = distance - image_offset
    k = 1 / (4 * pi * eps)
    force_scalar = k * q * image_charge / separation**2
    reaction_potential = k * image_charge / separation
    energy = q * reaction_potential / 2
    charge_rate = q * a * radial_speed / distance**2
    return dict(distance=distance, radial_speed=radial_speed,
                metal_charge=image_charge, charge_rate=charge_rate,
                current=-charge_rate, force_scalar=force_scalar,
                force=tuple(force_scalar * n for n in normal),
                energy=energy, reaction_potential=reaction_potential)
