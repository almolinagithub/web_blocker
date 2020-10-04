
import os
from datetime import datetime as dt
import time as t

loopback = '127.0.0.1 '
hosts = 'hostbk'
websites_list = ['www.facebook.com', 'www.hotmail.com', 'www.redtube.com']


while True:
    if dt.now().hour > 8 and dt.now().hour < 17 :
        with open(hosts, 'r+') as file:
            for website in websites_list:
                content = file.read()
                if website in content:
                    break
                else:
                    file.write(loopback + ' ' + website + '\n')
                    print('working hour')
        t.sleep(5)
    else:
        with open(hosts, 'r+') as file:
            content = file.readlines()
            if not any(website in websites_list for line in lines):
                file.seek(0)
                for line in lines:
                    file.write(line)
            file.truncate()

    #    print('freetime')
        t.sleep(5)
