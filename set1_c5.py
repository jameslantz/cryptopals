import binascii
import codecs

def repeatingKeyXOR(key, encryptIn):
	bk = bytearray(key)
	bs = bytearray(encryptIn)
	newBA = bytearray(len(bs))
	for i in range(len(bs)):
		byteKey = bk[i%len(bk)]
		newBA[i] = byteKey ^ bs[i]
	return codecs.encode(newBA, "hex")

xorString = "Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal".encode("ascii")
xorKey = "ICE".encode("ascii")

print(xorString, xorKey)

result = repeatingKeyXOR(xorKey, xorString)
print(result)