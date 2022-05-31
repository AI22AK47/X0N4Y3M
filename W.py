import os
import urllib2
import sys
white="\033[0;37m"        # White
g="\033[1;32m"
yellow="\033[0;33m"       # Yellow
on_green="\033[42m"       # Green
os.system('clear')
print('\033[92m')
os.system('figlet WEB INFO')
print('\033[0;37m')
print(on_green+'\n\t [Author]-X0N4Y3M XbvGMJ'+white)
url = raw_input(yellow+'\n ENTER WEBSITE LINK : ')
url.rstrip ( )
header = urllib2.urlopen (url) .info ( )
print(str (header) )
