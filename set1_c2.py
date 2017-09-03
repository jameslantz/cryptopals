import binascii
import codecs
bytes1 = b"1c0111001f010100061a024b53535009181c"
print(bytes1)
b1Hex = codecs.decode(bytes1, "hex")
print(b1Hex)
bytes2 = b"686974207468652062756c6c277320657965"
print(bytes2)
b2Hex = codecs.decode(bytes2, "hex")
print(b2Hex)

def bytesXOR(b1, b2):
	b1A = bytearray(b1)
	b2A = bytearray(b2)
	newBA = bytearray(len(b1A))
	for i in range(len(b1A)):
		newBA[i] = b1A[i] ^ b2A[i]
	return codecs.encode(newBA, "hex")

result = bytesXOR(b1Hex, b2Hex)
print(result)