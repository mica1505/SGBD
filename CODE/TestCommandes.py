
from DiskManager import DiskManager
import BufferManager as BM
from ByteBuffer import ByteBuffer
from TableInfo import TableInfo
from DataBaseInfo import DataBaseInfo
import DBParams as DP
from BDD import BDD
from DatabaseManager import DatabaseManager

#CREATE TABLE NomRelation (NomCol_1:TypeCol_1,NomCol_2)
#CREATE TABLE PremiereRelation(Nom:STRING(20),Prenom:STRING(10))
#INSERT INTO PremiereRelation VALUES (Mazouz,Camelia)

def main():
    dataBaseManager = DatabaseManager(BDD(DP.DBParams("../DB/",4096, 4, 2)))
    run = True
    commande = ""
    while(run):
        commande = input("=>")
        if(commande == "EXIT"):
            dataBaseManager.Finish()
            run = False
        else:
            dataBaseManager.ProcessCommand(commande)
    
    
    return
main()