import socket
import requests
file = open('wp-contentthemessitein.txt').read().split()
for url in file:
    domain = url.split('//')[1].replace('www.', '').replace('/', '')
    try :
        ipadrre = socket.gethostbyname(domain)
        response = requests.get(f"https://sonar.omnisint.io/reverse/{ipadrre}").json()
        for urldata in response:
            a=open('urllist.txt','a').write(urldata+"\n")
            a.close()
    except:
        pass
    
