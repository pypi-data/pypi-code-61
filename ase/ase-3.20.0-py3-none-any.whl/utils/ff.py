# flake8: noqa
import numpy as np
from numpy import linalg
from ase import units 

# Three variables extracted from what used to be endless repetitions below.
Ax = np.array([[1, 0, 0, -1, 0, 0, 0, 0, 0],
               [0, 1, 0, 0, -1, 0, 0, 0, 0],
               [0, 0, 1, 0, 0, -1, 0, 0, 0],
               [0, 0, 0, -1, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, -1, 0, 0, 1, 0],
               [0, 0, 0, 0, 0, -1, 0, 0, 1]])
Bx = np.array([[1, 0, 0, -1, 0, 0],
               [0, 1, 0, 0, -1, 0],
               [0, 0, 1, 0, 0, -1]])
Mx = Bx



class Morse:
    def __init__(self, atomi, atomj, D, alpha, r0):
        self.atomi = atomi
        self.atomj = atomj
        self.D = D
        self.alpha = alpha
        self.r0 = r0
        self.r = None

class Bond:
    def __init__(self, atomi, atomj, k, b0, 
                 alpha=None, rref=None):
        self.atomi = atomi
        self.atomj = atomj
        self.k = k
        self.b0 = b0
        self.alpha = alpha
        self.rref = rref
        self.b = None

class Angle:
    def __init__(self, atomi, atomj, atomk, k, a0, cos=False, 
                 alpha=None, rref=None):
        self.atomi = atomi
        self.atomj = atomj
        self.atomk = atomk
        self.k = k
        self.a0 = a0
        self.cos = cos
        self.alpha = alpha
        self.rref = rref
        self.a = None

class Dihedral:
    def __init__(self, atomi, atomj, atomk, atoml, k, d0=None, n=None, 
                 alpha=None, rref=None):
        self.atomi = atomi
        self.atomj = atomj
        self.atomk = atomk
        self.atoml = atoml
        self.k = k
        self.d0 = d0
        self.n = n
        self.alpha = alpha
        self.rref = rref
        self.d = None

class VdW:
    def __init__(self, atomi, atomj, epsilonij=None, sigmaij=None, rminij=None,
                 Aij=None, Bij=None, epsiloni=None, epsilonj=None, 
                 sigmai=None, sigmaj=None, rmini=None, rminj=None, scale=1.0):
        self.atomi = atomi
        self.atomj = atomj
        if epsilonij is not None:
            if sigmaij is not None:
                self.Aij = scale * 4.0 * epsilonij * sigmaij**12
                self.Bij = scale * 4.0 * epsilonij * sigmaij**6 * scale
            elif rminij is not None:
                self.Aij = scale * epsilonij * rminij**12
                self.Bij = scale * 2.0 * epsilonij * rminij**6
            else:
                raise NotImplementedError("not implemented combination" 
                                          "of vdW parameters.")
        elif Aij is not None and Bij is not None:
            self.Aij = scale * Aij
            self.Bij = scale * Bij
        elif epsiloni is not None and epsilonj is not None:
            if sigmai is not None and sigmaj is not None:
                self.Aij = ( scale * 4.0 * np.sqrt(epsiloni * epsilonj)
                             * ((sigmai + sigmaj) / 2.0)**12 )
                self.Bij = ( scale * 2.0 * np.sqrt(epsiloni * epsilonj)
                             * ((sigmai + sigmaj) / 2.0)**6 )
            elif rmini is not None and rminj is not None:
                self.Aij = ( scale * np.sqrt(epsiloni * epsilonj)
                             * ((rmini + rminj) / 2.0)**12 )
                self.Bij = ( scale * 2.0 * np.sqrt(epsiloni * epsilonj) 
                             * ((rmini + rminj) / 2.0)**6 )
        else:
            raise NotImplementedError("not implemented combination"
                                      "of vdW parameters.")
        self.r = None

class Coulomb:
    def __init__(self, atomi, atomj, chargeij=None, 
                 chargei=None, chargej=None, scale=1.0):
        self.atomi = atomi
        self.atomj = atomj
        if chargeij is not None:
            self.chargeij = ( scale * chargeij * 8.9875517873681764e9
                              * units.m * units.J / units.C / units.C )
        elif chargei is not None and chargej is not None:
            self.chargeij = ( scale * chargei * chargej * 8.9875517873681764e9
                            * units.m * units.J / units.C / units.C )
        else:
            raise NotImplementedError("not implemented combination"
                                      "of Coulomb parameters.")
        self.r = None

def get_morse_potential_eta(atoms, morse):
    i = morse.atomi
    j = morse.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)

    if dij > morse.r0:
        exp = np.exp(-morse.alpha*(dij-morse.r0))
        eta = 1.0 - (1.0 - exp)**2
    else:
        eta = 1.0

    return eta

def get_morse_potential_value(atoms, morse):
    i = morse.atomi
    j = morse.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)

    exp = np.exp(-morse.alpha*(dij-morse.r0))

    v = morse.D*(1.0-exp)**2

    morse.r = dij

    return i, j, v

def get_morse_potential_gradient(atoms, morse):
    i = morse.atomi
    j = morse.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    exp = np.exp(-morse.alpha*(dij-morse.r0))

    gr = 2.0*morse.D*morse.alpha*exp*(1.0-exp)*eij

    gx = np.dot(Mx.T, gr)

    morse.r = dij

    return i, j, gx

def get_morse_potential_hessian(atoms, morse, spectral=False):
    i = morse.atomi
    j = morse.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij

    exp = np.exp(-morse.alpha*(dij-morse.r0))

    Hr = ( 2.0*morse.D*morse.alpha*exp*(morse.alpha*(2.0*exp-1.0)*Pij
                                        + (1.0-exp)/dij*Qij) )

    Hx = np.dot(Mx.T, np.dot(Hr, Mx))

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    morse.r = dij

    return i, j, Hx

def get_morse_potential_reduced_hessian(atoms, morse):
    i = morse.atomi
    j = morse.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)

    exp = np.exp(-morse.alpha*(dij-morse.r0))

    Hr = np.abs(2.0*morse.D*morse.alpha**2*exp*(2.0*exp-1.0))*Pij

    Hx = np.dot(Mx.T, np.dot(Hr, Mx))

    morse.r = dij

    return i, j, Hx

def get_bond_potential_value(atoms, bond):
    i = bond.atomi
    j = bond.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)

    v = 0.5*bond.k*(dij-bond.b0)**2

    bond.b = dij

    return i, j, v

def get_bond_potential_gradient(atoms, bond):
    i = bond.atomi
    j = bond.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    gr = bond.k*(dij-bond.b0)*eij

    gx = np.dot(Bx.T, gr)

    bond.b = dij

    return i, j, gx

def get_bond_potential_hessian(atoms, bond, morses=None, spectral=False):
    i = bond.atomi
    j = bond.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij

    Hr = bond.k*Pij+bond.k*(dij-bond.b0)/dij*Qij

    if bond.alpha is not None:
        Hr *= np.exp(bond.alpha[0]*(bond.rref[0]**2-dij**2))

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j ):
                Hr *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j ):
                Hr *= get_morse_potential_eta(atoms, morses[m])

    Hx = np.dot(Bx.T, np.dot(Hr, Bx))

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    bond.b = dij

    return i, j, Hx

def get_bond_potential_reduced_hessian(atoms, bond, morses=None):
    i = bond.atomi
    j = bond.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)

    Hr = bond.k*Pij

    if bond.alpha is not None:
        Hr *= np.exp(bond.alpha[0]*(bond.rref[0]**2-dij**2))

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j ):
                Hr *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j ):
                Hr *= get_morse_potential_eta(atoms, morses[m])

    Hx = np.dot(Bx.T, np.dot(Hr, Bx))

    bond.b = dij

    return i, j, Hx

def get_bond_potential_reduced_hessian_test(atoms, bond):

    i, j, v = get_bond_potential_value(atoms, bond)
    i, j, gx = get_bond_potential_gradient(atoms, bond)

    Hx = np.tensordot(gx,gx,axes=0)/v/2.0

    return i, j, Hx

def get_angle_potential_value(atoms, angle):

    i = angle.atomi
    j = angle.atomj
    k = angle.atomk

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    ekj = rkj/dkj
    eijekj = np.dot(eij, ekj)
    if np.abs(eijekj) > 1.0:
        eijekj = np.sign(eijekj)

    a = np.arccos(eijekj)

    if angle.cos:
        da = np.cos(a)-np.cos(angle.a0)
    else:
        da = a-angle.a0
        da = da - np.around(da / np.pi) * np.pi

    v = 0.5*angle.k*da**2

    angle.a = a

    return i, j, k, v

def get_angle_potential_gradient(atoms, angle):
    i = angle.atomi
    j = angle.atomj
    k = angle.atomk

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    ekj = rkj/dkj
    eijekj = np.dot(eij, ekj)
    if np.abs(eijekj) > 1.0:
        eijekj = np.sign(eijekj)

    a = np.arccos(eijekj)
    if angle.cos:
        da = np.cos(a)-np.cos(angle.a0)
    else:
        da = a-angle.a0
        da = da - np.around(da / np.pi) * np.pi
        sina = np.sin(a)

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij
    Pkj = np.tensordot(ekj,ekj,axes=0)
    Qkj = np.eye(3)-Pkj

    gr = np.zeros(6)
    if angle.cos:
        gr[0:3] = angle.k*da/dij*np.dot(Qij,ekj)
        gr[3:6] = angle.k*da/dkj*np.dot(Qkj,eij)
    elif np.abs(sina) > 0.001:
        gr[0:3] = -angle.k*da/sina/dij*np.dot(Qij,ekj)
        gr[3:6] = -angle.k*da/sina/dkj*np.dot(Qkj,eij)

    gx = np.dot(Ax.T, gr)

    angle.a = a

    return i, j, k, gx

def get_angle_potential_hessian(atoms, angle, morses=None, spectral=False):
    i = angle.atomi
    j = angle.atomj
    k = angle.atomk

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    dij2 = dij*dij
    eij = rij/dij
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    dkj2 = dkj*dkj
    ekj = rkj/dkj
    dijdkj = dij*dkj
    eijekj = np.dot(eij, ekj)
    if np.abs(eijekj) > 1.0:
        eijekj = np.sign(eijekj)

    a = np.arccos(eijekj)
    if angle.cos:
        da = np.cos(a)-np.cos(angle.a0)
        cosa0 = np.cos(angle.a0)
    else:
        da = a-angle.a0
        da = da - np.around(da / np.pi) * np.pi
    sina = np.sin(a)
    cosa = np.cos(a)
    ctga = cosa/sina

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij
    Pkj = np.tensordot(ekj,ekj,axes=0)
    Qkj = np.eye(3)-Pkj
    Pik = np.tensordot(eij,ekj,axes=0)
    Pki = np.tensordot(ekj,eij,axes=0)
    P = np.eye(3)*eijekj

    QijPkjQij = np.dot(Qij, np.dot(Pkj, Qij))
    QijPkiQkj = np.dot(Qij, np.dot(Pki, Qkj))
    QkjPijQkj = np.dot(Qkj, np.dot(Pij, Qkj))

    Hr = np.zeros((6,6))
    if angle.cos and np.abs(sina) > 0.001:
        factor = 1.0-2.0*cosa*cosa+cosa*cosa0
        Hr[0:3,0:3] = ( angle.k*(factor*QijPkjQij/sina 
                       - sina*da*(-ctga*QijPkjQij/sina+np.dot(Qij, Pki)
                       -np.dot(Pij, Pki)*2.0+(Pik+P)))/sina/dij2 ) 
        Hr[0:3,3:6] = ( angle.k*(factor*QijPkiQkj/sina 
                       - sina*da*(-ctga*QijPkiQkj/sina
                       -np.dot(Qij, Qkj)))/sina/dijdkj )
        Hr[3:6,0:3] = Hr[0:3,3:6].T
        Hr[3:6,3:6] = ( angle.k*(factor*QkjPijQkj/sina 
                       - sina*da*(-ctga*QkjPijQkj/sina
                       +np.dot(Qkj, Pik)-np.dot(Pkj, Pik)
                       *2.0+(Pki+P)))/sina/dkj2 )
    elif np.abs(sina) > 0.001:
        Hr[0:3,0:3] = ( angle.k*(QijPkjQij/sina 
                       + da*(-ctga*QijPkjQij/sina+np.dot(Qij, Pki)
                       -np.dot(Pij, Pki)*2.0+(Pik+P)))/sina/dij2 )
        Hr[0:3,3:6] = ( angle.k*(QijPkiQkj/sina 
                       + da*(-ctga*QijPkiQkj/sina
                       -np.dot(Qij, Qkj)))/sina/dijdkj )
        Hr[3:6,0:3] = Hr[0:3,3:6].T
        Hr[3:6,3:6] = ( angle.k*(QkjPijQkj/sina 
                       + da*(-ctga*QkjPijQkj/sina
                       +np.dot(Qkj, Pik)-np.dot(Pkj, Pik)
                       *2.0+(Pki+P)))/sina/dkj2 )

    if angle.alpha is not None:
        Hr *= ( np.exp(angle.alpha[0]*(angle.rref[0]**2-dij**2))
               *np.exp(angle.alpha[1]*(angle.rref[1]**2-dkj**2)) )

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j or 
                 morses[m].atomi == k ):
                Hr *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j or 
                   morses[m].atomj == k ):
                Hr *= get_morse_potential_eta(atoms, morses[m])

    Hx = np.dot(Ax.T, np.dot(Hr, Ax))

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    angle.a = a

    return i, j, k, Hx

def get_angle_potential_reduced_hessian(atoms, angle, morses=None):
    i = angle.atomi
    j = angle.atomj
    k = angle.atomk

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    dij2 = dij*dij
    eij = rij/dij
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    dkj2 = dkj*dkj
    ekj = rkj/dkj
    dijdkj = dij*dkj
    eijekj = np.dot(eij, ekj)
    if np.abs(eijekj) > 1.0:
        eijekj = np.sign(eijekj)

    a = np.arccos(eijekj)
    sina = np.sin(a)
    sina2 = sina*sina

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij
    Pkj = np.tensordot(ekj,ekj,axes=0)
    Qkj = np.eye(3)-Pkj
    Pki = np.tensordot(ekj,eij,axes=0)

    Hr = np.zeros((6,6))
    if np.abs(sina) > 0.001:
        Hr[0:3,0:3] = np.dot(Qij, np.dot(Pkj, Qij))/dij2
        Hr[0:3,3:6] = np.dot(Qij, np.dot(Pki, Qkj))/dijdkj
        Hr[3:6,0:3] = Hr[0:3,3:6].T
        Hr[3:6,3:6] = np.dot(Qkj, np.dot(Pij, Qkj))/dkj2

    if angle.cos and np.abs(sina) > 0.001:
        cosa = np.cos(a)
        cosa0 = np.cos(angle.a0)
        factor = np.abs(1.0-2.0*cosa*cosa+cosa*cosa0)
        Hr = Hr*factor*angle.k/sina2
    elif np.abs(sina) > 0.001:
        Hr = Hr*angle.k/sina2

    if angle.alpha is not None:
        Hr *= ( np.exp(angle.alpha[0]*(angle.rref[0]**2-dij**2))
               *np.exp(angle.alpha[1]*(angle.rref[1]**2-dkj**2)) )

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j or 
                 morses[m].atomi == k ):
                Hr *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j or 
                   morses[m].atomj == k ):
                Hr *= get_morse_potential_eta(atoms, morses[m])

    Hx=np.dot(Ax.T, np.dot(Hr, Ax))

    angle.a = a

    return i, j, k, Hx

def get_angle_potential_reduced_hessian_test(atoms, angle):
    i, j, k, v = get_angle_potential_value(atoms, angle)
    i, j, k, gx = get_angle_potential_gradient(atoms, angle)

    Hx = np.tensordot(gx,gx,axes=0)/v/2.0

    return i, j, k, Hx

def get_dihedral_potential_value(atoms, dihedral):
    i = dihedral.atomi
    j = dihedral.atomj
    k = dihedral.atomk
    l = dihedral.atoml

    rij = rel_pos_pbc(atoms, i, j)
    rkj = rel_pos_pbc(atoms, k, j)
    rkl = rel_pos_pbc(atoms, k, l)

    rmj = np.cross(rij, rkj)
    dmj = linalg.norm(rmj)
    emj = rmj/dmj
    rnk = np.cross(rkj, rkl)
    dnk = linalg.norm(rnk)
    enk = rnk/dnk
    emjenk = np.dot(emj, enk)
    if np.abs(emjenk) > 1.0:
        emjenk = np.sign(emjenk)

    d = np.sign(np.dot(rkj, np.cross(rmj, rnk)))*np.arccos(emjenk)

    if dihedral.d0 is None:
        v = 0.5*dihedral.k*(1.0 - np.cos(2.0 * d))
    else:
        dd = d-dihedral.d0
        dd = dd - np.around(dd / np.pi / 2.0) * np.pi * 2.0
        if dihedral.n is None:
            v = 0.5*dihedral.k*dd**2
        else:
            v = dihedral.k*(1.0 + np.cos(dihedral.n*d - dihedral.d0))

    dihedral.d = d

    return i, j, k, l, v

def get_dihedral_potential_gradient(atoms, dihedral):
    i = dihedral.atomi
    j = dihedral.atomj
    k = dihedral.atomk
    l = dihedral.atoml

    rij = rel_pos_pbc(atoms, i, j)
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    dkj2 = dkj*dkj
    rkl = rel_pos_pbc(atoms, k, l)

    rijrkj = np.dot(rij, rkj)
    rkjrkl = np.dot(rkj, rkl)

    rmj = np.cross(rij, rkj)
    dmj = linalg.norm(rmj)
    dmj2 = dmj*dmj
    emj = rmj/dmj
    rnk = np.cross(rkj, rkl)
    dnk = linalg.norm(rnk)
    dnk2 = dnk*dnk
    enk = rnk/dnk
    emjenk = np.dot(emj, enk)
    if np.abs(emjenk) > 1.0:
        emjenk = np.sign(emjenk)

    dddri = dkj/dmj2*rmj
    dddrl = -dkj/dnk2*rnk

    gx = np.zeros(12)

    gx[0:3] = dddri
    gx[3:6] = (rijrkj/dkj2-1.0)*dddri-rkjrkl/dkj2*dddrl
    gx[6:9] = (rkjrkl/dkj2-1.0)*dddrl-rijrkj/dkj2*dddri
    gx[9:12] = dddrl

    d = np.sign(np.dot(rkj, np.cross(rmj, rnk)))*np.arccos(emjenk)

    if dihedral.d0 is None:
        gx *= dihedral.k*np.sin(2.0 * d)
    else:
        dd = d-dihedral.d0
        dd = dd - np.around(dd / np.pi / 2.0) * np.pi * 2.0
        if dihedral.n is None:
            gx *= dihedral.k*dd
        else:
            gx *= -dihedral.k*dihedral.n*np.sin(dihedral.n*d - dihedral.d0)

    dihedral.d = d

    return i, j, k, l, gx

def get_dihedral_potential_hessian(atoms, dihedral, morses=None, 
                                   spectral=False):
    eps = 0.000001

    i,j,k,l,g = get_dihedral_potential_gradient(atoms, dihedral)

    Hx = np.zeros((12,12))

    dihedral_eps = Dihedral(dihedral.atomi, dihedral.atomj, 
                            dihedral.atomk, dihedral.atoml, 
                            dihedral.k, dihedral.d0, dihedral.n)
    indx = [3*i, 3*i+1, 3*i+2,
            3*j, 3*j+1, 3*j+2,
            3*k, 3*k+1, 3*k+2,
            3*l, 3*l+1, 3*l+2]
    for x in range(12):
        a = atoms.copy()
        positions = np.reshape(a.get_positions(),-1)
        positions[indx[x]] += eps
        a.set_positions(np.reshape(positions, (len(a),3)))
        i,j,k,l,geps = get_dihedral_potential_gradient(a, dihedral_eps)
        for y in range(12):
            Hx[x,y] += 0.5*(geps[y]-g[y])/eps
            Hx[y,x] += 0.5*(geps[y]-g[y])/eps

    if dihedral.alpha is not None:
        rij = rel_pos_pbc(atoms, i, j)
        dij = linalg.norm(rij)
        rkj = rel_pos_pbc(atoms, k, j)
        dkj = linalg.norm(rkj)
        rkl = rel_pos_pbc(atoms, k, l)
        dkl = linalg.norm(rkl)
        Hx *= ( np.exp(dihedral.alpha[0]*(dihedral.rref[0]**2-dij**2))
               *np.exp(dihedral.alpha[1]*(dihedral.rref[1]**2-dkj**2))
               *np.exp(dihedral.alpha[2]*(dihedral.rref[2]**2-dkl**2)) )

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j or 
                 morses[m].atomi == k or 
                 morses[m].atomi == l ):
                Hx *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j or 
                   morses[m].atomj == k or 
                   morses[m].atomj == l ):
                Hx *= get_morse_potential_eta(atoms, morses[m])

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    return i, j, k, l, Hx

def get_dihedral_potential_reduced_hessian(atoms, dihedral, morses=None):
    i = dihedral.atomi
    j = dihedral.atomj
    k = dihedral.atomk
    l = dihedral.atoml

    rij = rel_pos_pbc(atoms, i, j)
    rkj = rel_pos_pbc(atoms, k, j)
    dkj = linalg.norm(rkj)
    dkj2 = dkj*dkj
    rkl = rel_pos_pbc(atoms, k, l)

    rijrkj = np.dot(rij, rkj)
    rkjrkl = np.dot(rkj, rkl)

    rmj = np.cross(rij, rkj)
    dmj = linalg.norm(rmj)
    dmj2 = dmj*dmj
    emj = rmj/dmj
    rnk = np.cross(rkj, rkl)
    dnk = linalg.norm(rnk)
    dnk2 = dnk*dnk
    enk = rnk/dnk
    emjenk = np.dot(emj, enk)
    if np.abs(emjenk) > 1.0:
        emjenk = np.sign(emjenk)

    d = np.sign(np.dot(rkj, np.cross(rmj, rnk)))*np.arccos(emjenk)

    dddri = dkj/dmj2*rmj
    dddrl = -dkj/dnk2*rnk

    gx = np.zeros(12)

    gx[0:3] = dddri
    gx[3:6] = (rijrkj/dkj2-1.0)*dddri-rkjrkl/dkj2*dddrl
    gx[6:9] = (rkjrkl/dkj2-1.0)*dddrl-rijrkj/dkj2*dddri
    gx[9:12] = dddrl

    if dihedral.d0 is None:
        Hx = np.abs(2.0*dihedral.k*np.cos(2.0 * d))*np.tensordot(gx,gx,axes=0)
    if dihedral.n is None: 
        Hx = dihedral.k*np.tensordot(gx,gx,axes=0)
    else:
        Hx = ( np.abs(-dihedral.k*dihedral.n**2
              *np.cos(dihedral.n*d-dihedral.d0))*np.tensordot(gx,gx,axes=0) )

    if dihedral.alpha is not None:
        rij = rel_pos_pbc(atoms, i, j)
        dij = linalg.norm(rij)
        rkj = rel_pos_pbc(atoms, k, j)
        dkj = linalg.norm(rkj)
        rkl = rel_pos_pbc(atoms, k, l)
        dkl = linalg.norm(rkl)
        Hx *= ( np.exp(dihedral.alpha[0]*(dihedral.rref[0]**2-dij**2))
               *np.exp(dihedral.alpha[1]*(dihedral.rref[1]**2-dkj**2))
               *np.exp(dihedral.alpha[2]*(dihedral.rref[2]**2-dkl**2)) )

    if morses is not None:
        for m in range(len(morses)):
            if ( morses[m].atomi == i or 
                 morses[m].atomi == j or 
                 morses[m].atomi == k or 
                 morses[m].atomi == l ):
                Hx *= get_morse_potential_eta(atoms, morses[m])
            elif ( morses[m].atomj == i or 
                   morses[m].atomj == j or 
                   morses[m].atomj == k or 
                   morses[m].atomj == l ):
                Hx *= get_morse_potential_eta(atoms, morses[m])

    dihedral.d = d

    return i, j, k, l, Hx

def get_dihedral_potential_reduced_hessian_test(atoms, dihedral):
    i, j, k, l, gx = get_dihedral_potential_gradient(atoms, dihedral)

    if dihedral.n is None:
        i, j, k, l, v = get_dihedral_potential_value(atoms, dihedral)
        Hx = np.tensordot(gx,gx,axes=0)/v/2.0
    else:
        arg = dihedral.n*dihedral.d - dihedral.d0
        Hx = ( np.tensordot(gx,gx,axes=0)/dihedral.k/np.sin(arg)/np.sin(arg)
              *np.cos(arg) )

    return i, j, k, l, Hx

def get_vdw_potential_value(atoms, vdw):
    i = vdw.atomi
    j = vdw.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)

    v = vdw.Aij/dij**12 - vdw.Bij/dij**6

    vdw.r = dij

    return i, j, v

def get_vdw_potential_gradient(atoms, vdw):
    i = vdw.atomi
    j = vdw.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    gr = (-12.0*vdw.Aij/dij**13+6.0*vdw.Bij/dij**7)*eij

    gx = np.dot(Bx.T, gr)

    vdw.r = dij

    return i, j, gx

def get_vdw_potential_hessian(atoms, vdw, spectral=False):
    i = vdw.atomi
    j = vdw.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij

    Hr = ( (156.0*vdw.Aij/dij**14-42.0*vdw.Bij/dij**8)*Pij
          +(-12.0*vdw.Aij/dij**13+6.0*vdw.Bij/dij**7)/dij*Qij )

    Hx = np.dot(Bx.T, np.dot(Hr, Bx))

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    vdw.r = dij

    return i, j, Hx

def get_coulomb_potential_value(atoms, coulomb):
    i = coulomb.atomi
    j = coulomb.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)

    v = coulomb.chargeij/dij

    coulomb.r = dij

    return i, j, v

def get_coulomb_potential_gradient(atoms, coulomb):
    i = coulomb.atomi
    j = coulomb.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    gr = -coulomb.chargeij/dij/dij*eij

    gx = np.dot(Bx.T, gr)

    coulomb.r = dij

    return i, j, gx

def get_coulomb_potential_hessian(atoms, coulomb, spectral=False):
    i = coulomb.atomi
    j = coulomb.atomj

    rij = rel_pos_pbc(atoms, i, j)
    dij = linalg.norm(rij)
    eij = rij/dij

    Pij = np.tensordot(eij,eij,axes=0)
    Qij = np.eye(3)-Pij

    Hr = (2.0*coulomb.chargeij/dij**3)*Pij+(-coulomb.chargeij/dij/dij)/dij*Qij

    Hx = np.dot(Bx.T, np.dot(Hr, Bx))

    if spectral:
        eigvals, eigvecs = linalg.eigh(Hx)
        D = np.diag(np.abs(eigvals))
        U = eigvecs
        Hx = np.dot(U,np.dot(D,np.transpose(U)))

    coulomb.r = dij

    return i, j, Hx

def rel_pos_pbc(atoms, i, j):
    """
    Return difference between two atomic positions, 
    correcting for jumps across PBC
    """
    d = atoms.get_positions()[i,:]-atoms.get_positions()[j,:]
    g = linalg.inv(atoms.get_cell().T)
    f = np.floor(np.dot(g, d.T) + 0.5)
    d -= np.dot(atoms.get_cell().T, f).T
    return d
