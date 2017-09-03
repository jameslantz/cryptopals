import binascii
import codecs
bString = b"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
stringHex = codecs.decode(bString, "hex")
stringB64 = binascii.b2a_base64(stringHex)
print(bString)
print(stringHex)
print(stringB64)