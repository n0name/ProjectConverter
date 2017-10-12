"""
Exporter for XCode Projects
"""

from Base.Common import *
from Base.IProjectExporter import IProjectExporter


class XCodeExporter(IProjectExporter):
    def __init__(self, iipr):
        super().__init__(iipr)

    def export_to_file(self, file_name):
        pass
