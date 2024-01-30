from InsertCommand import InsertCommand
from Record import Record
class ImportCommand:
    def __init__(self,chaineCommande,bdd):
        """
        Initialise une instance de la classe ImportCommand
        """
        self.bdd = bdd
        self.commande = chaineCommande
        self.nomRelation,self.nomFichier = self.parseCommandeImport(chaineCommande)
        
    def parseCommandeImport(self,string):
        """
        Sépare la chaîne de commande d'importation pour extraire le nom de la relation et le nom du fichier
        """
        return string.split(" ")[2].strip(),string.split(" ")[3].strip()
    
    def Execute(self)->None:
        """
        Exécute la commande d'importation
        La méthode lit le fichier CSV spécifié et insère chaque ligne en tant que nouveau record dans la table correspondante de la BDD
        """ 
        insertion = InsertCommand("",self.bdd)
        insertion.nomRelation = self.nomRelation
        with  open("../"+self.nomFichier,"r") as fichier : 
            for ligne in fichier : 
                
                ligne = ligne.strip()
                relation = self.bdd.data_base_info.GetTableInfo(self.nomRelation)

                rec = Record(relation,ligne.split(","))
                insertion.values = rec

                insertion.Execute()
