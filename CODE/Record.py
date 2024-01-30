import TableInfo as TableInfo

class Record : 
    def __init__(self, tableInfo,recvalues):
        """
        Initialise une instance de la classe Record
        """
        #relation a laquelle appartient le record
        self.tabInfo : TableInfo = tableInfo
        #valeurs du record -> un tuple a n vlauers (nb de cols dans la relation)
        self.recvalues : list = recvalues

    def initTaille(self, indice):
        """
        Initialise la taille d'un champ du record
        """
        if(self.tabInfo.cols[indice].typeColonne[0] == "VARSTRING(T)"):
            return len(self.recvalues[indice])
        else :
            return self.tabInfo.cols[indice].typeColonne[1]
        
    def writeToBuffer(self, buff, pos) -> int : 
        """
        Ecrit le record dans le buffer à une position spécifique
        """
        nbColonnes = len(self.recvalues)

        buff.set_position(pos)

        buff.put_int(self.initTaille(0))
        taille = self.initTaille(0)
        for j in range(1,nbColonnes):
            taille += self.initTaille(j)
            buff.put_int(taille)

        for i in range(nbColonnes):
            match self.tabInfo.cols[i].typeColonne[0] :
                case "INT": 
                    val = int(self.recvalues[i])
                    buff.put_int(val)

                case "FLOAT" : 
                    buff.put_float(float(self.recvalues[i]))

                case "VARSTRING(T)": 
                    if(len(self.recvalues[i])>0):
                        for c in self.recvalues[i] :
                            buff.put_char(c)
                    else:
                        buff.put_char("N")
                        buff.put_char("O")
                        buff.put_char("N")
                        buff.put_char("E")

                case "STRING(T)" :
                    if len(self.recvalues[i])>0:
                        for c in self.recvalues[i] :
                            buff.put_char(c)
                            
        return taille #nb d'octets ecrits
    
    def readFromBuffer(self, buff, pos):
        """
        Lit le record depuis un buffer à une position spécifique et retourne la taille du record
        """
        tabTaille : list = []
        nbColonnes = len(self.tabInfo.cols)
        buff.set_position(pos)
        for i in range(nbColonnes):
            n=buff.read_int()
            tabTaille.append(n) 
        tailleRecord = tabTaille[-1]

        for i in range(nbColonnes):
            match self.tabInfo.cols[i].typeColonne[0] :
                case "INT": 
                    a = buff.read_int()
                    self.recvalues.append(a)
                    
                case "FLOAT" : 
                    b = buff.read_float()
                    self.recvalues.append(b)

                case "VARSTRING(T)" : 
                    self.recvalues.append(buff.read_char()) #faut trouver la longueur de la chaine de caracteres
                    for j in range(tabTaille[i]-tabTaille[i-1]-1 if i != 0 else tabTaille[i]-1):
                        self.recvalues[i]+=buff.read_char()
                    self.recvalues[i]=self.recvalues[i].strip() 

                case "STRING(T)" :
                    ch = ""
                    t=self.tabInfo.cols[i].typeColonne[1]
                    for j in range(t):
                        ch+=buff.read_char()

                    self.recvalues.append(ch)

                case _:
                    print("erreur")  
        
        return tailleRecord
    
    def getTailleRecord(self):
        """
        Retourne la taille du record
        """
        somme=0
        for i in range (len(self.recvalues)):            
            somme+=self.initTaille(i)
        return somme + 4*(len(self.recvalues))
    
    def __str__(self):
        """
        Retourne sous forme de chaîne de caractères le record
        """
        res = ""
        for i in self.recvalues :
            if i == self.recvalues[-1]:
                res += str(i)+ '.'
            else:
                 res += str(i)+ ' ; '

        return res
    
    def __eq__(self,rec):
        """
        Vérifie l'égalité entre 2 record
        """
        res = True
        if(rec==None):
            return False
        for c in range(len(self.recvalues)):
            if(rec.recvalues[c] != self.recvalues[c]):
                res = False
        return res
        