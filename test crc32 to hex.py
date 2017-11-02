from zlib import crc32
print(hex(crc32(b'TEST-the-equivalence')))
print("%08X" % ((crc32(b'TEST-the-equivalence') & 0xFFFFFFFF)))