from ByteBuffer import ByteBuffer

class Frame :
    def __init__(self) -> None:
        """
        Initialise une instance de la classe Frame
        Une Frame représente un espace dans le BufferManager pour stocker une page
        """
        self.buffer : ByteBuffer = ByteBuffer()
        self.page_id = None #id de la page stocké dans la frame
        self.dirty = False #indique si le contenu de la pge a été modifié
        self.pin_count = 0 #compteur de références
        self.LFU = 0 #compteur d'accès pour la politique LFU

    def clear(self):
        """
        Réinitialise les attributs de la frame
        """
        self.page_id = None
        self.dirty = False
        self.pin_count = 0
        self.LFU = 0
        self.buffer.set_position(0)
        
    def __str__(self):
        """
        Retourne les attributs de la frame sous forme de chaine de caractères
        """
        return " PAGEID : "+ str(self.page_id) + " DIRTY " +str(self.dirty) + " PINCOUNT " + str(self.pin_count) + " LFU : "  + str(self.LFU)
