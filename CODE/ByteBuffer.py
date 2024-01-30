import struct

class ByteBuffer:
    def __init__(self, size=4096):
        """
        Initialise une instance de la classe ByteBuffer
        """
        self.__bytes = [None]*size #tableau créer
        self.__pos = 0 #position initialisé

    def set_position(self, pos):
        self.__pos = pos #défini la position

    def from_bytes(self, bytes):
        #lire
        self.__pos = 0
        for i,b in enumerate(bytes):
            self.__bytes[i] = b

    def to_bytes(self):
        #ecrire
        return bytes([b for b in self.__bytes if b != None])

    def read_int(self):
        #lit un entier de 4 octets
        b = self.__bytes[self.__pos: self.__pos + 4]
        val = int.from_bytes(b, byteorder='big', signed=True)
        self.__pos = self.__pos + 4
        return val

    def put_int(self, i):
        #convertit un entier en 4 octets
        for i, c in enumerate(i.to_bytes(4, byteorder = 'big', signed=True)):
            self.__bytes[self.__pos + i] = c
        self.__pos = self.__pos + 4

    def read_float(self):
        #lit un float de 4 octets
        b = bytes(self.__bytes[self.__pos: self.__pos + 4])
        f = struct.unpack_from('<f', b)[0]
        f = round(f, ndigits=2)
        self.__pos = self.__pos + 4
        return f

    def put_float(self, f):
        #convertit un float en 4 octets
        for i, c in enumerate(struct.pack('<f', f)):
            self.__bytes[self.__pos + i] = c
        self.__pos = self.__pos + 4

    def read_char(self):
        #lit un caractère d'2 octet et le décode en utf-8
        r = self.__bytes[self.__pos]
        r = bytes([r]).decode('utf-8')
        #faut check la taille d'un char
        self.__pos += 1
        return r

    def put_char(self, c):
        #convertit en utf-8 un caractère en 2 octet 
        b = c.encode('utf-8')
        self.__bytes[self.__pos] = b[0]
        self.__pos += 1

    def get_pos(self):
        #retourne la position actuelle
        return self.__pos
    
