import json
import requests
from numpy import random

#url = requests.get("https://raw.githubusercontent.com/GT013/information/main/i.json")
#print(url)
#print(url.content)
#print(type(url.content))
#json_string = url.content
#infor = json.loads(json_string)

with open('i.json',encoding='utf8') as f:
    #s=f.read()
    obj = json.load(f)

#print(obj[0]['answer'][0])


q = input("entity : ")
#t = input("intents : ")
th =3
    #print(data['entity'])

if q == '3':
    print(input("พิมพ์คำถามทิ้งไว้ : "))
    print("แล้วจะติดต่อกลับ")
else:
    pass

for obj in obj :
    E1 = obj['entity']['E1']
    E2 = obj['entity']['E2']
    G1 = obj['intents']['I1']
    G2 = obj['intents']['I2']

    
    #if E1 == q and G1 == t or E2 == q and G2 == t:
        #print(obj['response'])
    #else:
        #pass
        #print(random.choice(["จีจี","Haha","บ้าเอ้ย"],size=1))      


   



    