#created by -- Sibivasan (Linux_3rr0r)
#updated on -- 08/08/2021
#Thanks to Ram ,Shakthi saravanaa

import requests
import json

file = open('mail.txt', 'r')
file1 = open('passwords_check.txt', 'r')
file2 = open('not_found.txt','r')
found1 = file1.read()
notfound = file2.read()
url = "https://myrz.org/"
dump = "8ba5e87b6a65aeb1f291d56850ffe036"
last = "&email="
uri = "api/email_search.php?key="
a=0
for each in file:
        x =(str(each))
        #print (x)
        if x in found1:
                #print(x)
                print(each +" *This password already found and present in a password.txt file :)")
                continue
        if x in notfound:
                print(each + " *we already process this mail this not found in a database ")
                continue
        if (a>=5):
                break
        a=a+1
        new_line = each.rstrip("\n")
        final    = new_line.replace(" ","")
        response = requests.get(url+uri+dump+last+final)
        dict = response.json()
        check = (dict['success'])
        if (check == True):
                result= (dict['results'])
                z = (result)
                file_check = open('passwords_check.txt', 'a')
                file_check.write(final + "\n")
                file_check.close()
                print(z)
                re = str(z)
                file_object = open('passwords.txt', 'a')
                file_object.write(re+ "\n")
                file_object.close()

        else:
                not_found = str(final)
                print (final + " *oops his password not leak in dark web")
                file_object1 = open('not_found.txt', 'a')
                file_object1.write(not_found + "\n")
                file_object1.close()


