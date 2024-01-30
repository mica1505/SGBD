class ColInfo : 
    def __init__(self, nomColonne, typecolonne):
        """
        Initialise une colonne de la table
        """
        self.types = ["INT","FLOAT","STRING(T)","VARSTRING(T)"]
        self.nomColonne = nomColonne
        self.typeColonne = typecolonne #(TYPE DE LA COLONNE,TAILLE DU TYPE)

    def __str__(self):
        """
        Retourne sous forme de chaîne de caractères les attributs de ColInfo
        """
        return ""+self.nomColonne+":"+self.typeColonne[0] +" "+str(self.typeColonne[1])