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

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

#get results from text file
text_file = open("4.txt", "r")
lines = text_file.readlines()
realScore = 0
realNeedle = ""
index = 0
index2 = 0

for x in range(len(lines)):
	highScore = 0 
	index2Temp = 0
	line = lines[x]
	bytes1 = line.encode()
	b1Decode = codecs.decode(bytes1.strip(), "hex")

	needle = ""

	for i in range(len(string.printable)):
		b2Decode = string.printable[i].encode('ascii')
		english = XORCHar(b1Decode, b2Decode)
		try:
			english.decode("ascii")	
			score = scoreEnglish(english.decode("ascii"))
			if score > highScore:
				needle = english.decode("ascii")
				highScore = score
				index2Temp = i 
		except UnicodeDecodeError:
			break

	if highScore > realScore: 
		realScore = highScore
		realNeedle = needle
		index = x
		index2 = index2Temp

print(realScore)
print(realNeedle)
print(index)
print(string.printable[index2])
print(lines[index])

