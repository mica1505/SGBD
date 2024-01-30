from PageId import PageId
from TableInfo import TableInfo
from BufferManager import BufferManager
from DataPage import DataPage
from Record import Record

class RecordIterator:
    def __init__(self,bdd,tabInfo,pageId):
        self.bdd=bdd
        self.buffer_manager=self.bdd.buffer_manager
        self.tabInfo=tabInfo
        self.pageId=pageId
        self.buffRI=self.buffer_manager.GetPage(self.pageId)
        self.dataPage=DataPage(self.buffRI)
        self.indiceSlot = 0
        self.nbSlots = self.dataPage.getNbSlots(self.bdd)
        self.dataPage.setBufferAt(8) #position du premier record.


    def GetNextRecord(self,index)->Record: #index correspond a l'index de la boucle sur laquelle on va iterer
        record=Record(self.tabInfo,[])
        if(self.indiceSlot < self.nbSlots):
            taille = record.readFromBuffer(self.buffRI,self.buffRI.get_pos())
            self.indiceSlot +=1
            return record
        else:
            return None
     
    #libere notre dataPage
    def Close(self):
        self.buffer_manager.FreePage(self.pageId,False)

    #remet au debut
    def Reset(self):
        self.indiceSlot=0
        self.dataPage.setBufferAt(8)

