from PageId import PageId
from DataPage import DataPage
class HeaderPage : 
    def __init__(self,buff,bdd):
        """
        Initialise une instance de la classe HeaderPage
        """
        self.bdd = bdd
        self.buff = buff
        dirty = False #indique si la page a été modifiée

    def setFreePageId (self,pageId:PageId): #DES QUIL YA UN SET ON MET LE DIRTY A TRUE
        """
        Définit le 1er PageId livre
        """
        dirty=True
        self.buff.set_position(0)
        self.buff.put_int(pageId.FileIdx)
        self.buff.put_int(pageId.PageIdx)
        self.buff.set_position(0)
    def setFullPageId (self,pageId:PageId): #DES QUIL YA UN SET ON MET LE DIRTY A TRUE
        """
        Définit le 1er PageId plein
        """
        dirty=True
        self.buff.set_position(8)
        self.buff.put_int(pageId.FileIdx)
        self.buff.put_int(pageId.PageIdx)
        self.buff.set_position(8)
        return 
    
    def getFreePageId (self)->PageId:
        """
        Récupère le 1er PageId libre
        """
        self.buff.set_position(0)
        fileId=self.buff.read_int()
        pageId=self.buff.read_int()
        self.buff.set_position(0)
        return PageId(fileId,pageId)

    def getFullPageId (self)->PageId:
        """
        Récupère le 1er PageId plein
        """
        self.buff.set_position(8)
        fileId=self.buff.read_int()
        pageId=self.buff.read_int()
        x = PageId(fileId,pageId)
        self.buff.set_position(8)
        return x
    
    def getPagesFromListe(self,pageId):
        """
        Récupère une liste chainee de pageId qui precedent un certain pageId

        """
        listePage= []
        listePage.append(pageId)

        #initialisation
        if pageId.FileIdx != -1 :
            buffPage=self.bdd.buffer_manager.GetPage(pageId)
            dataPage= DataPage(buffPage)
            nextPage= dataPage.nextPageId()
            self.bdd.buffer_manager.FreePage(pageId,False)

            #on itere tant que ce n'est pas la derniere page
            while(nextPage.FileIdx!=-1):
                buffPage=self.bdd.buffer_manager.GetPage(nextPage)
                dataPage= DataPage(buffPage)
                tmp = nextPage
                if nextPage.FileIdx !=-1:
                    self.bdd.buffer_manager.FreePage(tmp,False)
                    listePage = listePage + [nextPage]
                nextPage = dataPage.nextPageId()
            
            self.bdd.buffer_manager.FreePage(nextPage,False)
        return listePage



