"""Reviewer-only M40a accepted-nearly-unit surface-normal accuracy probe.

Does not mutate candidate. Both normals have the same geometric direction.
The second is admitted by the 1e-12 `_normal` length tolerance.
"""
from math import pi
from conductor_sim.cavity_gauss import GaussCavityAssembly, SealedCavity, CavityCharge
from conductor_sim.model import Grounded
from conductor_sim.spherical_multicavity import (
    SphericalVoid,NamedSourcePosition,SphericalMetalGeometry,SphericalSigmaModel,solve_spherical_sigma)
a=.85
q=3.1e-9
d=a*(1-1.2e-8) # admitted: clearance > 1e-8 radius
model=SphericalSigmaModel(
    GaussCavityAssembly("M",(SealedCavity("V",(CavityCharge("q",q),)),),Grounded()),
    SphericalMetalGeometry((0.,0.,0.),3.,(
        SphericalVoid("V",(0.,0.,0.),a,(NamedSourcePosition("q",(d,0.,0.)),)),)))
s=solve_spherical_sigma(model)
unit=s.inner_surface_charge_density("V",(1.,0.,0.))
near=s.inner_surface_charge_density("V",(1.+9e-13,0.,0.))
pole=-q*(a+d)/(4*pi*a*(a-d)**2)
relative_error=abs(near-unit)/abs(unit)
print("Genuine physical pole sigma:",pole,flush=True)
print("Native exact-unit sigma:",unit,flush=True)
print("Native accepted-nearly-unit sigma:",near,flush=True)
print("Relative discrepancy for same radial direction:",relative_error,flush=True)
print("normal length deviation:",9e-13,flush=True)
print("physical source-wall relative gap:",(a-d)/a,flush=True)
assert abs((unit-pole)/pole) < 1e-7
assert relative_error>2e-4
print("OBSERVED: accepted near-unit input moves the evaluated point off the sphere.",flush=True)
