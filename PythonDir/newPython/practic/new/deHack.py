import os
import codecs
from Crypto.Cipher import XOR

def OpenFile(file_name, mod):
    try:
        the_file = codecs.open(file_name, mod, encoding='utf-8', errors='ignore')
    except IOError as e:
        print('Can\'t open file - ', file_name, '. Work will be closed \n', e)
    else:
        return the_file

def xorDecoder(string, key):
    cipher = XOR.new(key)
    return cipher.decrypt(string)

def Main():
    key = '123'
    for filename in os.listdir(os.getcwd()):
        if filename != 'Hack.py' and filename != 'deHack.py':
            the_file = OpenFile(filename, 'r')
            string = the_file.read()
            decrypted = xorDecoder(string, key)
            the_file.close()
            the_file = OpenFile(filename, 'w')
            the_file.write(decrypted)
            the_file.close()

Main()
