import PageId
import ByteBuffer
from Frame import Frame

class BufferManager :

    def __init__(self, bdd):
        """
        Initialise une instance de la classe BufferManager
        """
        self.bdd = bdd
        self.disk_manager = bdd.disk_manager
        self.frameCount = bdd.DBParams.frameCount
        self.listFrame = [Frame() for i in range(self.frameCount)]
        
        
    def reset(self):
        """
        Réinitialise tous les tampons dans la liste de tampons
        """
        #self.frameCount = 0
        for frame in self.listFrame :
            frame.clear()
             #a verifier
        
    def __str__(self):
        """
        Renvoie sous forme de chaine de caractères le bufferManager
        """
        res = ""
        for i in range(len(self.listFrame)):
            res += "\n" +str(i)+ "\t" + str(self.listFrame[i])
        return res
    
    def FindFrameLibre(self)->int:
        """
        LFU : 
        Une page peut être remplacée ssi son pin_count = 0
        • Choisir une frame parmi celles dont le contenu n'est pas utilisé couramment (pin_count=0) pour remplacer son contenu;
        • Si la frame est marquée comme “dirty”, écrire d'abord son contenu sur le disque puis remettre son dirty à 0
        """
        #LFU
        index : int = None
        min=None
        #il ya une case libre
        for i in range(len(self.listFrame)) :
            if self.listFrame[i].page_id==None :
                index=i 
                return index 
        #on remplace
            elif self.listFrame[i].pin_count == 0:
                if min==None or min > self.listFrame[i].LFU: #premier pincount a zero 
                    min=self.listFrame[i].LFU
                    index=i

        if index==None : 
            raise Exception("Aucune frame disponible")
        # a verifier dans le cas d'une case vide
        if(self.listFrame[index].dirty):
            self.disk_manager.WritePage(self.listFrame[index].page_id,self.listFrame[index].buffer)

        self.listFrame[index].clear() 
        return index

    def FindFrame(self, pageId : PageId):#verifie si la page est deja chargee
        """
        Recherche si la page est déjà chargé dans une frame
        """
        index = None
        for i in range(len(self.listFrame)) :
            if self.listFrame[i].page_id == pageId : 
                index = i 
        return index

    def GetPage(self, pageId : PageId) -> ByteBuffer:
        """
        Récupère une page à partir du bufferPool
        """
        if pageId.FileIdx == -1 and pageId.PageIdx == 0:
            return None

        indice = self.FindFrame(pageId) #La page est déjà chargé dans la frame
        if indice != None:
            self.listFrame[indice].pin_count+=1
            self.listFrame[indice].LFU+=1
            return self.listFrame[indice].buffer

        #La page n'est pas déjà chargé dans une frame
        i = self.FindFrameLibre()
        
        frameId=self.listFrame[i]
        frameId.page_id = pageId
        self.bdd.disk_manager.ReadPage(pageId, frameId.buffer)
        frameId.pin_count+=1
        frameId.LFU+=1
        return self.listFrame[i].buffer

    def FreePage(self, pageId : PageId, valdirty) -> None:
        """
        Libère une page et met à jour le pin_count
        """
        for i in range(len(self.listFrame)) : 
            if self.listFrame[i].page_id == pageId :
                self.listFrame[i].pin_count-=1
                if valdirty:
                    self.listFrame[i].dirty = valdirty
                self.listFrame[i].buffer.set_position(0)
                
                
    
    def FlushAll(self) -> None :
        """
        ◦ l'écriture de toutes les pages dont le flag dirty = 1 sur disque
        ◦ la remise à 0 de tous les flags/informations et contenus des buffers (buffer pool « vide »)

        """
        for i in range(len(self.listFrame)):
            if(self.listFrame[i].dirty==1):
                self.bdd.disk_manager.WritePage(self.listFrame[i].page_id,self.listFrame[i].buffer)
            self.listFrame[i].clear()
