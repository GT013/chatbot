'''
import json,requests
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
    E1 = data[0]['entity1']
    E2 = data[0]['entity2']
    G1 = data[0]['intents1']
    G2 = data[0]['intents2']
    R1 = data[0]['response1']
    if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
        print(R1)
        break
    else :
        pass
#ค้นหาทีละลำดับเปรียบเทียบทีละอัน
'''