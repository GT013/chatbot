from wit import Wit
import requests
wit_access_token = ""
url = "https://api.aiforthai.in.th/tlexplus"
headers = {
    'Apikey': "3jCLZWjPRQNh4xbgbb1B5OF5wBib37j8"
    }
client = Wit(access_token=wit_access_token)

text = 'เอกสารกู้ยืม กยศ ใช้อะไรบ้าง'

resp = client.message(text)


data = {'text':text}
 
response = requests.post(url, data=data, headers=headers)

print(resp) 
print(response.json())
