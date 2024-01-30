
from DiskManager import DiskManager
from BufferManager import BufferManager
from DBParams import DBParams
from DataBaseInfo import DataBaseInfo
from DataBaseInfo import DataBaseInfo
from FileManager import FileManager

class BDD:
    #Chaque attribut prend la BDD (self) en parametre
    def __init__(self, DBParams):
        """
        Initialise une instance de la classe BDD
        """
        self.DBParams = DBParams
        self.disk_manager = DiskManager(self)
        self.buffer_manager = BufferManager(self)
        self.data_base_info = DataBaseInfo(self)
        self.dataBaseInfo = DataBaseInfo(self)
        self.file_manager = FileManager(self)
    

