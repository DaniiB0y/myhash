import hashlib, sys, string
class myhash:
	def encode(self, hash, string):
		string = string.strip().lower()
		string = string.encode('utf-8')
		tips = hashlib.new(hash)
		tips.update(b"%b" % string)
		print("[+] Encrypt -> "+tips.hexdigest())
	#def decode(self, string):
try:
	h = sys.argv[1]
	s = sys.argv[2]
	exec = myhash()
	exec.encode(h, s)
except:
	print("\n[+] Usage -> python3 {hash} {string}\n\n[+] Exemple -> python3 md5 a")
