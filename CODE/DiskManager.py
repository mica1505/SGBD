from PageId import PageId
from ByteBuffer import ByteBuffer


class DiskManager :

    def __init__(self, bdd):
        """
        Initialise une instance de la classe DiskManager
        """
        self.bdd = bdd
        self.fileCounter = [0]*self.bdd.DBParams.DMFileCount
        self.pagesDisponibles = []

    def reset(self):
        """
        Réinitialise les compteurs et la liste de page disponibles
        """
        self.fileCounter = [0]*self.bdd.DBParams.DMFileCount
        self.pagesDisponibles = []
        
    def AllocPage(self) -> PageId :
        """
        Alloue une nouvelle page
        """
        if (len(self.pagesDisponibles)!=0):
            return self.pagesDisponibles.pop(0)
        else:
            index = self.fileCounter.index(min(self.fileCounter))
            self.fileCounter[index]+=1

            with open(self.bdd.DBParams.DBPath+"F"+str(index)+".data","ab") as f:
                f.write(bytearray(4096))
            return PageId(index, self.fileCounter[index]-1)

    def ReadPage(self,pageId: PageId, buff : ByteBuffer) -> None:
        """
        Lit le contenu d'une page dans un fichier
        """
        numPage = pageId.PageIdx
        numFile = pageId.FileIdx
        pos = self.bdd.DBParams.SGBDPageSize*numPage
        file = open(self.bdd.DBParams.DBPath+"F"+str(numFile)+".data","rb")#revoir le seek
        file.seek(pos)
        buff.from_bytes(file.read(self.bdd.DBParams.SGBDPageSize))
        file.close()
    
    def WritePage(self,pageId: PageId, buff) -> None:
        """
        Ecrit le contenu d'une page dans un fichier
        """
        numPage = pageId.PageIdx
        numFile = pageId.FileIdx
        pos = 4096*numPage
        with open(self.bdd.DBParams.DBPath+"F"+str(numFile)+".data","rb+") as f:
            f.seek(pos)
            f.write(buff.to_bytes())

    def Dealloc(self,pageId:PageId) -> None: 
        """
        Desalloue une page en ajoutant son PageId à la liste de pages
        """
        self.pagesDisponibles.append(pageId)

    def GetCurrentCountAllocPages(self) ->  int :
        """
        Retourne le nombre actuel de pages allouées
        """
        return sum(self.fileCounter)-len(self.pagesDisponibles)
    
    def Init(self) -> None :
        """
        Initialise les compteurs et la liste de pages disponibles à partir d'un fichier
        """
        with open (self.bdd.DBParams.DBPath+'DBDisk.save','r') as f1:
            # première ligne TabInfo self.fileCounter et taille self.pagesDisponibles 
            param = f1.readline().split(" ")
            param[-1] = param[-1][:-1]
            for i in range(4):
                self.fileCounter[i] = int(param[i])
            nbPagesDisponibles = int(param[4])
            # les autre lignes representent les PageId
            for f in f1:
                self.pagesDisponibles.append(PageId(int(f.split(" ")[0]), int(f.split(" ")[1])))
                
    def Finish(self) -> None:
        """
        Sauvegarde les compteurs et la liste de pages disponibles dans un fichier
        """
        with open (self.bdd.DBParams.DBPath+'DBDisk.save','w') as f1:
            # première ligne TabInfo self.fileCounter et taille self.pagesDisponibles 
            for i in range(4):
                f1.write(str(self.fileCounter[i]) + " ")
            f1.write(str(len(self.pagesDisponibles)) + "\n")
            for i in range(len(self.pagesDisponibles)):
                f1.write(str(self.pagesDisponibles[i].FileIdx) + " " + str(self.pagesDisponibles[i].PageIdx) + "\n")    