import socket
import requests
file = open('url.txt').read().split()
for url in file:
    domain = url.split('//')[1].replace('www.', '').replace('/', '')
    try :
        ipadrre = socket.gethostbyname(domain)
        print(ipadrre)
        response = requests.get(f"https://sonar.omnisint.io/reverse/{ipadrre}").json()
        print(len(response))
        for urldata in response:
            with open("urllist.txt", "a") as f:
                f.write(urldata+"\n")
                
            
    except:
        pass
    
