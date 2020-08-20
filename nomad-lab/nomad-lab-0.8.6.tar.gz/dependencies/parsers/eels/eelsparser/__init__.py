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
import numpy as np
from datetime import datetime
import time
import ast
import logging

from .metainfo import eels as meels
from nomad.datamodel.metainfo.general_experimental import section_experiment as SectionExperiment
from nomad.datamodel.metainfo.general_experimental import section_data as SectionData
from nomad.datamodel.metainfo.general_experimental_method import section_method as SectionMethod
from nomad.datamodel.metainfo.general_experimental_sample import section_sample as SectionSample
from nomad.parsing.parser import FairdiParser

from .hyper2json import transform as read_hyper


logger = logging.getLogger(__name__)


class EelsParser(FairdiParser):
    def __init__(self):
        super().__init__(
            name='parsers/eels', code_name='eels', code_homepage='https://eelsdb.eu/',
            domain='ems', mainfile_mime_re=r'text/.*', mainfile_name_re=(r'.*.txt'),
            mainfile_contents_re=(r'api_permalink = https://api\.eelsdb\.eu')
        )

    def parse(self, filepath, archive, logger=logger):
        try:
            data = read_hyper(filepath)
        except Exception as e:
            logger.error('could not read mainfile', exc_info=e)
            raise e

        section_experiment = archive.m_create(SectionExperiment)
        section_experiment.experiment_summary = 'EELS-Spectra'
        section_experiment.experiment_location = 'Earth'

        try:
            dt_string = data.get('published')
            dt_object = datetime.strptime(dt_string, "%Y-%m-%d %H:%M:%S")
            section_experiment.experiment_time = int(time.mktime(dt_object.timetuple()))
        except ValueError as e:
            logger.warn('Wrong time format in start time!', exc_info=e)
            dt_string = data.get('published')
            section_experiment.start_time = dt_string
        except Exception as e:
            logger.warn('Some error occured transforming the time.', exc_info=e)
            dt_string = data.get('published')
            section_experiment.start_time = dt_string

        section_experiment.spectrum_type = data.get('type')
        section_experiment.title = data.get('title')

        section_user = section_experiment.m_create(meels.section_user)
        section_user.username = data.get('author').get('name')
        section_user.profile_api_url = data.get('author').get('profile_api_url')
        section_user.profile_url = data.get('author').get('profile_url')

        section_method = section_experiment.m_create(SectionMethod)
        section_method.experiment_method_name = 'Electron Energy Loss Spectroscopy'
        section_method.probing_method = 'electrons'

        section_sample = section_experiment.m_create(SectionSample)
        section_sample.sample_atom_labels = np.asarray(ast.literal_eval(data.get('elements')))
        section_sample.sample_chemical_formula = data.get('formula')
        temp = data.get('probesize')
        # unfortunately necessary because not every dataset contains this information
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_sample.probe_size = float(temp1)
        section_sample.source_purity = data.get('source_purity')

        section_em = section_experiment.m_create(meels.section_em)
        section_em.name_em = data.get('microscope')
        section_em.gun_type = data.get('guntype')
        section_em.acquisition_mode = data.get('acquisition_mode')
        temp = data.get('convergence')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_em.convergence_semi_angle = float(temp1)
        temp = data.get('collection')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_em.collection_semi_angle = float(temp1)
        section_em.detector = data.get('detector')
        temp = data.get('integratetime')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_em.integration_time = float(temp1)
        temp = data.get('readouts')
        if temp is not None:
            section_em.readouts = int(temp)
        temp = data.get('darkcurrent')
        temp1 = False
        if temp is not None:
            if(temp == 'Yes'):
                temp1 = True
        section_em.dark_current_correction = temp1
        temp = data.get('gainvariation')
        temp1 = False
        if temp is not None:
            if(temp == 'Yes'):
                temp1 = True
        section_em.gain_variation_spectrum = temp1
        temp = data.get('thickness')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_em.relative_thickness = float(temp1)

        section_source1 = section_em.m_create(meels.section_source1)
        temp = data.get('beamenergy')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_source1.incident_energy = float(temp1)
        temp = data.get('resolution')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_source1.resolution = float(temp1)
        temp = data.get('stepSize')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_source1.dispersion = float(temp1)
        temp = data.get('monochromated')
        temp1 = False
        if temp is not None:
            if(temp == 'Yes'):
                temp1 = True
        section_source1.monochromated = temp1

        section_data = section_experiment.m_create(SectionData)
        section_data.id = int(data.get('id'))
        section_data.edges = data.get('edges')
        temp = data.get('min_energy')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_data.min_energy = float(temp1)
        temp = data.get('max_energy')
        if temp is not None:
            split = temp.find(' ')
            temp1 = temp[:split]
            section_data.max_energy = float(temp1)
        temp1 = data.get('description')
        for i in range(3):
            j = i + 1
            temp0 = 'additionalInformation' + str(j)
            temp = data.get(temp0)
            if temp is not None:
                temp1 = temp1 + ', ' + temp
        temp = data.get('keywords')
        if temp is not None:
            temp1 = temp1 + ', ' + temp
        section_data.description = temp1
        section_data.data_repository_name = 'EELS-DB'
        section_data.data_repository_url = data.get('download_link')
        section_data.data_preview_url = data.get('download_link')
        section_data.entry_repository_url = data.get('permalink')
        section_data.published = data.get('published')
        section_data.permalink = data.get('permalink')
        section_data.api_permalink = data.get('api_permalink')
        section_data.other_links = data.get('other_links')
        if data.get('comment_count') is not None:
            section_data.comment_count = int(data.get('comment_count'))
        section_data.associated_spectra = data.get('associated_spectra')
        tempref = data.get('reference')
        if tempref is not None:
            section_reference = section_data.m_create(meels.section_reference)
            section_reference.authors = tempref.get('authors')
            section_reference.doi = tempref.get('doi')
            section_reference.issue = tempref.get('issue')
            section_reference.journal = tempref.get('journal')
            section_reference.page = tempref.get('page')
            section_reference.title_ref = tempref.get('title')
            section_reference.url = tempref.get('url')
            section_reference.volume = tempref.get('volume')
            section_reference.year = tempref.get('year')
            temp1 = tempref.get('freetext')
            for i in range(2):
                j = i + 4
                temp0 = 'additionalInformation' + str(j)
                temp = tempref.get(temp0)
                if temp is not None:
                    temp1 = temp1 + ', ' + temp
            section_reference.freetext = temp1
