import binascii
import codecs
import string
import base64

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
	bs = byteString
	newBA = bytearray(len(bs))
	for i in range(len(bs)):
		newBA[i] = bs[i] ^ bc[0]
	return newBA

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(len(bits) / 8):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

KEYSIZE_MIN = 2 
KEYSIZE_MAX = 40

def FindEditDistance(b1, b2):
	dist = 0
	for i in range(len(b1)):
		if b1[i] != b2[i]:
			dist = dist+1;
	return dist

# bits1 = tobits("this is a test")
# bits2 = tobits("wokka wokka!!!")

text_file = open("6.txt", "r")
file = text_file.read()
fileBytes = file.encode()
fileNoLines = file.replace("\n", "")
fileBytesNoLines = fileNoLines.encode()
fileBytesNoLines = codecs.decode(fileBytesNoLines, "base64")

# print(fileBytes)
# print(fileBytesNoLines)

keysizeScores = {}
for i in range(KEYSIZE_MIN, KEYSIZE_MAX):
	ba = bytearray(fileBytesNoLines)
	chunks = []
	for j in range(0, len(ba), i):
		chunks.append(ba[j:i+j])

	distances = []
	for j in range(1, len(chunks), 2):
		sb1 = codecs.decode(chunks[j], "ascii")
		sb2 = codecs.decode(chunks[j-1], "ascii")
		editDistance = FindEditDistance(tobits(sb1), tobits(sb2)) / i
		distances.append(editDistance)

	dist = sum(distances) / len(distances)
	keysizeScores[i] = dist
	# if i == 12:
	# 	print(kb1)
	# 	print(kb2)
	# 	print(fileBytesNoLines)

sortedScores = sorted(keysizeScores, key=keysizeScores.get)
print(keysizeScores)
print(sortedScores)

#for each tried keysize
sortedScores[0] = 29
repeatingKeys = []
for i in range(4):
	# print("========== NEW KEYSIZE, KEYSIZE NUMBER " + str(sortedScores[i])  + " ===========")
	# print("")
	blocks = []
	tryKesize = sortedScores[i]
	repeatingKey = bytearray(tryKesize)
	f = fileBytesNoLines
	max = int(len(f) / tryKesize)
	for j in range(max):
		blocks.append(f[tryKesize*j:tryKesize*(j+1)])
	transposedBlocks = []
	for j in range(tryKesize):
		transpose = bytearray(len(blocks))
		for x in range(len(blocks)):
			transpose[x] = blocks[x][j]
		transposedBlocks.append(transpose)
	for j in range(len(transposedBlocks)):
		# print("========= TRANSPOSED BLOCKS NUMBER " + str(j) + "===========")
		# print(transposedBlocks[j])
		# print("")
		scoreForThisBlock = 0
		stringForThisBlock = 0
		englishForThisBlock = ""
		for x in range(len(string.printable)):
			encode = string.printable[x].encode('ascii')
			english = XORCHar(transposedBlocks[j], encode)
			try:
				english.decode("ascii")
				score = scoreEnglish(english.decode("ascii"))
				if score > scoreForThisBlock:
					englishForThisBlock = english.decode("ascii")
					scoreForThisBlock = score
					stringForThisBlock = ord(string.printable[x])
			except UnicodeDecodeError:
				break
		if scoreForThisBlock > 0:
			repeatingKey[j] = stringForThisBlock
	repeatingKeys.append(repeatingKey)

print(repeatingKeys)
