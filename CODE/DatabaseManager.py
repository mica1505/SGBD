from CreateTableCommand import CreateTableCommand
from ResetDBCommand import ResetDBCommand
from InsertCommand import InsertCommand
from SelectCommand import SelectCommand
from ImportCommand import ImportCommand
import pickle
import os
class DatabaseManager:

    def __init__(self,bdd):
        """
        Initialise une instance de la classe DataBaseManager
        """
        self.bdd=bdd
        self.diskManager = bdd.disk_manager
        self.bufferManager = bdd.buffer_manager
        self.databaseInfo = bdd.data_base_info

    def savedData(self):
        """
        Charge les informations de la BDD depuis un fichier
        """
        file = self.bdd.DBParams.DBPath+'DBInfo.save'
        if os.path.exists(file) and os.path.getsize(file) > 0:
            self.diskManager.Init()
            self.databaseInfo.Init()
        # print(self.databaseInfo)
        
    def Finish(self):
        """
        Termine l'utilisation de la BDD et effectue les opérations nécessaires
        """
        self.databaseInfo.Finish()
        self.bufferManager.FlushAll()
        self.diskManager.Finish()
        
        

    def createTable(self,cmd):
        """
        Vérifie si la commande est une commande CREATE TABLE
        """
        typeComande = cmd.split(' ')
        if typeComande[0] == "CREATE" and typeComande[1] == "TABLE":
            return True
        else :
            return False
        
    def insert(self,cmd):
        """
        Vérifie si la commande est une commande INSERT
        """
        typeComande = cmd.split(' ')
        if typeComande[0] == "INSERT":
            return True
        else :
            return False
        
    def select(self,cmd):
        """
        Vérifie si la commmande est une commande SELECT
        """
        typeComande = cmd.split(' ')
        if typeComande[0] == "SELECT":
            return True
        else :
            return False

    def reset(self,cmd):
        """
        Vérifie si la commande est une commande RESETDB
        """
        if cmd == "RESETDB":
            return True
        else :
            return False
        
    def imprt(self,cmd):
        """
        Vérifie si la commande est une commande IMPORT INTO
        """
        typeComande = cmd.split(' ')
        if typeComande[0] == "IMPORT" and typeComande[1] == "INTO":
            return True
        else :
            return False

    def ProcessCommand(self, cmd : str):
        """
        Traite une commande SQL en appelant les commandes appropriées en fonction du type de commande
        """
        if self.createTable(cmd):
            CreateTableCommand(cmd,self.bdd).Execute()

        if self.reset(cmd):
            ResetDBCommand(self.bdd).Execute()

        if self.insert(cmd):
            InsertCommand(cmd,self.bdd).Execute()

        if self.select(cmd):
            SelectCommand(cmd,self.bdd).Execute()

        if self.imprt(cmd):
            ImportCommand(cmd,self.bdd).Execute()
            