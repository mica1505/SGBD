class DeleteCommand:
    def __init__(self,chaineCommande):
        """
        Initialise une instance de la classe DeleteCommand
        """
        self.commande = chaineCommande
        self.nomRelation,self.operations = self.parseCommandeDelete(chaineCommande)
    #DELETE FROM nomRelation WHERE nomColonne1OPvaleur1 nomColonne2OPvaleur2 AND nomColonnekOPvaleurk 
    def parseCommandeDelete(string):
        """
        Sépare les arguments de la commande DELETE et extrait le nom de la relation et les opération de condition
        """
        condition = string.split("WHERE")[1].strip()
        operations = condition.split(" ")
        operations[-1] = operations.pop(-1)

        
        nomRelation = string.split(" ")[2].strip()

        return nomRelation,operations
    
    def parseOperation(self,op):#> < = >= <=
        """
        Sépare l'opérateur de comparaison de l'operation de condition
        """
        operationsSolo= ['>','<','=']
        operationsDuo = [">=","<="]
        
        for c in operationsDuo:
            if c in op:
                return c
        
        for c in operationsSolo:
            if c in op:
                return c
    
    def Execute(self):
        """
        Exécute la commande DELETE
        """
        return 
