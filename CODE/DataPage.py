from PageId import PageId
class DataPage : 
    def __init__(self,buff):
        """
        Initialise une instance de la classe DataPage
        """
        self.buff = buff


    def initialisation(self):
        """
        Initialise une DataPage avec le nombre de slots et le début de l'espace libre
        """
        self.buff.set_position(4088)
        self.buff.put_int(0)#nb slots
        self.buff.put_int(8)#début espace libre
        self.buff.set_position(0)

    def setPageId(self,pageId):
        """
        Définit le PageIdx et le FileIdx de la PageId
        """
        self.buff.set_position(0)
        self.buff.put_int(pageId.FileIdx)
        self.buff.put_int(pageId.PageIdx)
        self.buff.set_position(0)

    def nextPageId(self):
        """
        Récupère le PageId suivant de la PageId actuelle
        """
        self.buff.set_position(0)
        pageId = PageId(self.buff.read_int(),self.buff.read_int())
        self.buff.set_position(0)
        return pageId

    def getEspaceDisponible(self):
        """
        Retourne l'espace disponible dans la PageId
        """
        self.buff.set_position(4096-8)
        nbSlot = self.buff.read_int()
        posFreeArea = self.buff.read_int()
        self.buff.set_position(0)
        return 4096-(nbSlot*8)-posFreeArea-8
    
    def setBufferAt(self,pos):
        self.buff.set_position(pos)
    
    def getNbSlots(self,bdd):
        """
        Récupère le nombre de slots dans la PageId
        """
        self.buff.set_position(bdd.DBParams.SGBDPageSize-8)
        nbSlots = self.buff.read_int()
        self.buff.set_position(0)
        return nbSlots
    
    def getdebutEspaceDispo(self,bdd):
        """
        Retourne le début de l'espace disponible de la PageId
        """
        self.buff.set_position(bdd.DBParams.SGBDPageSize-4)
        espaceDispo = self.buff.read_int()
        self.buff.set_position(0)
        return espaceDispo
    
    def setNbSlots(self, nbSlots,bdd):
        """
        Définit le nombre de slots dans la PageId
        """
        self.buff.set_position(bdd.DBParams.SGBDPageSize-8)
        self.buff.put_int(nbSlots)
        self.buff.set_position(0)

    def setdebutEspaceDispo(self,espaceDispo ,bdd):
        """
        Définit le début de l'espace disponible de la PageId
        """
        self.buff.set_position(bdd.DBParams.SGBDPageSize-4)
        self.buff.put_int(espaceDispo)
        self.buff.set_position(0)

    def putNewSlot(self,bdd,tailleRecord):
        """
        Ajoute un nouveau slot dans la PageId
        """
        nbSlot = self.getNbSlots(bdd)
        debutEspaceDispo = self.getdebutEspaceDispo(bdd)
        self.buff.set_position(bdd.DBParams.SGBDPageSize-16-(nbSlot*8))
        self.buff.put_int(debutEspaceDispo)
        self.buff.put_int(tailleRecord)
        self.buff.set_position(0)
    
    def remove(self,numSlot,bdd):
        '''
        Fonction utilisee pour le delete
        '''
        self.buff.set_position(bdd.DBParams.SGBDPageSize-8-(numSlot*8))
        #on va fixer la taille a -1
        self.buff.put_int(-1)
        self.buff.put_int(0)
        self.buff.set_position(0)
    
    def getValeurSlotAt(self,numSlot,bdd,pos):
        self.buff.set_position(bdd.DBParams.SGBDPageSize-8-(numSlot*8))
        value=self.buff.read_int()
        self.buff.set_position(pos)#pour rem
        return value
    