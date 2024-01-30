from TableInfo import TableInfo
from ColInfo import ColInfo

class CreateTableCommand:

    def __init__(self,chaineCommande,db):
        """
        Initialise une instance de la classe CreateTableCommand qui permet de créer une table dans la BDD
        """
        self.db = db
        self.commande = chaineCommande
        self.nomRelation,self.nbColonne,self.colInfos = self.parseCommandeCreateTable(chaineCommande)
    
    def parseCommandeCreateTable(self,string):
        """
        Séparation de la chaîne de commande pour extraire les informations nécessaires
        """
        args = string[12:len(string)-1]#extraction des arguments de la commande
        nomRelation = (args.split('(')[0]).strip()#extraction de la relation
        cols = args.split(nomRelation+' (')[1].split(',')#extraction des colonnes de la table
        listCols = []

        for c in cols:#boucle pour traiter chaque colonnes
            nomCol = c.split(':')[0]
            typeCol = c.split(':')[1]
            if "VARSTRING" in typeCol:
                typeCol = ("VARSTRING(T)", int(typeCol.split("(")[1][:-1]))
            if "STRING" in typeCol:
                typeCol = ("STRING(T)", int(typeCol.split("(")[1][:-1]))
            if "INT" in typeCol:
                typeCol = ("INT", 4)
            if "FLOAT" in typeCol:
                typeCol = ("FLOAT", 4)

            listCols.append(ColInfo(nomCol.strip(),typeCol))
        return nomRelation,len(listCols),listCols
    
    def Execute(self)->None:
        #instanciation d'un headerPage et d'une  et ajour de la tableInfo à la BDD
        headerPage = self.db.file_manager.createNewHeaderPage()
        relation = TableInfo(self.nomRelation,self.nbColonne,self.colInfos,headerPage)
        self.db.data_base_info.AddTableInfo(relation)

        
        return
    

    #CREATE TABLE NomRelation (NomCol_1:TypeCol_1,NomCol_2:TypeCol_2,NomCol_NbCol:TypeCol_NbCol)
        