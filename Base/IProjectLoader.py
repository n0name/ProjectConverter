class IProjectLoader(object):
    """
        Interface for project Importers
    """

    def load_project(self, file_name):
        raise NotImplementedError()

    def parse_data(self):
        raise NotImplementedError()
