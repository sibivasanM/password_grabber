#!/usr/shre/python

import requests
import pyfiglet

result = pyfiglet.figlet_format("Passwd_Grabber")
print(result)

print ("[+]==========>Password_Grabber Tool coded by:*@sibivasan *@Ram_Rv *@Shakthi_saravanaa <===========[-] \n")
print ("[+]@Linux_3rr0r[-]\n")
print ("[+]==========> Disclaimer: Developers assume no liability and are not <============================[-]\n")

file = open('mail.txt', 'r')

for each in file:

	
	response = requests.get("https://myrz.org/api/email_search.php?key=8ba5e87b6a65aeb1f291d56850ffe036&email="+each.rstrip("\n"))
	
	print("")
	print ("[+]",each.rstrip("\n"),"=>",response.json())
	 
	
	

file.close()
