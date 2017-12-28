import random
from random import choice
from string import ascii_letters
from string import digits
import re
import rsa

def func(string):
    (bob_pub, bob_priv) = rsa.newkeys(512)
    string = string.encode('utf8')
    crypto = rsa.encrypt(string, bob_pub)
    return (crypto,bob_priv)

def encrypt(crypto):
    string = rsa.decrypt(crypto[0], crypto[1])
    return string.decode('utf8')

string = 'Kolya programmer'
enc = func(string)
dec = encrypt(enc)
print(enc[0],'\n',enc[1],'\n',dec)
