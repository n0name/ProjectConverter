"""
Exporter for AutoConf projects
"""

from Base.Common import *
from Base.IProjectExporter import IProjectExporter

_MakefileModel = """
MODULE    = {target}
IMPORTLIB = {imp_lib}
IMPORTS   = {imports}
EXTRADEFS = {defs}

C_SRCS = {sources}

IDL_SRCS = {idls}
"""


class AutoconfMakefileExporter(IProjectExporter):
    def __init__(self, iipr, name):
        super().__init__(iipr)
        self.name = name

    def _format_sources(self):
        def is_src(file):
            return "type" in file.attrib and file.attrib['type'] == 'source'

        return "\\\n\t''" + " \\\n\t".join(f.path for f in self.iipr.files if is_src(f))

    def _format_idls(self):
        return ""

    def export_to_file(self, file_name):
        sources = self._format_sources()
        idls = self._format_idls()

        output_srt = _MakefileModel.format(sources=sources,
                                           idls=idls,
                                           target="{}.dll".format(self.name),
                                           imp_lib=self.name,
                                           imports="",
                                           defs="")

        with open(file_name, 'w') as makefile:
            makefile.write(output_srt)
