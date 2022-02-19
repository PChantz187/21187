# Το IDE που χρησιμοποιούσα αποφάσισε να σταματήσει να δουλεύει οπότε έγραψα τον κώδικα σε 
# online editor, δεν έχω ιδέα πως να περάσω το randomness σε online editor 
# οπότε το έκανα copy-paste

import urllib2
import json
import datetime


randomness = "7998eb8d725e3edb054b52bfe1cc6b93f1219e2059160a87091e3df083fa15a7"
n = 2   
split_string = [randomness[i:i+n] for i in range(0, len(randomness), n)]
print(split_string)
length = len(split_string)

dec_string = [0] * length

# Δεκαεξαδικός σε Δεκαδικό
for i in range(len(split_string)):
    dec_string[i] = int(split_string[i], 16)
print(dec_string)

#Modulo 80
for i in range(len(split_string)):
    dec_string[i] = dec_string[i] % 80
print(dec_string)

#Βγάζω τα διπλά
dec_string = list(dict.fromkeys(dec_string))
print(dec_string)

ur_date=datetime.datetime.now()

def compare_lists(l1,l2):
    s=0
    for i in l1:
        if i in l2:
            s+=1
    return s
mynums= dec_string
for i in range(31):
    cur_date= cur_date - datetime.timedelta(days=1)
    date_str= cur_date.strftime("%d-%m-%Y")
    url='https://api.opap.gr/draws/v3.0/1100/last-result-and-active'%date_str
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    data = response.read()
    data=json.loads(data)
    klhrwseis= data['draws']['draw']
    r=[]
    for k in klhrwseis:
        tmp=k["results"]
        r.append(compare_lists(mynums,tmp))
    print("apotelesmata",date_str)
    print(min(r),r.count(min(r)))
    print (max(r),r.count(max(r)))
    print (10*"-")