from ase import *
from hotbit import *
from box.md import check_energy_conservation

M=7
atoms = Atoms('Au2',[(5,0,0),(5,2.5,0.3)])
atoms.set_container(type='Wedge',M=M)
calc=Hotbit(SCC=False,txt='-',kpts=(M,1,1))
atoms.set_calculator(calc)
e1 = atoms.get_potential_energy()


whole = atoms.extended_copy([(i-M/2,0,0) for i in range(M)])
calc=Hotbit(SCC=False,txt='-')
whole.set_calculator(calc)
e2 = whole.get_potential_energy()

assert abs(M*e1-e2)<1E-10


assert check_energy_conservation(atoms,dt=2.5*fs,steps=50,tol=0.01,plot=False)

#dyn = VelocityVerlet(atoms,2.5*fs)
#traj = PickleTrajectory('koe.traj','w',atoms)
#dyn.attach(traj.write)
#dyn.run(100)