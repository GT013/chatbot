'''
import json,requests

url = requests.get("https://raw.githubusercontent.com/GT013/information/main/databasebot.json")
json_string = url.content
infor = json.loads(json_string)

entity = input("Entity = ")
intents = input("Intents = ")
for obj in infor:

    E1 = obj['entity1']
    E2 = obj['entity2']
    G1 = obj['intents1']
    G2 = obj['intents2']

    if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
        print(obj['response1'])      
        break    
    else:
        pass
    '''