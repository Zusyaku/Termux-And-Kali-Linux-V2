#code h4cklinker

import json,requests,re,sys

try:
    print("""

█    ▄█    ▄   █  █▀  ▄▄▄▄▄   
█    ██     █  █▄█   █     ▀▄ 
█    ██ ██   █ █▀▄ ▄  ▀▀▀▀▄   
███▄ ▐█ █ █  █ █  █ ▀▄▄▄▄▀    
    ▀ ▐ █  █ █   █            
 v.01   █   ██  ▀  SEO ?-
-----------------Tegal1337
        """)
    if (sys.version_info.major == 3):
        site = input("[+] Jeneng domain\t: ")
    else:
        site = raw_input("[+] Jeneng domain\t: ")
    with open("backlink.json", "r") as file:
        data = json.loads(file.read())
        for backlink in data:
            url = backlink['url'].replace("tegal-1337.com", site)
            try:
                r = requests.get(url).status_code
            except KeyboardInterrupt:
                sys.exit()
            except:
                r = "Request kesuen"
            
            print ("~ " + site + " | Hasile -> "+re.search('http:\/\/.*?\/', url).group(0).replace("/", "").replace("http:","")+ " status: "+str(r))
except:
    print("\n\n -> exit\n")
