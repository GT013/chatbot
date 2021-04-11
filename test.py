import json,requests
from typing import KeysView
from re import error
from sys import intern
import condata
#url = requests.get("https://raw.githubusercontent.com/GT013/information/main/databasebot.json")
#json_string = url.content
#infor = json.loads(json_string)
#for obj in infor:
    #E1 = obj['entity1']
 
entity = input("Entity = ")
intents = input("Intents = ")
for data in condata.rpw:              
    try:
        E1 = data[0]['entity1']
        E2 = data[0]['entity2']
        G1 = data[0]['intents1']
        G2 = data[0]['intents2']
        R1 = data[0]['response1']
        if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
            print(R1)
    except KeyError:
        continue
for data in condata.rpw:              
    try:
        E1 = data[0]['entity1']
        E2 = data[0]['entity2']
        G1 = data[0]['intents1']
        G2 = data[0]['intents2']
        R2 = data[0]['response2']
        if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
            print(R2)
    except KeyError:
        continue
#ค้นหาทีละลำดับเปรียบเทียบทีละอัน