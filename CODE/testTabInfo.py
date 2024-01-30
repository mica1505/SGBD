from ByteBuffer import ByteBuffer
import DBParams as DBP
from BDD import BDD
from Record import Record
from TableInfo import TableInfo
from ColInfo import ColInfo
'''
initialisation de la BDD
'''
bdd = BDD(DBP.DBParams("../DB/",4096, 4, 2))
diskManager = bdd.disk_manager
bfManager = bdd.buffer_manager
data_base_info = bdd.data_base_info



"""
Creation tableInfo(relation)
"""
table = TableInfo("Personne",2,[ColInfo("Id",("INT",4)),ColInfo("Nom",("STRING(T)",20))])
tabVar = TableInfo("Prsn",2,[ColInfo("PRENOM",("VARSTRING(T)",15)),ColInfo("ID",("INT",4))])

'''
CREATION D"UN RECORD
'''

rec = Record(table,[0,"SMAIL"])
recVar = Record(tabVar,["ME9IOUS",2])
recVide = Record(tabVar,[])


"""
ALLOCATOIN D"UNE FRAME ET RECUPERATION DU BUFFER
"""
pageId = diskManager.AllocPage()

bf = bfManager.GetPage(pageId)

"""
ECRIRE LE RECORD DANS LE BUFFER
"""

recVar.writeToBuffer(bf,0)

bf.set_position(0)
print('-',bf.read_int())
print('-',bf.read_int())
print(bf.read_char())
print(bf.read_char())
print(bf.read_char())
print(bf.read_char())
print(bf.read_char())
print(bf.read_char())
print(bf.read_char())

print(recVide.readFromBuffer(bf,0))
print(recVide.recvalues)


