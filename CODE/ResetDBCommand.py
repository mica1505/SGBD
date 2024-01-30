import BufferManager
import DataBaseInfo
import DiskManager

class ResetDBCommand():
    def __init__(self,bdd):
        """
        Initialise une instance de la classe ResetDBCommand
        """
        self.bdd = bdd
        self.diskManager = bdd.disk_manager
        self.bufferManager = bdd.buffer_manager
        self.databaseInfo = bdd.data_base_info

    def Execute(self):
        """
        Réinitialise la BDD en réinitialisant le diskManager, le bufferManager et dataBaseInfo
        """
        self.diskManager.reset()
        self.bufferManager.reset()
        self.databaseInfo.reset()
        for i in range(4):
            with open(self.bdd.DBParams.DBPath+'F'+str(i)+'.data', 'w'):
                pass
        
        
        