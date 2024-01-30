from ByteBuffer import ByteBuffer
import DBParams as DBP
from BDD import BDD

'''
initialisation de la BDD
'''
bdd = BDD(DBP.DBParams("../DB/",4096, 4, 2))
diskManager = bdd.disk_manager
bfManager = bdd.buffer_manager

'''
Ecrire dans une page
'''
#instanciation du buffer d'ecriture
bfEcriture = ByteBuffer(4096)

#ecrire dans le buffer
print('------BUFFER ECRITURE------')
bfEcriture.put_char('L')
bfEcriture.put_int(0)
bfEcriture.put_char('L')
bfEcriture.put_char('L')


#Allocation de la page
pageId1 = diskManager.AllocPage()

#on ecrit dans la page
diskManager.WritePage(pageId1,bfEcriture)
print('-----pageId1----',pageId1)


'''
Lecture dans une page
'''

#instanciation du buffer de lecture
bfLecture = ByteBuffer(4096)

#on recupere le contenu de la page dans le buffer
diskManager.ReadPage(pageId1,bfLecture)


'''
On passe aux tests di buffer pool
'''
pageId2 = diskManager.AllocPage()
print('\n-----pageId2 ----',pageId2)

diskManager.Dealloc(pageId1)

pageId3 = diskManager.AllocPage()
print('\n-----pageId3--',pageId3)


bfManager.GetPage(pageId2)
print('on charge 1 0\n',bfManager)

bfManager.FreePage(pageId2,True)
print('on free 1 0\n',bfManager)

bfManager.GetPage(pageId3)
print('on charge 2 0\n',bfManager)

bfManager.GetPage(pageId3)
print('on accede 2 0\n',bfManager)


#print(bfManager.FindFrame(pageId1))
#print(bfManager.FindFrameLibre())


'''
Allocatioon de buffer depuis le buffer pool (bufferManager)

Frame1 = bfManager.listFrame[bfManager.FindFrameLibre()]
Frame1.page_id = diskManager.AllocPage()
#print(Frame1.page_id)

Frame1.buffer.put_char('D')
Frame1.buffer.put_char('R')
Frame1.buffer.put_float(1.258)
Frame1.buffer.put_float(52251112)
Frame1.buffer.put_char('O')

diskManager.WritePage(Frame1.page_id,Frame1.buffer)
diskManager.ReadPage(Frame1.page_id,Frame1.buffer)

print(Frame1.buffer.read_char(),end=' ')
print(Frame1.buffer.read_char(),end=' ')
print(Frame1.buffer.read_float(),end=' ')
print(Frame1.buffer.read_float(),end=' ')
print(Frame1.buffer.read_char(),end=' ')

print(bfManager)

'''