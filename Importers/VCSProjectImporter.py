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

        self._debug_print_node(et.getroot())

    def parse_data(self):
        et = ET.parse(self.project_name)
        if et is None:
            return False
        root = et.getroot()
        iipr = IIPR()
        for item in _find_rec(root, 'ClCompile', []):
            if 'Include' in item.attrib:
                iipr.files.append(File(item.attrib['Include'], type='source'))

        for item in _find_rec(root, 'ClInclude', []):
            if 'Include' in item.attrib:
                iipr.files.append(File(item.attrib['Include'], type='include'))

        self.iipr = iipr

        return True
