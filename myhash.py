import hashlib, sys, string, requests, os
from bs4 import BeautifulSoup

class myhash:
    def encode(self, hash, string):
        string = string.strip().lower()
        string = string.encode('utf-8')
        tips = hashlib.new(hash)
        tips.update(b"%b" % string)
        print("\n[+] ENCRYPT -> "+tips.hexdigest())
    def decode(self, hash):
        page = requests.get('https://hashtoolkit.com/reverse-hash/?hash={}'.format(hash))
        soup = BeautifulSoup(page.content, 'lxml')
        links = soup.findAll('a')
        payload = ''
        for link in links:
            link_href = link.get('href')
            if ('/generate-hash/?text=') in link_href:
                payload += (link.get('href').split('?text=')[1]+'\n')
            if payload:
                try:
                    payload = payload.split()
                    a = list(set(payload))
                    b = ''.join(a)
                    print("\n[+] DECRYPT -> {}".format(b))
                except:
                    pass
myclass = myhash()
if len(sys.argv) == 3:
    h = sys.argv[1]
    s = sys.argv[2]
    myclass.encode(h, s)
elif len(sys.argv) == 2:
    h = sys.argv[1]
    myclass.decode(h)
else:
    print("\n[+] USAGE TO ENCRYPT -> python3 myhash.py {hash} {string}\n\n[+] USAGE TO DECRYPT -> python3 myhash.py {hash}")
