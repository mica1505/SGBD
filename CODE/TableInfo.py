from PageId import PageId

class TableInfo :
    def __init__(self,nomRelation,nbColonnes,cols,headerPageId : PageId):
        """
        Initialise une instance de la classe de TableInfo
        """
        self.nomRelation = nomRelation
        self.nbColonne : int = nbColonnes
        self.cols : list = cols
        self.headerPageId = headerPageId #PageId

    def __str__(self):
        """
        Retourne sous forme de chaîne de caractères les attributs de la table
        """
        res = f"Table {self.nomRelation} with"
        for c in self.cols :
            res += "\t" + c.nomColonne
        return res
    
    def save(self):
        """
        Enregistre les informations de la table sous forme de chaîne de caractères
        """
        res = str(self.nomRelation) + " " + str(self.nbColonne) + " " + str(self.headerPageId.FileIdx) + " " + str(self.headerPageId.PageIdx) + " "
        for c in self.cols :
            res+= c.__str__()+" "
        res+="\n" 
        return res
