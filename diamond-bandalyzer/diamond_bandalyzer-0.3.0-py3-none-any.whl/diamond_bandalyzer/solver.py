"""Base class for a numerical solver."""

__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

import numpy as np
from diamond_bandalyzer.utilities import extrema_fast
from diamond_bandalyzer.settingsobject import SettingsObject


class Solver(SettingsObject):
    _settings_heading_ = "SolverBase"
    default_settings = {'accuracy': 1e-6}


    def __init__(self, z_mesh=None, init=None, z_mesh_file=None, **kwargs):
        super().__init__(z_mesh, **kwargs)

        self.__add_default_settings__(Solver, **kwargs)
        self.unsolved = True
        self.failed = False  # Somethings gone wrong, end the iteration.

        if z_mesh is not None:
            self.z_mesh = z_mesh
            self.s_mesh = self._initialise_solution_(init)
            self.s_mesh_last = self._initialise_solution_(init)
        elif z_mesh_file is not None:
            try:
                #load file
                self.z_mesh = np.loadtxt('/.config/{}'.format(z_mesh_file))
            except:
                IOError('z_mesh_file could not be found! This is a fatal error, please make sure to run the z_mesher.')
        else:
            RuntimeError('No z_mesh provided and no z_mesh_file found. This is a fatal error, please make sure to run '
                         +'the z_mesher or specify a z_mesh manually.')

        self.diff = 1
        self.end_condition = self.settings['accuracy']


    def __step__(self):
        """Steps the solver, needs to be implemented per solver."""
        pass

    def __updates__(self, n):
        """Any updates to variables before the current step (n)."""
        pass

    def __update_end_condition__(self):
        """Overwrite to apply any updates to end condition, such as multiplying by variable under/over relaxation parameters."""
        pass

    def __fail_solver__(self, msg=None):
        self.failed = True
        if msg:
            print(msg)

    def __is_solved__(self, n):
        """Applies desired check to see if system is solved, can be overridden."""
        self.diff = np.max(np.abs(extrema_fast(self.s_mesh_last-self.s_mesh)))
        self.__update_end_condition__()
        return self.diff < self.end_condition

    def _initialise_solution_(self, init):
        if init is None:
            return np.zeros_like(self.z_mesh)
        elif type(init) is (int or float):
            return np.zeros_like(self.z_mesh) + init
        elif init.shape == self.z_mesh.shape:
            return init
        else:
            raise NotImplementedError("Not sure what to do with provided initial solution.")

    def _initialise_solver_(self):
        pass

    def solve(self):
        # self.unsolved = False  # hard block on running during testing/development delete when ready.
        self._initialise_solver_()
        n = 0
        while self.unsolved and not self.failed:
            self.s_mesh_last = np.copy(self.s_mesh)  # Ensure s_mesh_last is protected from changes to s_mesh.
            self.__updates__(n)
            self.__step__()
            self.unsolved = not self.__is_solved__(n)
            n += 1
        self._on_solve()

    def _on_solve(self):
        """Run if solved itself."""

    def get_solution(self):
        if not self.unsolved:
            return np.array(self.s_mesh)
