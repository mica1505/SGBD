
from DiskManager import DiskManager
import BufferManager as BM
from ByteBuffer import ByteBuffer
from TableInfo import TableInfo
from DataBaseInfo import DataBaseInfo
import DBParams as DP
from BDD import BDD
from DatabaseManager import DatabaseManager
from PageId import PageId


def main():
    dataBaseManager = DatabaseManager(BDD(DP.DBParams("../DB/",4096, 4, 2)))
    run = True
    commande = ""
    dataBaseManager.savedData()
    while(run):
        commande = input("=>")
        if(commande == "EXIT"):
            dataBaseManager.Finish()
            run = False
        else:
            dataBaseManager.ProcessCommand(commande)
    
    return
main()