# Coded by GH0STH4CKER
# Python 3.10
# For Education Purposes Only

import requests,json,re,time
from random_useragent import RANDOM_USER_AGENT
from bs4 import BeautifulSoup
from colorama import Fore,init
init()
Dgreen = Fore.LIGHTGREEN_EX
Lgreen = Fore.LIGHTGREEN_EX
Lyellw = Fore.LIGHTYELLOW_EX
Lred = Fore.LIGHTRED_EX
Lcyan = Fore.LIGHTCYAN_EX

def user_finder(new_u) :

    new_url2 = new_u+'/wp-json/wp/v2/users'
    
    headers = {"user-agent":RANDOM_USER_AGENT}
    
    r2 = requests.get(new_url2,headers=headers)
    
    if r2.status_code == 200 :
        print(Dgreen+'\n[+] Enumerating usernames : \n')
        time.sleep(1.3)
        data = json.loads(r2.text)
        for info in data :
            print(Lgreen+' [*] Username Found : {}'.format(info['slug']))
            time.sleep(0.2)
    else :
            print(Lyellw+'\n[-] Usernames Not Found ')
#--------------------------------------------

def adminpanel_finder(org_url) :
    
    urlA = org_url+'/wp-login.php?action=lostpassword&error=invalidkey'
    uagent = {"user-agent":RANDOM_USER_AGENT}
    
    r3 = requests.get(urlA,headers=uagent)

    if r3.status_code == 200 :
        r3data = r3.text
        pagesoup = BeautifulSoup(r3data,'html.parser')
        ptag = pagesoup.findAll("p",{"id":"nav"})
        
        if len(ptag) > 0 :
            for ptags in ptag :
                for atags in ptags.find_all('a') :
                    if 'Log in' in atags :
                        admin_url = atags['href']
                    else :
                        print(Lyellw+'\n[-] Admin panel not found ')

            print(Lgreen+'\n[+] Admin panel found - ',admin_url)
        
        else :
            print(Lyellw+'\n[-] Admin panel not found ')
    else :
        print(Lyellw+'\n[-] Admin panel not found ')


#---------------------------------------------

banner = """
 █ █ █ █▀█   █▀ █▀▀ ▄▀█ █▄ █ █▄ █ █▀▀ █▀█
 ▀▄▀▄▀ █▀▀   ▄█ █▄▄ █▀█ █ ▀█ █ ▀█ ██▄ █▀▄ """
dashline = "-------------------------------------------"
author = "  [+] Coded by GH0STH4CKER   [+] v 1.0 "

print(Lgreen+banner)
print(Lgreen+dashline)
print(Lyellw+author)
print(Lgreen+dashline)

#---------------------------------------------
print(Dgreen+ '\nWebsite Url (with https://) : ' + Lgreen, end="")
url = input('')
org_url = url
roboturl = url+'/robots.txt'
feedurl = url+'/feed'
url = url+'/wp-json'

headers = {"user-agent":RANDOM_USER_AGENT}

try:
    testreq = requests.get(org_url,headers=headers)
except Exception as e:
    print(Lred+'\nWebsite status : Error !')
else :
    print(Dgreen+'\nWebsite status : ',Lgreen+'Up')

    r = requests.get(url,headers=headers)
    rcode = r.status_code

    if rcode == 200 :

        robotres = requests.get(roboturl,headers=headers)

        if 'wp-admin' in robotres.text :
            print(Dgreen+'\n[+] WordPress Detection : ',Lgreen+'Yes')

            feedres = requests.get(feedurl,headers=headers)
            contents = feedres.text
            soup = BeautifulSoup(contents,'xml')
            wpversion = soup.find_all('generator')
            if len(wpversion) > 0 :
                wpversion = re.sub('<[^<]+>', "", str(wpversion[0])).replace('https://wordpress.org/?v=','')
                print(Dgreen+'\n[+] WordPress version : ',Lgreen+wpversion)
            else:
                rnew = requests.get(org_url,headers=headers)
                if rnew.status_code == 200 :
                    newsoup = BeautifulSoup(rnew.text,'html.parser')
                    generatorTAGS = newsoup.find_all('meta',{"name":"generator"})
                    for metatags in generatorTAGS :     
                        if "WordPress" in str(metatags) :
                            altwpversion = metatags['content']
                            altwpversion = str(altwpversion).replace('WordPress','')
                            print(Dgreen+'\n[+] WordPress version : ',Lgreen+altwpversion)
                else :
                    print(Lyellw+'[-] WordPress version : Not Found !')
            time.sleep(0.8)

            data = json.loads(r.text)
            siteName = data['name']
            siteDesc = data['description']

            plugins = data['namespaces']

            print(Dgreen+'\n[+] Webite name        :',Lgreen+siteName)
            time.sleep(0.8)
            print(Dgreen+'\n[+] Webite description :',Lgreen+siteDesc)
            time.sleep(0.8)
            print(Dgreen+'\n[+] Enumerating Plugins :',end=' ')
            plugins=list(set(plugins))
            print('\n')
            for i in plugins :
                elem = (i[:i.find('/')])
                print(Lgreen+' [*] ',elem) 
                time.sleep(0.2)
                              
            time.sleep(1)
            adminpanel_finder(org_url)
            time.sleep(1)
            user_finder(org_url)

        else :
            print(Lyellw+'\n[-] WordPress Detection : No')
    else :
        print(Lyellw+'\n[-] WordPress Detection : No')

print(Lcyan+'')
input('[ Thank you for using my tool ]')
