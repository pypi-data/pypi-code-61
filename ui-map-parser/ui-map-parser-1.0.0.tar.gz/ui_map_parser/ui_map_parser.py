# -*- coding: utf-8 -*-

__author__ = 'f1ashhimself@gmail.com'

from typing import Dict, Tuple
from os import path, listdir
from configparser import ConfigParser
from collections import OrderedDict


class UIMapException(Exception):
    """
    UI Map exception.
    """


class UIMapParser:
    """
    Parser for ui map storage.

    Args:
        ui_map_folder: path to folder that contains ini files.
        default_page: name of default page that will be used if "." will not be in element name.
        language: language name that will be used when constructing selector.
    """

    def __init__(self, ui_map_folder: str, default_page: str = 'common', language: str = None):
        self._ui_map_folder = ui_map_folder
        self._default_page = default_page
        self._language = language

    def parse_element(self, element_name: str, template: Dict[str, str] = None) -> Tuple[str, str]:
        """
        Parse element.

        Args:
            element_name: name of element that should be parsed, if name contains "." then first part of name will be
                used as file name and second as element name.
            template: template that show what replacements should be done e.g. {'some_text': 'text123'} will transform
                selector "//div[text()='%some_text%']" to "//div[text()='text123']".
        """
        parser = ConfigParser()
        splitted_name = element_name.split('.', 1)
        if len(splitted_name) == 1:
            splitted_name = [self._default_page] + splitted_name
        file_name, name = [part.lower() for part in splitted_name]
        ui_map_folder_files = {f.lower()[:-4]: f for f in listdir(self._ui_map_folder) if f.lower().endswith('.ini')}
        if file_name not in ui_map_folder_files:
            raise UIMapException(f'File "{file_name}" was not found.')

        parser.read(path.join(self._ui_map_folder, ui_map_folder_files[file_name]), encoding='utf-8')
        lowered_sections = OrderedDict()
        for section_name, section_data in parser._sections.items():
            lowered_sections[section_name.lower()] = section_data
        parser._sections = lowered_sections
        if not parser.has_section(name):
            raise UIMapException(f'Element "{element_name}" was not found.')

        el_type = parser.get(name, 'type')
        el_selector = parser.get(name, 'selector')
        if self._language and parser.has_option(name, self._language):
            el_selector += parser.get(name, self._language)

        if parser.has_option(name, 'parent'):
            parent_el_name = parser.get(name, 'parent')
            parent_el_type, parent_el_selector = self.parse_element(parent_el_name)
            if parent_el_type != el_type:
                raise UIMapException(f'"{element_name}" element and "{parent_el_name}" element have different element '
                                     f'types.')
            el_selector = parent_el_selector + el_selector

        if template:
            for k, v in template.items():
                el_selector = el_selector.replace('%%%s%%' % k, v)

        return el_type, el_selector
