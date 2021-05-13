import requests
# GUANABARA
import urllib
import urllib.request
#

try:
    url = 'http://pudim.com.br/'

    response = requests.get(url)

    print('\033[0;32mConsegui acessar o site do pudim!\033[m')

except:
    print('\033[0;31mNão consegui acessar o site do pudim!\033[m')

# GUANABARA
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('Deu erro')
else:
    print('Tudo ok')
    # print(site.read())  # PEGA O CONTEÚDO DO SITE
#
