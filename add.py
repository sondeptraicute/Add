import requests
import re
import os
from time import sleep
from telegram import Bot

# Thay thế các giá trị sau bằng thông tin của bạn
TELEGRAM_TOKEN = '6462195738:AAHuj034oSgaV07Rg3oKiYTPZ2krFw10Suo'
CHAT_ID = '-1001982286205'

def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL ADD BẠN BÈ GỢI Ý - THANHPC')
    banner = '''
          Copyright © T-Tool 2023 | Phiên Bản: 1.0
          
    [  COPYRIGHT LICENSE: THANHPC         ]
    [  FB: Fb.com/ThanhVip.Prolife        ]              
    [  TOOL ADD BẠN BÈ GỢI Ý - VERSION 1.0  ]
    '''
    print(banner)

def check_live(cookie):
    headers = {
        # Headers của bạn ở đây
    }

    try:
        user_id = cookie.split('c_user=')[1].split(';')[0]
        name = requests.get(f'https://mbasic.facebook.com/profile.php?id={user_id}', headers=headers).text.split(f'<title>')[1].split(f'<')[0]
        return f'Facebook: {name} | UserID: {user_id}'
    except:
        return False

if __name__ == '__main__':
    banner()
    dem = 0
    cookie = input(f'Vui Lòng Nhập Cookie Facebook: ')

    if check_live(cookie) == False:
        exit(f'Cookie Facebook Die Hoặc Bị Văng !!')
    else:
        print(check_live(cookie))

    headers = {
        # Headers của bạn ở đây
    }

    while True:
        access = requests.get(f'https://mbasic.facebook.com/friends/center/suggestions/', headers=headers).text
        find = re.findall(f'\/a\/friends\/add\/\?encrypted_id\=.*?"', access)
        for add in find:
            dem = dem + 1
            add = add.replace(f'amp;', '').replace(f'"', '')
            id = add.split(f'subject_id=')[1].split(f'&')[0]
            name_ = requests.get(f'https://mbasic.facebook.com/profile.php?id={id}', headers=headers).text.split(f'<title>')[1].split(f'<')[0]
            requests.get(f'https://mbasic.facebook.com/'+add, headers=headers)
            message = f'[{dem}] | ADD FRIEND | {name_} - {id} |'
            send_telegram_message(message)
            sleep(60)
import requests
import re
import os
from time import sleep
from telegram import Bot

# Thay thế các giá trị sau bằng thông tin của bạn
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'

def send_telegram_message(message):
    bot = Bot(token=TELEGRAM_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    os.system('title TOOL ADD BẠN BÈ GỢI Ý - THANHPC')
    banner = '''
          Copyright © T-Tool 2023 | Phiên Bản: 1.0
          
    [  COPYRIGHT LICENSE: THANHPC         ]
    [  FB: Fb.com/ThanhVip.Prolife        ]              
    [  TOOL ADD BẠN BÈ GỢI Ý - VERSION 1.0  ]
    '''
    print(banner)

def check_live(cookie):
    headers = {
        # Headers của bạn ở đây
    }

    try:
        user_id = cookie.split('c_user=')[1].split(';')[0]
        name = requests.get(f'https://mbasic.facebook.com/profile.php?id={user_id}', headers=headers).text.split(f'<title>')[1].split(f'<')[0]
        return f'Facebook: {name} | UserID: {user_id}'
    except:
        return False

if __name__ == '__main__':
    banner()
    dem = 0
    cookie = input(f'Vui Lòng Nhập Cookie Facebook: ')

    if check_live(cookie) == False:
        exit(f'Cookie Facebook Die Hoặc Bị Văng !!')
    else:
        print(check_live(cookie))

    headers = {
        # Headers của bạn ở đây
    }

    while True:
        access = requests.get(f'https://mbasic.facebook.com/friends/center/suggestions/', headers=headers).text
        find = re.findall(f'\/a\/friends\/add\/\?encrypted_id\=.*?"', access)
        for add in find:
            dem = dem + 1
            add = add.replace(f'amp;', '').replace(f'"', '')
            id = add.split(f'subject_id=')[1].split(f'&')[0]
            name_ = requests.get(f'https://mbasic.facebook.com/profile.php?id={id}', headers=headers).text.split(f'<title>')[1].split(f'<')[0]
            requests.get(f'https://mbasic.facebook.com/'+add, headers=headers)
            message = f'[{dem}] | ADD FRIEND | {name_} - {id} |'
            send_telegram_message(message)
            sleep(60)
