"""Solution class, handel's generating, saving and reloading solve diamond bands."""

__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

import numpy as np
import datetime
import re
import traceback
import matplotlib.pyplot as plt
from pathlib import Path
from bandalyzer_app.settingsobject import SettingsObject
from bandalyzer_app.defects import Defects
from bandalyzer_app import poissonrelaxationsolver, poissonNRsolver, schrodpoissonNRsolver
from bandalyzer_app.plotter import plotter
from bandalyzer_app.utilities import int_float, solve_meshing_problem
from scipy.interpolate import pchip
from scipy.ndimage import gaussian_filter1d



# TODO manipulate the spacing for readability.
def make_data_comments(Qspace):
    return 'z_mesh / Q external' + ' '*4 + (' '*20).join(f"{Q:0.0e}" for Q in Qspace)


def parse_data_comments(comments):
    return np.fromstring(comments[len('# z_mesh / Q external   '):], sep=' ')


white_list_operators = ['+', '-', '/', '*', '**', '(', ')']

solver_types = {
    'Relax_Poisson': ["The relaxation method of solving the Poisson equation to determine a diamonds band structure.",
                      poissonrelaxationsolver.PoissonRelaxationSolver],
    'NR_Poisson': ["Newton Rhaphson minimisation The relaxation method of solving the Poisson equation to determine "
                   "a diamonds band structure.",
                   poissonNRsolver.PoissonNRSolver],
    'NR_Schrodinger': ["Newton Rhaphson minimisation The relaxation method of solving the Schrodinger-Poisson equation "
                       "to determine a diamonds band structure.",
                       schrodpoissonNRsolver.SchrodingerPoissonNRSolver],
}


class DiamondSoln(SettingsObject):
    _settings_heading_ = "DiamondBandSolve"
    default_settings = {'solver_type': None, 'z_mesh_definition': 'auto', 'q_external_definition': None,
                        'q_externalBack_definition': None, 'diamond_thickness': 0.050, 'z_mesh_maxpoints': 5000}

    def __init__(self, dry_run=False, initial_solution_file=None, initial_fom_file=None, overwrite=False, **kwargs):
        super().__init__(**kwargs)
        self.__add_default_settings__(DiamondSoln, **kwargs)
        self.z_mesh = None
        self.defects = None
        self.kwargs = kwargs
        self.settings_file = None
        self.local_dir = None
        self.initial_solution = None
        self.Qspace = None
        self.solved_Qspace = None
        self.initEf = None
        self.dry_run = dry_run
        self.solver_class = None
        self.soln_space = None
        self.fom = None
        self.temp_solver_class = None
        self.initial_soln_non_zero_idx = []
        self.overwrite_file = None
        self.Qexternal_back = 0
        if initial_solution_file is not None:
            initial_solution_file = Path(initial_solution_file)
            if initial_solution_file.is_file():
                self.initial_solution = np.loadtxt(initial_solution_file).T
                self.z_mesh = self.initial_solution[0]
                self.initial_solution = self.initial_solution[1:]
                self.initial_soln_non_zero_idx = np.ravel(np.argwhere(np.sum(self.initial_solution, axis=1) > 1))
                with open(initial_solution_file) as f:
                    first_line = f.readline()
                # just incase we didn't get given a fom file.
                self.solved_Qspace = parse_data_comments(first_line)
                self.settings['inital_solution_filename'] = str(initial_solution_file.absolute())
                if overwrite:
                    self.overwrite_file = initial_solution_file

        if initial_fom_file is not None:
            initial_fom_file = Path(initial_fom_file)
            if initial_fom_file.is_file():
                init_fom = np.loadtxt(initial_fom_file).T
                self.solved_Qspace = init_fom[0]
                self.initEf = init_fom[1]
                self.settings['inital_FOM_filename'] = str(initial_fom_file.absolute())

    def initialise(self):
        # Get our settings file and local directories.
        self.settings_file = self.settings['settings_file']
        self.local_dir = self.settings['local_dir']

        # Load in our defects:
        self.defects = Defects(**self.kwargs)

        # find the chosen solver class
        if self.settings['solver_type'] not in solver_types:
            raise NotImplementedError(
                f"Solver type {self.settings['solver_type']} not implemented, see diamondsolve --solver-types.")
        self.solver_class = solver_types[self.settings['solver_type']][1]

        # If don't already have a z-mesh from init.
        # TODO raise warning here if settings.ini diverges from initial solution z-mesh.
        if self.z_mesh is None:
            if self.settings['z_mesh_definition'] == 'auto':
                self.z_mesh = self.z_mesh_auto()
        #        plt.plot(range(len(self.z_mesh)), self.z_mesh)
        #        plt.show()
            else:
                self.z_mesh = self.z_mesh_from_def()

        # Determine Q solution space definition, we floor as we only want integer Qexternal.
        Qdef = self.settings['q_external_definition']
        if Qdef is not None:
            if np.shape(Qdef):
                 self.Qspace = np.floor(np.linspace(*Qdef))
            else:
                self.Qspace = Qdef
        # Fill out Qspace with any solved_Qspace values not defined, ensure unique Qspace.
        if self.solved_Qspace is not None:
            self.Qspace = np.concatenate((self.Qspace, self.solved_Qspace))
            self.Qspace = np.unique(self.Qspace)

        # build the solution space:
        self.soln_space = np.zeros((len(self.Qspace), len(self.z_mesh)))

        # build the fom class ### THIS IS A LITMUS TEST FOR Z MESH SHARING ACROSS MULTIPLE INSTANCES
        self.temp_solver_class = self.solver_class(z_mesh=np.linspace(0,420e-9,69), Qext_top=0, defects=self.defects, **self.kwargs)
        defect_names = list(self.temp_solver_class.get_defect_densities(0, 0).keys())
        self.fom = FiguresOfMerit(defect_names, len(self.Qspace), **self.kwargs)
        self.fom.set_column(0, self.Qspace)

        # build any special solver args here
        if self.settings['q_externalBack_definition'] is not None:
            self.Qexternal_back = float(self.settings['q_externalBack_definition'])

    def solve(self):
        if self.dry_run:
            print(f"Solving with {self.solver_class}.\nPassing {self.kwargs}.\nOur z_mesh:\n{self.z_mesh}\n "
                  f"It has a length of {len(self.z_mesh)} and we will need {len(self.z_mesh)**2*8e-9:0.0f}Gb of memory "
                  f"per diamond.\n Qexternal: {self.Qspace}")
            print("FOM row definitions: ")
            self.fom.print_row_statements()
            return

        # TODO smarter starting, i.e. order of Qspace solving to maximise closeness of initial conditions
        direction = 1
        if self.initial_soln_non_zero_idx:
            if self.initial_soln_non_zero_idx[0] > len(self.solved_Qspace) / 2:
                direction = -1
        for n, Qexternal in enumerate(self.Qspace[::direction]):
            self.__solve_single__(n, Qexternal)

    def _best_inital_soln(self, Qexternal):
        to_init = None
        if self.solved_Qspace is not None:
            to_init = np.argmin(np.abs(self.solved_Qspace - Qexternal))
        to_solved = np.argmin(np.abs(self.Qspace - Qexternal))
        current_soln_non_zero_idx = np.ravel(np.argwhere(np.sum(self.soln_space, axis=1) > 1))

        if to_solved in current_soln_non_zero_idx:
            if to_init in self.initial_soln_non_zero_idx:
                if np.abs(self.Qspace[to_solved] - Qexternal) > np.abs(self.solved_Qspace[to_init] - Qexternal):
                    return self.initial_solution[to_init]
                return self.soln_space[to_solved]
            else:
                return self.soln_space[to_solved]
        elif to_init in self.initial_soln_non_zero_idx:
            return self.initial_solution[to_init]
        return None

    def __solve_single__(self, n, Qexternal):
        initial_s_mesh = self._best_inital_soln(Qexternal)
        try:
            the_solver = self.solver_class(z_mesh=self.z_mesh, Qext_top=Qexternal, defects=self.defects,
                                           init=initial_s_mesh, Qext_back=self.Qexternal_back, **self.kwargs)
            the_solver.solve()
            self.soln_space[n] = the_solver.get_solution()
            default_values = {'Qexternal': Qexternal, 'Ef': the_solver.Ef}
            defect_values = the_solver.get_defect_densities(self.soln_space[n], the_solver.Ef, integrated=True)
            self.fom.evaluate_location(n, {**default_values, **defect_values})
        except:
            traceback.print_exc()
            print(f"Solver failed at Qexternal = {Qexternal:0.0e}")

    def plot_solve(self, Qclose, level):
        n = np.argmin(np.abs(self.Qspace - Qclose))
        Qexternal = self.Qspace[n]
        hold = self.solver_class
        self.solver_class = plotter(self.solver_class, level=level)
        if self.dry_run:
            print(f"Plotting with level {level} and solving with {type(self.solver_class)}.\nPassing {self.kwargs}."
                  f"\nOur z_mesh:\n{self.z_mesh}\n It has a length of {len(self.z_mesh)} and we will need "
                  f"{len(self.z_mesh)**2*8e-9:0.0f}Gb of memory per diamond.\n Qexternal: {Qexternal}")
            print("FOM row definitions: ")
            self.fom.print_row_statements()
            return
        plt.ion()
        self.__solve_single__(n, Qexternal)
        plt.ioff()
        self.solver_class = hold

    def save_and_data_and_settings(self):
        # Grab all the settings and dump all settings to a json file
        # (duplicates automatically get eaten up by the {**dict, **dict})
        settings_to_append = {}
        for obj in [self, self.fom, self.defects]:
            settings_dict = obj.save_jsoncache(dump_to_file=False)
            if settings_dict is not None:
                settings_to_append = {**settings_to_append, **settings_dict}
            else:
                # TODO log as warning
                print(f"{type(obj)} did not return any settings to dump to json dict!!!")
        # we dump from the temp_solve_class so the filename contains the solver type used.
        self.temp_solver_class.save_jsoncache(dump_to_file=True, dict_to_append=settings_to_append)

        # Save the data to well named files
        if self.overwrite_file is None:
            dateid = datetime.datetime.now().strftime(f'%Y%m%d_{self.solver_class._settings_heading_}')
            qrange = f'Q_{self.Qspace[0]:0.0E}_{self.Qspace[-1]:0.0E}_{len(self.Qspace):d}'.replace('+', '').replace('-',
                                                                                                                     '')
            datafile = Path(self.local_dir) / (dateid + "_solution_space_" + qrange + '.txt')
            fomfile = Path(self.local_dir) / (dateid + "_FOM_" + qrange + '.txt')
            n = 1
            while datafile.exists():
                datafile = Path(self.local_dir) / (dateid + "_solution_space_" + qrange + f'_{n}' + '.txt')
                fomfile = Path(self.local_dir) / (dateid + "_FOM_" + qrange + f'_{n}' + '.txt')
                n += 1
        else:
            datafile = self.overwrite_file
            fomfile = Path(self.local_dir) / self.overwrite_file.name.replace("solution_space", "FOM")

        np.savetxt(datafile, np.vstack((self.z_mesh, self.soln_space)).T, header=make_data_comments(self.Qspace))
        self.fom.save_fom_to_file(fomfile)



    def z_mesh_auto(self):
        # First, we go through each defect and create a pchip spline for total maximum donor and acceptor densities.
        uniformZ = np.linspace(0, self.settings['diamond_thickness'], num=self.settings['z_mesh_maxpoints'])
        donors = np.zeros(len(uniformZ))
        acceptors = np.zeros(len(uniformZ))
        for name, defect in self.defects.defect_dict:
            if "density_file" in defect: #TODO: Implement this
                # Load in the SRIM/CTRIM data and form a spline interpolant from it. Spit out a warning if file not found
                if "donor_energy" in defect:
                    # add to donors 'mesh'
                    pass
                if "acceptor_energy" in defect:
                    # add to acceptors 'mesh'
                    pass
                pass
            elif "density_ranges" and "defect_densities" in defect: # Create spline interpolants from the provided density ranges and defect densities
                # Check for appropriate length
                if len(defect['density_ranges']) is not len(defect['defect_densities']):
                    IOError('Number of provided density ranges does not match number of provided densities for the defect called: {}'.format(name))
                if "donor_energy" in defect:
                    # add to donors 'mesh'
                    for range, density in (defect['density_ranges'], defect['defect_densities']):
                        if range[1] > self.settings['diamond_thickness']:
                            range[1] = self.settings['diamond_thickness']
                        rangeOfZ = (uniformZ >= range[0]) and (uniformZ <= range[1])
                        donors[rangeOfZ] = donors[rangeOfZ] + density
                if "acceptor_energy" in defect:
                    # add to acceptors 'mesh'
                    for range, density in (defect['density_ranges'], defect['defect_densities']):
                        if range[1] > self.settings['diamond_thickness']:
                            range[1] = self.settings['diamond_thickness']
                        rangeOfZ = (uniformZ >= range[0]) and (uniformZ <= range[1])
                        acceptors[rangeOfZ] = acceptors[rangeOfZ] + density
            else:
                UserWarning('Neither a density file nor manual density ranges and defect densities have been specified. Skipping the defect called: {}'.format(name))
                pass
        maxiondensity = np.abs(donors-acceptors)
        maxiondensity = gaussian_filter1d(maxiondensity, 0.005*self.settings['z_mesh_maxpoints'], mode='constant', cval=1e20, truncate=4)
       # densitySpline = pchip(uniformZ, maxiondensity, extrapolate=False)
        z_mesh = solve_meshing_problem(maxiondensity, uniformZ, self.settings['diamond_thickness'], self.settings['z_mesh_maxpoints'])
        return z_mesh

    def z_mesh_from_def(self):
        z_mesh_definition = self.settings['z_mesh_definition']
        shape = np.shape(z_mesh_definition)
        # Single range
        if shape == (3,):
            # Mesh unlikely to be >1cm in spacing, assume its a linspace.
            if type(z_mesh_definition[2]) is int:
                return np.linspace(*z_mesh_definition, endpoint=True)
            return np.arange(*z_mesh_definition)
        # List of ranges
        if shape[1] == 3:
            z_mesh = np.array([])
            for single_range in z_mesh_definition:
                if type(single_range[2]) is int:
                    z_mesh = np.append(z_mesh, np.linspace(*single_range, endpoint=False))
                else:
                    z_mesh = np.append(z_mesh, np.arange(*single_range))
            return np.array(z_mesh)
        raise NotImplementedError(f"Unsure how build a z_mesh from {z_mesh_definition}")


# fname = datetime.datetime.now().strftime(f'%Y%m%d_%H%M.%S_{self._settings_heading_}_settings.jsonlock')

class FiguresOfMerit(SettingsObject):
    _settings_heading_ = "FiguresOfMerit"
    default_settings = {'row0': 'Qexternal', 'row1': 'Ef', 'row2': '', 'row3': ''}
    default_variable_names = ['Qexternal', 'Ef']

    def __init__(self, defect_names, length, **kwargs):
        super().__init__(**kwargs)
        self.__add_default_settings__(FiguresOfMerit, **kwargs)

        self.all_variable_names = [] + self.default_variable_names + [name + '--' for name in defect_names] + [
            name + '++' for name in defect_names] + [name + '-' for name in defect_names] \
                                  + [name + '+' for name in defect_names] + defect_names
        self.all_variable_names.sort(key=len, reverse=True)

        # parse_rows
        self.rows = []
        n = 0
        n_blank = 0
        self.header = ''
        adjust = 2
        while f"row{n}" in self.settings:
            if self.settings[f"row{n}"]:
                self.rows.append(self.parse_fom_instruction(self.settings[f"row{n}"], n))
                self.header += self.settings[f"row{n}"] + ' '*(25-len(self.settings[f"row{n}"]) - adjust)
                adjust = 0
            else:
                n_blank += 1
            n += 1

        # build fom data
        self.data = np.zeros((length, n - n_blank))

    def save_fom_to_file(self, file_name):
        # Find the file we are going to save at.
        file = Path(self.settings['local_dir']) / file_name
        if file.exists():
            # TODO log as warning
            print(f'Figures of merit file {file} already exists, overwriting.')
        np.savetxt(file, self.data, header=self.header)

    def parse_fom_instruction(self, string, n=None):
        characters = string.split(' ')
        for idx, char in enumerate(characters):
            if char in white_list_operators:
                pass
            elif char in self.all_variable_names:
                characters[idx] = f"values_dict['{char}']"
            else:
                try:
                    characters[idx] = str(int_float(char))
                except ValueError:
                    raise ValueError(
                        f"Illegal operator character {char} or unknown variable in figures of merit row {n} "
                        f"definition -> {string}")
        return "".join(characters)

    def evaluate_location(self, location, values_dict):
        for n, row in enumerate(self.rows):
            self.data[location][n] = eval(row)

    def set_column(self, column, values):
        self.data.T[column] = values

    def print_row_statements(self):
        for row in self.rows:
            print(row)
