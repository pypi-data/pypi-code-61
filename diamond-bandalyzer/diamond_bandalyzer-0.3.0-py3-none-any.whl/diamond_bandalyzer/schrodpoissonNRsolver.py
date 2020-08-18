__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

from diamond_bandalyzer.solver import Solver
from diamond_bandalyzer.schrodpoissonequations import SchrodingerPoissonEquations
from scipy import sparse
import diamond_bandalyzer.differentiationStencil as differentiationStencil
import numpy as np
from diamond_bandalyzer.utilities import extrema_fast


class SchrodingerPoissonNRSolver(Solver, SchrodingerPoissonEquations):
    _settings_heading_ = "SchrodingerPoissonNRSolver"
    default_settings = {'derivativeorder': 4, 'omega_nr_s': 0.1,  'extraphantompts' : 10}

    def __init__(self, z_mesh=None, init=None, ef_init=None, **kwargs):
        super().__init__(z_mesh, init=init, **kwargs)
        self.__add_default_settings__(SchrodingerPoissonNRSolver, **kwargs)
        if ef_init is not None:
            self.Ef = ef_init
        else:
            self.Ef = self.__estimate_fermi_energy__(self.s_mesh)
        self.Ef_backup = self.Ef
        self.diff = 1e6
        self.z_mesh = z_mesh
        self.z_mesh_diffs = np.diff(self.z_mesh)
        self.order = self.settings['derivativeorder']
        self.numex = self.settings['extraphantompts']
        self.omegaNR = self.settings['omega_nr_s']


        # TODO move into solver initalise.
        if self.order == 2 or self.order == 4:  # Phantom point initialization stuff
            self.z_mesh_phantom = np.zeros(len(self.z_mesh) + 2*(self.order + self.numex))
            self.s_mesh_phantom = np.zeros(len(self.s_mesh) + 2*(self.order + self.numex))
            self.z_mesh_phantom[int(self.order + self.numex):-int(self.order + self.numex)] = self.z_mesh
            self.z_mesh_phantom[0:int(self.order + self.numex)] = self.z_mesh[0] + np.arange(-int(self.order + self.numex), 0, 1) * \
                                                         self.z_mesh_diffs[0]
            self.z_mesh_phantom[-int(self.order + self.numex):] = self.z_mesh[-1] + np.arange(1, int(self.order + self.numex) + 1, 1) * \
                                                         self.z_mesh_diffs[-1]
            self.z_mesh_phantom_diffs = np.diff(self.z_mesh_phantom)
            self.z_mesh = self.z_mesh_phantom[int(self.order + self.numex):-int(self.order + self.numex)]
            self.s_mesh_phantom[int(self.order + self.numex):-int(self.order + self.numex)] = self.s_mesh
            self.s_mesh = self.s_mesh_phantom[int(self.order + self.numex):-int(self.order + self.numex)]
            if init is not None:
                self.s_mesh_phantom[:int(self.order + self.numex)] = np.ones(int(self.order + self.numex)) * self.s_mesh[0]
                self.s_mesh_phantom[-int(self.order + self.numex):] = np.ones(int(self.order + self.numex)) * self.s_mesh[-1]
            if self.order == 2:
                self.stencil = differentiationStencil.SecondOrderSecondDerivative(self.z_mesh_phantom,
                                                                                  self.z_mesh_phantom_diffs)
            elif self.order == 4:
                self.stencil = differentiationStencil.FourthOrderSecondDerivative(self.z_mesh_phantom,
                                                                                  self.z_mesh_phantom_diffs)
        else:
            raise NotImplementedError('We only have 2nd and 4th order accurate 2nd derivatives!')

        # TODO check what we need to keep in persistent memory.
        self.stencil.modifyEndPoints()
        self.ddot_stencil = sparse.csr_matrix(self.stencil.get_stencil())
        self.lhs_stencil = sparse.csr_matrix(self.stencil.get_stencil())
        self.original_diagonal = self.ddot_stencil.diagonal(0)
        self.charge_deriv_terms = np.zeros(len(self.z_mesh_phantom))

    def __step__(self):
        """Does one step of the Newton-Raphson iteration"""
        rhs = self.generate_rhs()  # RHS of the equation (here also updates the wavefunctions)
        lhs_stencil = self.generate_lhs()  # LHS (matrix) of the equation
        step_direc = sparse.linalg.spsolve(lhs_stencil, -rhs, use_umfpack=True)  # Solve for the next step
        self.s_mesh_last = self.s_mesh
        self.s_mesh_phantom = self.s_mesh_phantom + self.omegaNR * step_direc  # Take the (scaled) step
        self.s_mesh = self.s_mesh_phantom[int(self.order + self.numex):-int(self.order + self.numex)]
        # Recompute hole density for the exchange correlation potential if using quantum hole density
        self.hole_density(self.s_mesh, self.Ef)
        self.diff = np.max(np.abs(extrema_fast(self.s_mesh - self.s_mesh_last)))
        #  if self.diff > prevDiff and self.diff < 1e-9:
        #      self.omegaNR = 0.5*self.omegaNR
        if self.diff < 1e-3:  # If close to convergence, shift the solution (and Ef) so that the minimum potential is 0
            self.EfOld = self.Ef
            minVal = np.min(self.s_mesh)
            self.Ef = self.Ef - self.kT * minVal
            self.s_mesh_phantom -= minVal
            self.s_mesh_last -= minVal
           # print(self.integrated_charge(self.Ef, self.s_mesh))
        # TODO: Recompute wavefunctions (the corrector) using the hole densities associated with the updated V (the predictor)

    def __updates__(self, n):
        pass

    def generate_rhs(self):
        rhs = self.ddot_stencil.dot(self.s_mesh_phantom)  # Laplacian of v
        rhs[int(self.order + self.numex):-int(self.order + self.numex)] += self.constRhotoV * self.rho_from_v(
            self.s_mesh, True)  # Add scaled charge density and update eigenpairs

        rhs[int(self.order + self.numex) - 1] -= self.constRhotoV * self.top_surface(self.Ef, self.s_mesh[0]) / \
                                        self.z_mesh_phantom_diffs[0]  # Top surface charge density

        rhs[-int(self.order + self.numex)] -= self.constRhotoV * self.back_surface(self.Ef, self.s_mesh[-1]) / \
                                     self.z_mesh_phantom_diffs[-1]  # Back surface charge density
        return rhs

    def generate_lhs(self):
        # Sum the total derivative of all bulk charges (electrons, holes, defects)
        self.charge_deriv_terms.fill(0)
        self.charge_deriv_terms[int(self.order + self.numex):-int(self.order + self.numex)] = self.rho_from_v_deriv(self.s_mesh)
        # Add the derivatives of the surface charge densities here (off diagonal terms)
        top_charge_deriv_term = self.constRhotoV * self.top_surface_deriv(self.Ef, self.s_mesh[0]) / \
                                self.z_mesh_phantom_diffs[0]
        back_charge_deriv_term = self.constRhotoV * self.back_surface_deriv(self.Ef, self.s_mesh[-1]) / \
                                 self.z_mesh_phantom_diffs[-1]

        upper_diag = self.ddot_stencil.diagonal(1)
        lower_diag = self.ddot_stencil.diagonal(-1)
        upper_diag[int(self.order + self.numex) - 1] += top_charge_deriv_term
        lower_diag[-int(self.order + self.numex)] += back_charge_deriv_term
        # Create the LHS of the equation to be solved by changing the 3 central diagonals
        lhs_stencil = self.lhs_stencil
        lhs_stencil.setdiag(self.original_diagonal + self.constRhotoV * self.charge_deriv_terms)
        lhs_stencil.setdiag(upper_diag, 1)
        lhs_stencil.setdiag(lower_diag, -1)
        return lhs_stencil

    def e_field_from_rho(self, rho, vs, vbs):
        """Overrides the e_field_from_rho function in poissonequations to simply compute the electric field via
        a second-order accurate central difference gradient of v"""
        efield = (1 / self.constEtoV) * np.gradient(self.s_mesh_phantom, self.z_mesh_phantom, edge_order=1)
        return efield[int(self.order + self.numex):-int(self.order + self.numex)]

    def __update_end_condition__(self):
        pass
