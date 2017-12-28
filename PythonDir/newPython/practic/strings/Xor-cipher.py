from Crypto.Cipher import XOR
def xorCoder(string, key):
    cipher = XOR.new(key)
    return cipher.encrypt(string)

def xorDecoder(string, key):
    cipher = XOR.new(key)
    return cipher.decrypt(string)

string = "I'm a killer"
key = '123'
encodedString = xorCoder(string, key)
print(encodedString)
decodedString = xorDecoder(encodedString, key)
print(decodedString)
