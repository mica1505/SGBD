class RecordId():
    def __init__(self,pageId,slotId):
        """
        Initialise une instance de la classe RecordId
        """
        self.pageId = pageId
        self.slotId = slotId

    def __str__(self):
        return "RecordId: PageId: "+str(self.pageId)+", slotId: "+str(self.slotId)
    