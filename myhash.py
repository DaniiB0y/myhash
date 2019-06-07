import hashlib, sys, string, os, re
import urllib3
import urllib
from pyfiglet import Figlet
def decode():
	print("Coming Soon")
def encode():
    a = input("cryptography -> ")
    a = a.lower()
    h = hashlib.new(a)
    b = input("Text -> ")
    c = b.encode('utf-8')
    h.update(b"%b" % c)
    print(h.hexdigest())
def main():	
	f = Figlet(font='slant')
	print (f.renderText('myhash'))
	print("Encode -> 1")
	print("Decode -> 2")
	s = int(input(": "))
	if s == 1:
		encode()
	elif s == 2:
		decode()	
main()
#creditos ao capitão do discord
