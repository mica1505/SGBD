import ByteBuffer as ByteBuffer
import sys
buffer = ByteBuffer.ByteBuffer()
buffer.put_int(13)
buffer.put_int(-24)
buffer.put_float(3.2)
buffer.put_char('T')
buffer.put_char('P')

buffer.set_position(0)
print(buffer.read_int())
print(buffer.read_int())
print(buffer.read_float())
print(buffer.read_char())
print(buffer.read_char())

with open("buffer.txt", 'wb') as f:
    f.seek(20)
    f.write(buffer.to_bytes())

    f.seek(10)
    f.write(buffer.to_bytes())

buffer = ByteBuffer.ByteBuffer(0)
with open("buffer.txt", 'rb') as f:
    buffer.from_bytes(f.read()[20:50])

    print(buffer.read_int())
    print(buffer.read_int())
    print(buffer.read_float())
    print(buffer.read_char())
    print(buffer.read_char())

with open("buffer.txt", 'rb') as f:
    buffer.from_bytes(f.read()[10:40])

    print(buffer.read_int())
    print(buffer.read_int())
    print(buffer.read_float())
    print(buffer.read_char())
    print(buffer.read_char())

