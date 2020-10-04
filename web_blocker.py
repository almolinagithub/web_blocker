
import os
import time
from datetime import datetime as dt

host_path = '/etc/hosts'
redirect = '127.0.0.1'
websites_list = ['www.facebook.com', 'facebook.com', 'www.hotmail.com', 'https://dub126.mail.live.com/' ]


while True:
    if dt.now().hour > 8 and dt.now().hour < 14:
        with open(host_path, mode= 'r+') as file:
            for website in websites_list:
                if website in file.read():
                    break
                else:
                    file.write(redirect +' ' + website + '\n')
        print('Working hour')
    else:
        with open(host_path, 'r+') as file:
            print('fun hours')
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in  websites_list):
                    file.write(line)
            file.truncate()
            break

        print('free time')
    time.sleep(5)
