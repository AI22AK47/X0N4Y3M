import os
import sys
import requests
import time
os.system('clear')

# Regular Colors
black="\033[0;30m"        # Black
red="\033[0;31m"          # Red
green="\033[0;32m"        # Green
yellow="\033[0;33m"       # Yellow
blue="\033[0;34m"         # Blue
purple="\033[0;35m"       # Purple
cyan="\033[0;36m"         # Cyan
on_green="\033[42m"       # Green
on_blue="\033[44m"        # Blue
white="\033[0;37m"        # White
	
os.system('clear')
os.system("figlet -f small X0N4Y3M | lolcat")


print(on_green+'\n\t[Author]-SABBIR AHMED')
print(blue+'========================================================')

print(red+'\n\t[1] SMS BOMBING ')
print(green+'\n\t[2] EMAIL BOMBING ')
print(red+'\n\t[3] WEB INFO ')
print(green+'\n\t[4] DDOS ATACK ')
print(red+'\n\t[5] EXTRA KEY ')
	
slc=str(input(yellow+'\n\t[!] CHOSE A OPTION : '))

if slc=='1':
	os.system('python3 S.py')
if slc=='2':
	os.system('python2 E.py')
if slc=='3':
    os.system('python2 W.py')
if slc=='4':
    os.system('python3 ddos.py')
else:
    os.system('toxic')
