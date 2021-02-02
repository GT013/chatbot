import json
import requests

url = requests.get("https://raw.githubusercontent.com/GT013/information/main/infor.json")
#print(url)
#print(url.content)
#print(type(url.content))
json_string = url.content
obj = json.loads(json_string)

#print(convert_to_list)
#print(type(convert_to_list))

for i in obj:
    #print(i)
    E1 = obj[0]['entity']['E1']
    E2 = obj[0]['entity']['E2']
    G1 = obj[0]['intents']['I1']
    G2 = obj[0]['intents']['I2']