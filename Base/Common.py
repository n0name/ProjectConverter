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


class IIPR(object):
    """
        IDE Independent Project Representation
    """
    files = []
    parameters = {}
