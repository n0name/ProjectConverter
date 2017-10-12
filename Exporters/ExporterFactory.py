"""
Factory that creates the proper exporter based on file extension
"""

import os
from Exporters.XCodeExporter import XCodeExporter

_EXPORTER_MAPPING = {
    ".xcodeproj": XCodeExporter
}


def get_exporter(file_name):
    ext = os.path.splitext(file_name)[1]
    return _EXPORTER_MAPPING.get(ext, None)
