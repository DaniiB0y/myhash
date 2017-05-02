# -*- coding: utf-8 -*-
""" Alpha version
	even have errors!"""
import hashlib, sys
from string import *
#----------------------------------
print" ___ ___  __ __  __ __   ____  _____ __ __  "
print "|   |   ||  |  ||  |  | /    |/ ___/|  |  |"
print "| _   _ ||  |  ||  |  ||  o  (   \_ |  |  |"
print "|  \_/  ||  ~  ||  _  ||     |\__  ||  _  |"
print "|   |   ||___, ||  |  ||  _  |/  \ ||  |  |"
print "|   |   ||     ||  |  ||  |  |\    ||  |  |"
print "|___|___||____/ |__|__||__|__| \___||__|__|"
print "___________________________________________"
print " ¹: Resolve my Hash"
print " ²: Encode my Hash"                                           
x = input(': ')
if x == 1:
	print "Set your hash!"
	print "1: md5"
	print "2: sha1"
	met = int(input('~---~~>: '))	
	print "Select your file: Like /tmp/coins.txt"
	file = raw_input(': ')
	encode()
elif x == 2:
		encode()	
def resolve():
	arq = open(file, 'r')
	o = arq.readline()
	arq.close()
if met == 1:
	hsh = hashlib.md5(o)
	return hashlib.md5(o.encode()).hexdigest()
elif met == 2:
	hsh = hashlib.sha1(o)
	return hashlib.sha1(cleartextString.encode()).hexdigest()
else:
	print "error"

def encode():	
	print "Encode in?"
	inc = raw_input('Md5, Or Sha1?:')
	inc.lower()
	h = raw_input('Mensage: ')
	hsh = h
	hsh = hashlib.inc(hsh)
	print (hsh.hexdigest())
