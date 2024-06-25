from fake_headers import Headers
from threading import Thread
from requests import get
from telebot import TeleBot
from time import sleep


def try_proxy(proxy):
    all_c.append('')
    try:
        proxies = {'http': f'http://{proxy.replace("http://", "")}', 'https': f'http://{proxy.replace("http://", "")}'}
        get("https://api.ipify.org", proxies=proxies, headers=headers.generate(), timeout=5).text
        print(f'{BOLD + GREEN + proxy.replace("http://", "")} - VALID (HTTP)')
        good_c.add(proxy)
        with open("good.txt", 'a') as f:
            f.write("http://" + proxy.replace("http://", "") + "\n")
    except:
        try:
            proxies = {'http': f'https://{proxy.replace("http://", "")}', 'https': f'https://{proxy.replace("http://", "")}'}
            get("https://api.ipify.org", proxies=proxies, headers=headers.generate(), timeout=5).text
            print(f'{BOLD + GREEN + proxy.replace("http://", "")} - VALID (HTTPS)')
            good_c.add(proxy)
            with open("good.txt", 'a') as f:
                f.write("https://" + proxy.replace("http://", "") + "\n")
        except:
            try:
                proxies = {'http': f'socks4://{proxy.replace("http://", "")}', 'https': f'socks4://{proxy.replace("http://", "")}'}
                get("https://api.ipify.org", proxies=proxies, headers=headers.generate(), timeout=5).text
                print(f'{BOLD + GREEN + proxy.replace("http://", "")} - VALID (SOCKS4)')
                good_c.add(proxy)
                with open("good.txt", 'a') as f:
                    f.write("socks4://" + proxy.replace("http://", "") + "\n")
            except:
                try:
                    proxies = {'http': f'socks5://{proxy.replace("http://", "")}', 'https': f'socks5://{proxy.replace("http://", "")}'}
                    get("https://api.ipify.org", proxies=proxies, headers=headers.generate(), timeout=5).text
                    print(f'{BOLD + GREEN + proxy.replace("http://", "")} - VALID (SOCKS5)')
                    good_c.add(proxy)
                    with open("good.txt", 'a') as f:
                        f.write("socks4://" + proxy.replace("http://", "") + "\n")
                except:
                    print(f'{BOLD + RED + proxy.replace("http://", "")} - INVALID')
                    


good_c = set()
all_c = list()
bot = TeleBot("7093667487:AAEBK00IkB3W3SW81b2bx7l879tFK-CitWo")
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
headers = Headers(headers=True)
proxies = set()
with open("proxy.txt") as file:
    for line in file:
        proxies.add(line.strip())


threads = []
count = 1
for proxy in proxies:
    sleep(0.1)
    thrd = Thread(target=try_proxy, args=(proxy,), name=count)
    threads.append(thrd)
    thrd.start()
    count += 1

for thrd in threads:
    thrd.join()
    print(f"{BOLD + GREEN}Thread {thrd.name} ended")

bot.send_document(6713279525, open("good.txt", 'rb'))