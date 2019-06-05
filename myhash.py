import hashlib, sys
from string import *
import os 

def encode():
    a = input("Hash -> ")
    a = a.lower()
    h = hashlib.new(a)
    b = input("Text -> ")
    c = b.encode('utf-8')
    h.update(b"%b" % c)
    print(h.hexdigest())
encode()
#creditos ao capitão do discord
