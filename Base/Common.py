"""
Models what a project looks like
"""


class File(object):
    """
        Represents a single file and it's attributes
    """

    def __init__(self, path, **kwargs):
        self.path = path
        self.attrib = kwargs


class Configuration(object):
    """
        Represents project configuration
    """
    def __init__(self, name, **kwargs):
        self.name = name
        self.params = kwargs


class IIPR(object):
    """
        IDE Independent Project Representation
    """
    configurations = []
    files = []
    parameters = {}
