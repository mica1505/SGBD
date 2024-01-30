class PageId :
    def __init__(self, FileIdx = -1,PageIdx= -1, ):
        """
        Initialise une instance de la classe PageId
        """
        self.FileIdx = FileIdx
        self.PageIdx = PageIdx

    def isValid(self):
        """
        Vérifie si l'identifiant de la page est valide
        """
        return self.FileIdx!=-1
    
    def __str__(self):
        """
        Retourne sous forme de chaîne de caractère les attributs de PageId
        """
        return "FileId : "+ str(self.FileIdx) + " PageId " +str(self.PageIdx)
    
    def __eq__(self,pId):
        """
        Vérifie l'égalité entre 2 PageId
        """
        if pId == None:
            return False
        return self.PageIdx == pId.PageIdx and self.FileIdx == pId.FileIdx
