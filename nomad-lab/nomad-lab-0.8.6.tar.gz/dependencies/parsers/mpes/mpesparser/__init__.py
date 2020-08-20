# Copyright 2016-2018 Markus Scheidgen
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys
import os.path
import json
import ase
import re
import numpy as np
from datetime import datetime

from nomad.parsing.parser import FairdiParser
from nomad.datamodel.metainfo.general_experimental import section_experiment as SectionExperiment
from nomad.datamodel.metainfo.general_experimental import section_data as SectionData
from nomad.datamodel.metainfo.general_experimental_method import section_method as SectionMethod
from nomad.datamodel.metainfo.general_experimental_sample import section_sample as SectionSample


class MPESParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/mpes', code_name='mpes', code_homepage='https://github.com/mpes-kit/mpes',
            domain='ems', mainfile_mime_re=r'(application/json)|(text/.*)', mainfile_name_re=(r'.*.meta'),
            mainfile_contents_re=(r'"data_repository_name": "zenodo.org"')
        )

    def parse(self, filepath, archive, logger=None):
        with open(filepath, 'rt') as f:
            data = json.load(f)

        section_experiment = archive.m_create(SectionExperiment)

        # Read general experimental parameters
        # section_experiment.experiment_location = ', '.join(reversed(re.findall(r"[\w']+", data.get('experiment_location'))))
        section_experiment.experiment_location = data.get('experiment_location')
        start, end = data.get('experiment_date').split(' ')
        try:
            section_experiment.experiment_time = int(datetime.strptime(start, '%m.%Y').timestamp())
        except ValueError:
            pass
        try:
            section_experiment.experiment_end_time = int(datetime.strptime(end, '%m.%Y').timestamp())
        except ValueError:
            pass
        section_experiment.experiment_summary = data.get('experiment_summary')
        section_experiment.experiment_facility_institution = data.get('facility_institution')
        section_experiment.experiment_facility_name = data.get('facility_name')

        # Read data parameters
        section_data = section_experiment.m_create(SectionData)
        section_data.data_repository_name = data.get('data_repository_name')
        section_data.data_repository_url = data.get('data_repository_url')
        section_data.data_preview_url = 'preview.png'

        # Read method parameters
        section_method = section_experiment.m_create(SectionMethod)
        section_method.experiment_method_name = data.get('experiment_method')
        section_method.experiment_method_abbreviation = data.get('experiment_method_abbrv')
        section_method.equipment_description = data.get('equipment_description')
        section_method.probing_method = 'laser pulses'
        section_method.general_beamline = data.get('beamline')
        section_method.general_source_pump = data.get('source_pump')
        section_method.general_source_probe = data.get('source_probe')
        section_method.general_measurement_axis = np.array(re.findall(r"[\w']+", data.get('measurement_axis')))
        section_method.general_physical_axis = np.array(re.findall(r"[\w']+", data.get('physical_axis')))

        # Read parameters related to experimental source
        # source_gid = backend.openSection('section_experiment_source_parameters')
        section_method.source_pump_repetition_rate = data.get('pump_rep_rate')
        section_method.source_pump_pulse_duration = data.get('pump_pulse_duration')
        section_method.source_pump_wavelength = data.get('pump_wavelength')
        section_method.source_pump_spectrum = np.array(data.get('pump_spectrum'))
        section_method.source_pump_photon_energy = data.get('pump_photon_energy')
        section_method.source_pump_size = np.array(data.get('pump_size'))
        section_method.source_pump_fluence = np.array(data.get('pump_fluence'))
        section_method.source_pump_polarization = data.get('pump_polarization')
        section_method.source_pump_bunch = data.get('pump_bunch')
        section_method.source_probe_repetition_rate = data.get('probe_rep_rate')
        section_method.source_probe_pulse_duration = data.get('probe_pulse_duration')
        section_method.source_probe_wavelength = data.get('probe_wavelength')
        section_method.source_probe_spectrum = np.array(data.get('probe_spectrum'))
        section_method.source_probe_photon_energy = data.get('probe_photon_energy')
        section_method.source_probe_size = np.array(data.get('probe_size'))
        section_method.source_probe_fluence = np.array(data.get('probe_fluence'))
        section_method.source_probe_polarization = data.get('probe_polarization')
        section_method.source_probe_bunch = data.get('probe_bunch')
        section_method.source_temporal_resolution = data.get('temporal_resolution')

        # Read parameters related to detector
        # detector_gid = backend.openSection('section_experiment_detector_parameters')
        section_method.detector_extractor_voltage = data.get('extractor_voltage')
        section_method.detector_work_distance = data.get('work_distance')
        section_method.detector_lens_names = np.array(re.findall(r"[\w']+", data.get('lens_names')))
        section_method.detector_lens_voltages = np.array(data.get('lens_voltages'))
        section_method.detector_tof_distance = data.get('tof_distance')
        section_method.detector_tof_voltages = np.array(data.get('tof_voltages'))
        section_method.detector_sample_bias = data.get('sample_bias')
        section_method.detector_magnification = data.get('magnification')
        section_method.detector_voltages = np.array(data.get('detector_voltages'))
        section_method.detector_type = data.get('detector_type')
        section_method.detector_sensor_size = np.array(data.get('sensor_size'))
        section_method.detector_sensor_count = data.get('sensor_count')
        section_method.detector_sensor_pixel_size = np.array(data.get('sensor_pixel_size'))
        section_method.detector_calibration_x_to_momentum = np.array(data.get('calibration_x_to_momentum'))
        section_method.detector_calibration_y_to_momentum = np.array(data.get('calibration_y_to_momentum'))
        section_method.detector_calibration_tof_to_energy = np.array(data.get('calibration_tof_to_energy'))
        section_method.detector_calibration_stage_to_delay = np.array(data.get('calibration_stage_to_delay'))
        section_method.detector_calibration_other_converts = np.array(data.get('calibration_other_converts'))
        section_method.detector_momentum_resolution = np.array(data.get('momentum_resolution'))
        section_method.detector_spatial_resolution = np.array(data.get('spatial_resolution'))
        section_method.detector_energy_resolution = np.array(data.get('energy_resolution'))

        # Read parameters related to sample
        section_sample = section_experiment.m_create(SectionSample)
        section_sample.sample_description = data.get('sample_description')
        section_sample.sample_id = data.get('sample_id')
        section_sample.sample_state_of_matter = data.get('sample_state')
        section_sample.sample_purity = data.get('sample_purity')
        section_sample.sample_surface_termination = data.get('sample_surface_termination')
        section_sample.sample_layers = data.get('sample_layers')
        section_sample.sample_stacking_order = data.get('sample_stacking_order')
        section_sample.sample_space_group = data.get('sample_space_group')
        section_sample.sample_chemical_name = data.get('chemical_name')
        section_sample.sample_chemical_formula = data.get('chemical_formula')
        # backend.addArrayValues('sample_chemical_elements', np.array(re.findall(r"[\w']+", data.get('chemical_elements'))))
        atoms = set(ase.Atoms(data.get('chemical_formula')).get_chemical_symbols())
        section_sample.sample_atom_labels = np.array(list(atoms))
        section_sample.sample_chemical_id_cas = data.get('chemical_id_cas')
        section_sample.sample_temperature = data.get('sample_temperature')
        section_sample.sample_pressure = data.get('sample_pressure')
        section_sample.sample_growth_method = data.get('growth_method')
        section_sample.sample_preparation_method = data.get('preparation_method')
        section_sample.sample_vendor = data.get('sample_vendor')
        section_sample.sample_substrate_material = data.get('substrate_material')
        section_sample.sample_substrate_state_of_matter = data.get('substrate_state')
        section_sample.sample_substrate_vendor = data.get('substrate_vendor')

        # TODO sample classification
        section_sample.sample_microstructure = 'bulk sample, polycrystalline'
        section_sample.sample_constituents = 'multi phase'
