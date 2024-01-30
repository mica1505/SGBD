from ByteBuffer import ByteBuffer
import DBParams as DBP
from BDD import BDD
from Record import Record
from TableInfo import TableInfo
from ColInfo import ColInfo
from HeaderPage import HeaderPage
from DataPage import DataPage
from PageId import PageId
from RecordIterator import RecordIterator
'''
initialisation de la BDD
'''
bdd = BDD(DBP.DBParams("../DB/",4096, 4, 5))
diskManager = bdd.disk_manager
bfManager = bdd.buffer_manager
data_base_info = bdd.data_base_info
file_manager = bdd.file_manager

'''
CREATION D'UN HEADERPAGE
'''
headerPage = file_manager.createNewHeaderPage()
#premiere page de notre relation


"""
Creation tableInfo(relation)
"""
table = TableInfo("Personne",2,[ColInfo("Id",("INT",4)),ColInfo("Nom",("STRING(T)",5))],headerPage)
#tabVar = TableInfo("Prsn",2,[ColInfo("PRENOM",("VARSTRING(T)",15)),ColInfo("ID",("INT",4))],headerPage)
#print("Dans la table ->",table.headerPageId)

'''
CREATION Des RECORDS
'''
rec = Record(table,[1,"SIMBA"])
rec2 = Record(table,[0,"SMAIL"])
rec3 = Record(table,[3,"CHOPP"])


'''
ON AJOUTE UN PAGEID VIDE DANS LA LISTE CHAINEE

pageId = file_manager.addDataPage(table) #pageId vide
print(pageId)
'''
"""
ECRIRE LE RECORD DANS LE BUFFER
"""
#print('---------pageId1--------')
# print('----------insert------------')
i1=file_manager.InsertRecordIntoTable(rec)
print('llllllll',file_manager.InsertRecordIntoTable(rec2))
print('yyyyyyyyyyy',file_manager.InsertRecordIntoTable(rec3))

#print(file_manager.GetAllRecords(table))
pageId2 = PageId(1,0)
print('----------------read--------------')
recItr=RecordIterator(bdd,table,i1.pageId)



# print("ici",recTmp)
# recTmp=recItr.GetNextRecord(2)
# print("ici",recTmp)
# recTmp=recItr.GetNextRecord(3)
# print("ici",recTmp)

nbSlots = recItr.dataPage.getNbSlots(bdd)
print("nbSlots : ", nbSlots)
recItr.Reset()

for i in range(0,nbSlots) :
    x=recItr.GetNextRecord(i)
    print("x : ",x)
    recTmp=x
    print(recTmp)
    

for i in range(len(file_manager.getRecordsInDataPage(table,pageId2))):
    print('stpppppppppppp',file_manager.getRecordsInDataPage(table,pageId2)[i])





#print('\n---------pageId2--------\n')
#pageId2 = file_manager.addDataPage(table)
#print(pageId2)
#file_manager.writeRecordToDataPage(rec3,pageId2)
#file_manager.getRecordsInDataPage(table,pageId2)[0]


#pageId2 = file_manager.addDataPage(table)
#print(pageId2)
#print('\n---------getFreePageId--------\n')
#HeaderPage(bfManager.GetPage(table.headerPageId))
#pageIdFree=file_manager.getFreeDataPageId(table,4049)

#print(bfManager)
#print(pageIdFree)

