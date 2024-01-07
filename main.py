import urllib.request
import json
import datetime
import random
import string
import time
import os
import sys

print("e̅r̅i̅c̅e̅t̅h̅a̅n̅")
script_version = '1'
window_title = f"WARP-PLUS-GB ++ Edited By Eric Ethan (version {script_version})"
os.system('title ' + window_title if os.name == 'nt' else 'PS1="\[\e]0;' +
          window_title + '\a\]"; echo $PS1')
os.system('cls' if os.name == 'nt' else 'clear')
print(
    '  By Eric Ethan \n'
)

print("[-] you can getting unlimited GB on Warp+.")
print(f"[-] Version: {script_version}")
print("--------")
print("[+] THIS SCRIPT CODDED BY ALIILAPRO")
print("[-] modified by Eric Ethan")
print("--------")
referrer = "9d5977bf-2f8d-4931-885f-0bb6220d81ff"


def progressBar():
    animation = [
    "10%","20%","30%","40%","50%","60%","70%","80%","90%","100%"
    ]
    progress_anim = 0
    save_anim = animation[progress_anim % len(animation)]
    percent = 0
    while True:
        for i in range(10):
            percent += 1
            text = "Eric Ethan"
            sys.stdout.write(f"\r[+] Server \nresponse...  " + text +
                             f" {percent} %")
            sys.stdout.flush()
            time.sleep(0.075)
        progress_anim += 1 
        save_anim = animation[progress_anim % len(animation)]
        if percent == 100:
            print("")
             
            sys.stdout.write("\r[+] Request completed...      100%")
        break

def genString(stringLength):
    try:
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    except Exception as error:
        print(error)


def digitString(stringLength):
    try:
        digit = string.digits
        return ''.join((random.choice(digit) for i in range(stringLength)))
    except Exception as error:
        print(error)


url = f'https://api.cloudflareclient.com/v0a{digitString(3)}/reg'


def run():
    try:
        install_id = genString(22)
        body = {
            "key": "{}=".format(genString(43)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+02:00",
            "type": "Android",
            "locale": "es_ES"
        }
        data = json.dumps(body).encode('utf8')
        headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Host': 'api.cloudflareclient.com',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
            'User-Agent': 'okhttp/3.12.1'
        }
        req = urllib.request.Request(url, data, headers)
        response = urllib.request.urlopen(req)
        status_code = response.getcode()
        return status_code
    except Exception as error:
        print("")
        print(error)


g = 0
b = 0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("e̅r̅i̅c̅e̅t̅h̅a̅n̅")
    print("")
    print("")
    sys.stdout.write("\r[+] Sending request...    0%")
    sys.stdout.flush()
    result = run()
    if result == 200:
        g += 1
        progressBar()
        print(f"\n[-] WORK ON ID: {referrer}")
        print(f"[:)] {g} GB have gb hack!")
        print(f"[#] Total: {g} Success {b} Error")
        for i in range(1, 0, -1):
            sys.stdout.write
            (
                f"\r[*] After {i} seconds, gb hack start")
            sys.stdout.flush()
            time.sleep(1)
    else:
        b += 1
        print("[:(] Error server.")
        print(f"[#] Total: {g} Success {b} Error")
        for i in range(1, 0, -1):
            sys.stdout.write(f"\r[*] Retry in {i}s...")
            sys.stdout.flush()
            time.sleep(1)
