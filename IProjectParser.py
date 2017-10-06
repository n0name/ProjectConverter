"""
Models what a project looks like
and general methods for loading/parsing
"""


class File(object):
    """
        Represents a single file and it's attributes
    """

    def __init__(self, path, **kwargs):
        self.path = path
        self.attrib = kwargs


class IIPR(object):
    """
        IDE Independent Project Representation
    """
    files = []
    parameters = {}


class IProjectParser(object):
    """
        Interface for project parsers
    """

    def load_project(self, file_name):
        raise NotImplementedError()

    def parse_data(self):
        raise NotImplementedError()
