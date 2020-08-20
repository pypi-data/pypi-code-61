# Copyright 2016-2019 Markus Scheidgen, Markus Kühbach
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


class APTFIMParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/aptfim', code_name='mpes', code_homepage='https://github.com/mpes-kit/mpes',
            domain='ems', mainfile_mime_re=r'(application/json)|(text/.*)', mainfile_name_re=(r'.*.aptfim')
        )

    def parse(self, filepath, archive, logger=None):
        with open(filepath, 'rt') as f:
            data = json.load(f)

        section_experiment = archive.m_create(SectionExperiment)

        # Read general tool environment details
        section_experiment.experiment_location = data.get('experiment_location')
        section_experiment.experiment_facility_institution = data.get('experiment_facility_institution')
        section_experiment.experiment_summary = '%s of %s.' % (data.get('experiment_method').capitalize(), data.get('specimen_description'))
        try:
            section_experiment.experiment_time = int(datetime.strptime(data.get('experiment_date_global_start'), '%d.%m.%Y %M:%H:%S').timestamp())
        except ValueError:
            pass
        try:
            section_experiment.experiment_end_time = int(datetime.strptime(data.get('experiment_date_global_end'), '%d.%m.%Y %M:%H:%S').timestamp())
        except ValueError:
            pass

        # Read data parameters
        section_data = section_experiment.m_create(SectionData)
        section_data.data_repository_name = data.get('data_repository_name')
        section_data.data_preview_url = data.get('data_repository_url')
        preview_url = data.get('data_preview_url')
        # TODO: This a little hack to correct the preview url and should be removed
        # after urls are corrected
        preview_url = '%s/files/%s' % tuple(preview_url.rsplit('/', 1))
        section_data.data_preview_url = preview_url

        # Read parameters related to method
        section_method = section_experiment.m_create(SectionMethod)
        section_method.experiment_method_name = data.get('experiment_method')
        section_method.experiment_method_abbreviation = 'APT/FIM'
        section_method.probing_method = 'electric pulsing'
        # backend.addValue('experiment_tool_info', data.get('instrument_info')) ###test here the case that input.json keyword is different to output.json
        # measured_pulse_voltage for instance should be a conditional read
        # backend.addValue('measured_number_ions_evaporated', data.get('measured_number_ions_evaporated'))
        # backend.addValue('measured_detector_hit_pos', data.get('measured_detector_hit_pos'))
        # backend.addValue('measured_detector_hit_mult', data.get('measured_detector_hit_mult'))
        # backend.addValue('measured_detector_dead_pulses', data.get('measured_detector_dead_pulses'))
        # backend.addValue('measured_time_of_flight', data.get('measured_time_of_flight'))
        # backend.addValue('measured_standing_voltage', data.get('measured_standing_voltage'))
        # backend.addValue('measured_pulse_voltage', data.get('measured_pulse_voltage'))
        # backend.addValue('experiment_operation_method', data.get('experiment_operation_method'))
        # backend.addValue('experiment_imaging_method', data.get('experiment_imaging_method'))

        # Read parameters related to sample
        section_sample = section_experiment.m_create(SectionSample)
        section_sample.sample_description = data.get('specimen_description')
        section_sample.sample_microstructure = data.get('specimen_microstructure')
        section_sample.sample_constituents = data.get('specimen_constitution')
        atom_labels = data.get('specimen_chemistry')
        formula = ase.Atoms(atom_labels).get_chemical_formula()
        section_sample.sample_atom_labels = np.array(atom_labels)
        section_sample.sample_chemical_formula = formula
