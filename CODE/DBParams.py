class DBParams:

    def __init__(self, DBPath, SGBDPageSize, DMFileCount, frameCount):
        """
        Initialise une instance de la classe DBParams avec les paramètres spécifiés
        """
        self.DBPath = DBPath
        self.SGBDPageSize = SGBDPageSize
        self.DMFileCount = DMFileCount
        self.frameCount = frameCount