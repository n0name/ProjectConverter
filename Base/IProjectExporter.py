class IProjectExporter(object):
    """
    Interface for project Exporter
    """

    def __init__(self, iipr):
        self.iipr = iipr

    def export_to_file(self, file_name):
        raise NotImplementedError()
