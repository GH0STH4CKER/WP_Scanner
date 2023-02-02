"""
* Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Dimuth De Zoysa <dimuthsakya@protonmail.com>, September 2022
 *
 """

# Coded by GH0STH4CKER
# Python 3.10.0
# For Education Purposes Only
import requests,json,re,time
from random import randint
from bs4 import BeautifulSoup
from colorama import Fore,init

init()
Dgreen = Fore.LIGHTGREEN_EX
Lgreen = Fore.LIGHTGREEN_EX
Lyellw = Fore.LIGHTYELLOW_EX
Lred = Fore.LIGHTRED_EX
Lcyan = Fore.LIGHTCYAN_EX

user_agent_list = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; E6653 Build/32.2.A.0.253) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One X10 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1","Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/13.2b11866 Mobile/16A366 Safari/605.1.15","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1","Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A5370a Safari/604.1","Mozilla/5.0 (iPhone9,3; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (iPhone9,4; U; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1","Mozilla/5.0 (Apple-iPhone7C2/1202.466; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543 Safari/419.3","Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; RM-1127_16056) AppleWebKit/537.36(KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10536","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.1058","Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36","Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36","Mozilla/5.0 (Linux; Android 4.4.3; KFTHWI Build/KTU84M) AppleWebKit/537.36 (KHTML, like Gecko) Silk/47.1.79 like Chrome/47.0.2526.80 Safari/537.36","Mozilla/5.0 (Linux; Android 5.0.2; LG-V410/V41020c Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/34.0.1847.118 Safari/537.36","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246","Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1","Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36","Roku4640X/DVP-7.70 (297.70E04154A)","Mozilla/5.0 (Linux; U; Android 4.2.2; he-il; NEO-X5-116A Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30","Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36","Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)","AppleTV6,2/11.1","AppleTV5,3/9.1.1","Mozilla/5.0 (Nintendo WiiU) AppleWebKit/536.30 (KHTML, like Gecko) NX/3.0.4.2.12 NintendoBrowser/4.3.1.11264.US","Mozilla/5.0 (Windows NT 10.0; Win64; x64; XBOX_ONE_ED) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393","Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Xbox; Xbox One) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10586","Mozilla/5.0 (PlayStation 4 3.11) AppleWebKit/537.73 (KHTML, like Gecko)","Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2","Mozilla/5.0 (Nintendo 3DS; U; ; en) Version/1.7412.EU","Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)","Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)","Mozilla/5.0 (compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp)","Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+","Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"]

RANDOM_USER_AGENT = user_agent_list[randint(0,52)]

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
