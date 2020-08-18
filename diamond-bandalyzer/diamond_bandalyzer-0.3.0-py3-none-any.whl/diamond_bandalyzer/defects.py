"""A class that loads and parses diamond electronic defects to be included when solving for the band structure."""

__author__ = "Nikolai Dontschuk and Dan McCloskey"
__copyright__ = "Copyright 2020, Nikolai Dontschuk and Dan McCloskey"
__license__ = "Licensed under the Academic Free License version 3.0"

import numpy as np
from scipy.interpolate import interp1d
from scipy.integrate import trapz
from scipy.special import expit
from scipy.interpolate import CubicSpline
from diamond_bandalyzer.settingsobject import SettingsObject, config_folder, config_parser_args
import diamond_bandalyzer.fundementalconstants as fc
from configparser import ConfigParser, NoSectionError, NoOptionError
from pathlib import Path
from diamond_bandalyzer.utilities import ini_string_to_python


if not config_folder.exists():
    print(f"Could'nt find .config folder!")

defect_library = config_folder / "defect_library.ini"
library_parser = ConfigParser(**config_parser_args)

# make sure we have a default settings file
if not defect_library.exists():
    print(f"Could'nt find {str(defect_library)}, only user defined defects can be used!")
else:
    with open(defect_library) as f:
        library_parser.read_file(f)


def energies_from_library(name):
    donor_energy = library_parser.getfloat(name, 'donor_energy')
    acceptor_energy = library_parser.getfloat(name, 'acceptor_energy')
    return {'donor_energy': donor_energy, 'acceptor_energy': acceptor_energy}


def parse_defect_addition(name, donor_energy=None, acceptor_energy=None, density_file=None, density_ranges=None,
                          defect_densities=None):
    if donor_energy is None and acceptor_energy is None:
        try:
            default_energies = energies_from_library(name)
        except NoSectionError:
            # TODO log as warning.
            print(f"Warning: defect '{name}' has neither donor, nor acceptor transition energies defined in defects.ini"
                  f"or in default defects library and will be ignored.")
            return
        else:
            donor_energy = default_energies['donor_energy']
            acceptor_energy = default_energies['acceptor_energy']

    if density_file is None and defect_densities is None:
        # TODO log as warning.
        print(f"Warning: defect '{name}' has neither file nor array density definition in defects.ini and will be "
              f"ignored.")
        return

    if density_file is None:
        density_ranges = np.array(density_ranges)
        if len(density_ranges.shape) == 1:
            density_ranges = np.array([density_ranges])
        if not np.shape(defect_densities):
            defect_densities = np.array([defect_densities])
        if len(defect_densities) != density_ranges.shape[0]:
            if len(defect_densities) > 1:
                print(f"Warning: Cannot determined desired defect box density for {name} as number of ranges doesnt "
                      "match with multiple provided densities.  This defect will be ignored")
                return
            else:
                print(f"Warning: One density for {name} provided, assuming every range has same density.")
                defect_densities = np.repeat(defect_densities, density_ranges.shape[0])

    for n, d_range in enumerate(density_ranges):
        density_ranges[n] = np.array([np.min(d_range), np.max(d_range)])
    parsed_defect_dict = {}
    for p_name, param in zip(['donor_energy', 'acceptor_energy', 'density_file', 'density_ranges',
                              'defect_densities'],
                             [donor_energy, acceptor_energy, density_file, density_ranges,
                              defect_densities]):
        if param is not None:
            parsed_defect_dict[p_name] = param

    return parsed_defect_dict


class Defects(SettingsObject):
    _settings_heading_ = "DefectDefinition"
    default_settings = {'density_file_comments': '#', 'temperature_k': 300, 'top_sp2_defect_density': 1e13,
                        'back_sp2_defect_density': 1e13,
                        'sp2_defect_full_width': 0.6, 'sp2_defect_energy': 1.5,
                        'sp2_convolution_v_linspace': [-5.4, 5.4, 10000],
                        'sp2_convolution_variable_bounds_multiplier': 7.6, 'sp2_convolution_variable_step': 0.01}

    def __init__(self, defects_ini=None, defect_dict=None, **kwargs):
        super().__init__(**kwargs)
        self.__add_default_settings__(Defects, **kwargs)

        self.kT = fc.k * self.settings['temperature_k']

        self.defect_dict = {}
        if defect_dict is not None:
            self.__unpack_defect_dict__(defect_dict)
        self.__generate_sp2_spline__()

        if defects_ini is not None:
            try:
                self.add_defects_from_ini(defects_ini)
            except FileNotFoundError:
                # TODO log as warning
                print(f"defects.ini not found at {defects_ini.absolute()}")

        if 'local_dir' in self.settings:
            init_path = Path(self.settings['local_dir']) / 'defects.ini'
        else:
            init_path = Path('defects.ini')
        try:
            self.add_defects_from_ini(init_path)
        except FileNotFoundError:
            # TODO log as warning
            print(f"defects.ini not found at {init_path.absolute()}")

    def __unpack_defect_dict__(self, defect_dict):
        if defect_dict is None:
            return
        for name, this_defect_dict in defect_dict.items():
            self.add_defect(name, **this_defect_dict)
            # self.defects[name] = {'E': E, 'N': N, 'donor': bool(donor), 'bulk': bool(bulk)}

    def add_defects_from_ini(self, ini_file):
        """Adds defects to the solver from an ini_file.  This need not be called directly, and the solver will
        search for a defects.ini upon instansation.  Use this function if a differently named ini file is to be used.

        The ini file syntax is section headings haveing the defect short name, and then the desired sections listed
        as options. e.g.

        [NV]
        donor_energy=0.75 ; Optional, will look in defect library
        acceptor_energy=2.85
        density_file=ImplantProfileNV ; Either this or the other two must be specified.
        density_ranges=[[0,2],[0,3]]
        defect_densities=[1e15,1e10]

        A name and either a density file or density range and density must be provided."""
        ini_parser = ConfigParser(**config_parser_args)
        with open(ini_file, mode='r') as f:
            ini_parser.read_file(f)
        for name in ini_parser.sections():
            load = {}
            for option in ['donor_energy', 'acceptor_energy', 'density_file', 'density_ranges', 'defect_densities']:
                try:
                    load[option] = ini_string_to_python(ini_parser.get(name, option))
                except NoOptionError:
                    pass
            parsed_dict = parse_defect_addition(name, **load)
            if parsed_dict:
                if name in self.defect_dict:
                    # TODO log warning
                    print(f"Overwriting pre-existing definition for {name} with ini file definition.\n"
                          f"Original Definition:\n{self.defect_dict[name]}\n\n"
                          f"New Definition:\n{parsed_dict}")
                self.defect_dict[name] = parsed_dict

    def add_defect(self, name, donor_energy=None, acceptor_energy=None, density_file=None, density_ranges=None,
                   defect_densities=None):
        """Adds defects to the solver, this can be achieved in three ways. In recommended order.
         1. Define a defects.ini in the local directory or pass a differently names ini to add_defects_from_ini.  See
         the function description for required ini structure.

         2. At class instance creation by passing parameters in as a dict with this structure:
         {'name': {'donor_energy', 'acceptor_energy', 'density_file', 'density_ranges', 'defect_densities'}}

        3. Adding each defect individually via this function."""

        if name not in self.defect_dict:
            parsed_dict = parse_defect_addition(name, donor_energy, acceptor_energy, density_file,
                                                density_ranges, defect_densities)
            if parsed_dict:
                if name in self.defect_dict:
                    # TODO log warning
                    print(f"Overwriting pre-existing definition for {name} with function call definition."
                          f"Original Definition:\n{self.defect_dict[name]}\n\n"
                          f"New Definition:\n{parsed_dict}")
                self.defect_dict[name] = parsed_dict

    def get_defect_transition_energies_and_densities(self, z_mesh):
        defect_densities = np.zeros((len(self.defect_dict), len(z_mesh)))
        density_non_zeros = []
        donor_transitions = {}
        acceptor_transitions = {}

        for n, (name, this_defect_dict) in enumerate(self.defect_dict.items()):
            if 'density_file' in this_defect_dict:
                density_data = np.loadtxt('density_file', comments=self.settings['density_file_comments'])
                if density_data.shape[0] > density_data.shape[1]:
                    defect_densities[n] = interp1d(*density_data.T, bounds_error=False, fill_value=0)(z_mesh)
                else:
                    defect_densities[n] = interp1d(*density_data, bounds_error=False, fill_value=0)(z_mesh)
            else:
                for (lower, upper), density in zip(this_defect_dict['density_ranges'],
                                                   this_defect_dict['defect_densities']):
                    defect_densities[n][(z_mesh >= lower) & (z_mesh <= upper)] += density
                density_non_zeros.append(np.nonzero(defect_densities[n])[0])
            if 'acceptor_energy' in this_defect_dict:
                acceptor_transitions[name] = [this_defect_dict['acceptor_energy'], defect_densities[n],
                                              density_non_zeros[n]]
            if 'donor_energy' in this_defect_dict:
                donor_transitions[name] = [this_defect_dict['donor_energy'], defect_densities[n], density_non_zeros[n]]

        return defect_densities, density_non_zeros, donor_transitions, acceptor_transitions

    def __generate_sp2_spline__(self):
        fwhm = self.settings['sp2_defect_full_width']
        c = fwhm / (2 * np.sqrt(2 * np.log(2)))
        test_v = np.linspace(*self.settings['sp2_convolution_v_linspace']) / self.kT
        bound = fwhm * self.settings['sp2_convolution_variable_bounds_multiplier']
        energies = np.arange(-bound, bound, self.settings['sp2_convolution_variable_step'])
        y = np.zeros_like(test_v)
        for n, V in enumerate(test_v):
            y[n] = trapz(expit(energies / self.kT + V) * np.exp(-energies ** 2 / (2 * c ** 2)), energies)
        y = y / (np.sqrt(2 * np.pi) * c)
        self.sp2_spline = CubicSpline(test_v, y)
        self.sp2_spline_deriv = self.sp2_spline.derivative(1)

    def get_top_surface(self, Qexternal):
        return lambda x: Qexternal + self.settings['top_sp2_defect_density'] \
                         * self.sp2_spline(-self.settings['sp2_defect_energy'] / self.kT + x)

    def get_back_surface(self, Qexternal):
        return lambda x: Qexternal + self.settings['back_sp2_defect_density'] \
                         * self.sp2_spline(-self.settings['sp2_defect_energy'] / self.kT + x)

    def save_jsoncache(self, **kwargs):
        # Extend the save function to get our defect dict into the jsoncache file.
        self.settings['defect_dict'] = self.defect_dict
        return super().save_jsoncache(**kwargs)


    def get_top_surface_deriv(self):
        return lambda x: self.settings['top_sp2_defect_density'] \
                         * self.sp2_spline_deriv(-self.settings['sp2_defect_energy'] / self.kT + x)

    def get_back_surface_deriv(self):
        return lambda x: self.settings['back_sp2_defect_density'] \
                         * self.sp2_spline_deriv(-self.settings['sp2_defect_energy'] / self.kT + x)
