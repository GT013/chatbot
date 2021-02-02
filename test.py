import json
import requests
from numpy import random

url = requests.get("https://raw.githubusercontent.com/GT013/information/main/i.json")
#print(url)
#print(url.content)
#print(type(url.content))
json_string = url.content
infor = json.loads(json_string)

#with open('inform.json',encoding='utf8') as f:
    #s=f.read()
    #obj = json.load(f)

q = input("entity : ")
t = input("intents : ")

    #print(data['entity'])
for obj in infor :
    E1 = obj['entity']['E1']
    E2 = obj['entity']['E2']
    G1 = obj['intents']['I1']
    G2 = obj['intents']['I2']

    if E1 == q and G1 == t or E2 == q and G2 == t:
        print(obj['response'])
    else:
        print(random.choice(obj['answer']))



   



    