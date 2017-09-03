import binascii
import codecs
import string

letterFreq = "e t a o i n s r h l d c u m f p g w y b v k x j q z"
letterArray = letterFreq.split(' ')[::-1] # ::-1 = reversed
freqArray = {}
for i in range(len(letterArray)):
	freqArray[letterArray[i]] = i

def scoreEnglish(string):
	score = 0
	for i in range(len(string)):
		key = string[i]
		if key in freqArray:
			score = score + freqArray[key]
	return score 

def XORCHar(byteString, bc):
	bs = bytearray(byteString)
	newBA = bytearray(len(bs))
	for i in range(len(bs)):
		newBA[i] = bs[i] ^ bc[0]
	return newBA

highScore = 0 
bytes1 = b"1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
b1Decode = codecs.decode(bytes1, "hex")

needle = ""
index = 0

for i in range(len(string.printable)):
	b2Decode = string.printable[i].encode('ascii')
	english = XORCHar(b1Decode, b2Decode)
	score = scoreEnglish(english.decode("ascii"))
	if score > highScore:
		needle = english.decode("ascii")
		highScore = score
		index = i

print(needle)
print(highScore)
print(string.printable[index])

