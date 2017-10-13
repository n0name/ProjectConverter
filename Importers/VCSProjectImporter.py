"""
Visual Studio .vcproj importer
"""
import xml.etree.ElementTree as ET

from Base.Common import *

from Base.IProjectLoader import *


def _find_rec(node, element, result):
    for child in node:
        if element in child.tag:
            result.append(child)
        _find_rec(child, element, result)
    return result


class VCSProjectImporter(IProjectLoader):
    def __init__(self):
        self.project_name = ""
        self.iipr = None

    def load_project(self, file_name):
        self.project_name = file_name
        pass

    def _debug_print_node(self, node=None, tabs=0):
        if node is None:
            return
        for child in node:
            print('\t' * tabs, child.tag, child.attrib)
            self._debug_print_node(child, tabs + 1)

    def _debug_print_data(self):
        et = ET.parse(self.project_name)
        if et is None:
            return

        root = et.getroot()
        for child in root:
            print(child.tag, child.attrib)

    def _parse_sources(self, root):
        # Find all the source files
        for item in _find_rec(root, 'ClCompile', []):
            if 'Include' in item.attrib:
                file_name = item.attrib['Include']
                exclude_from = []
                for child in item:
                    if "ExcludedFromBuild" in child.tag:
                        exclude_from.append(child.attrib['Condition'])

                self.iipr.files.append(File(file_name, type='source', exclude_from=exclude_from))

    def _parse_headers(self, root):
        # Find all the include files
        for item in _find_rec(root, 'ClInclude', []):
            if 'Include' in item.attrib:
                self.iipr.files.append(File(item.attrib['Include'], type='include'))

    def _parse_configurations(self, root):
        # Find all the build configurations
        for item in _find_rec(root, 'ProjectConfiguration', []):
            if 'Include' in item.attrib:
                config_name = item.attrib['Include']
                params_dict = {}
                for child in item:
                    params_dict.update({child.tag: child.text})

                self.iipr.configurations.append(Configuration(config_name, **params_dict))

    def parse_data(self):
        et = ET.parse(self.project_name)
        if et is None:
            return False
        root = et.getroot()
        self.iipr = IIPR()

        self._parse_sources(root)
        self._parse_headers(root)
        self._parse_configurations(root)

        return True
