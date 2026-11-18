"""Independent Chat B SI oracle; no production imports or copied checker calls.
Reviewer: GPT-6 Astra Pro, 2026-11-18. Inputs are serialized physical traces.
"""
import math


def numeric(value, name):
    assert type(value) in (int, float) and math.isfinite(value), (name, value)
    return value


def close(actual, expected, name, relative=2e-9):
    numeric(actual, name)
    assert math.isclose(actual, expected, rel_tol=relative,
                        abs_tol=max(128 * math.ulp(abs(expected)), 1e-28)), (name, actual, expected)


def expected_state(q, radius, epsilon, center, initial, speed, duration, index, count):
    displacement = tuple(initial[j] - center[j] for j in range(3))
    distance0 = math.sqrt(sum(x*x for x in displacement))
    axis = tuple(x/distance0 for x in displacement)
    time = duration*index/(count-1)
    distance = distance0 + speed*time
    k = 1/(4*math.pi*epsilon)
    image_charge = -q*radius/distance
    # Image force on the external source; mechanical energy is half q*phi_image.
    image_separation = distance-radius*radius/distance
    radial_force = k*q*image_charge/(image_separation*image_separation)
    energy = q*k*image_charge/(2*image_separation)
    current = -q*radius*speed/(distance*distance)
    return {
        'index': index, 'time_s': time, 'radial_distance_m': distance,
        'source_position_m': tuple(center[j]+distance*axis[j] for j in range(3)),
        'source_velocity_m_s': tuple(speed*x for x in axis),
        'induced_sphere_net_charge_c': image_charge,
        'wire_current_sphere_to_ground_a': current,
        'wire_current_ground_to_sphere_a': -current,
        'induced_force_on_source_n': tuple(radial_force*x for x in axis),
        'induced_mechanical_energy_j': energy,
    }


def verify_trace(data):
    q = numeric(data['source_charge_c'], 'q')
    radius = numeric(data['sphere_radius_m'], 'radius')
    eps = numeric(data['permittivity_f_per_m'], 'epsilon')
    speed = numeric(data['signed_constant_radial_speed_m_s'], 'speed')
    duration = numeric(data['duration_s'], 'duration')
    count = data['sample_count']
    assert type(count) is int and 3 <= count <= 201
    assert q != 0 and radius > 0 and eps > 0 and duration > 0
    assert 0 < abs(speed) < 29979245.8
    center, initial = data['sphere_center_m'], data['initial_source_position_m']
    assert len(center) == len(initial) == 3
    for v in center + initial:
        numeric(v, 'coordinate')
    assert len(data['samples']) == count
    results = []
    for i, row in enumerate(data['samples']):
        expected = expected_state(q, radius, eps, center, initial, speed, duration, i, count)
        assert type(row['index']) is int and row['index'] == i
        assert row['radial_distance_m'] > radius + data['surface_guard_m']
        for key, value in expected.items():
            if key == 'index':
                continue
            if isinstance(value, tuple):
                assert len(row[key]) == 3
                for j, component in enumerate(value):
                    close(row[key][j], component, f'{i}/{key}/{j}')
            else:
                close(row[key], value, f'{i}/{key}')
        results.append(expected)
    return results
