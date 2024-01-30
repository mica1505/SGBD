from TableInfo import TableInfo
from PageId import *
from ColInfo import *
import pickle

class DataBaseInfo :
    def __init__(self, db):
        """
        Initialise une instance de la classe DataBaseInfo
        """
        self.db=db
        self.tableInfo : list = [] #toute sles relations de notre BDD
        #pas besoin de compteur size
        #pas besoin d'initialiser un compteur, on retourne jujste la taille du tableau
    def reset(self):
        """
        Réinitialise les informations de la table
        """
        self.tableInfo = []
        
    def Init(self) -> None :
        '''
        init lit un fichier et recupere  les definitions des tables    
        
        '''
        with open (self.db.DBParams.DBPath+'DBInfo.save','r') as f1:
            for f in f1:
                param = f.split(" ")
                nomRelation = param[0]
                nbColonnes = int(param[1])
                headerPageId = PageId(int(param[2]), int(param[3]))
                cols = []
                for c in range(4, nbColonnes*2+3, 2):
                    cols.append(ColInfo(param[c].split(":")[0], (param[c].split(":")[1], int(param[c+1]))))
                self.tableInfo.append(TableInfo(nomRelation, nbColonnes, cols, headerPageId))

    
    
    def Finish(self) -> None:
        '''
        enregistre les definitions des tables
        '''
        with open (self.db.DBParams.DBPath+'DBInfo.save','w') as f1:
            for tb in self.tableInfo:
                f1.write(tb.save())

    def getNbRelations(self) -> int:
        """
        Renvoie le nombre de relations
        """
        return len(self.tableInfo)
    
    def AddTableInfo(self, TableInfo : TableInfo) -> None:
        """
        Ajoute les informations d'une nouvelle table à la liste
        """
        self.tableInfo.append(TableInfo)
    
    def GetTableInfo(self, nomRelation) -> TableInfo:
        """
        Récupère les informations d'une table spécifiée par son nom
        """
        table = None
        for i in self.tableInfo : 
            if i.nomRelation == nomRelation :
                table = i
        return table
    
    def __str__(self):
        """
        Retourne sous forme de chaîne de caractère la liste des tables
        """
        res = ""
        for t in self.tableInfo:
            res+=("\n"+t.__str__())
        return res