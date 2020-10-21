from wit import Wit

wit_access_token = "6VK62DOSFZVG5G3NUFOPI5LRPAIQTLVT"
client = Wit(access_token=wit_access_token)
resp = client.message("เอกสารกู้ยืม กยศ ใช้อะไรบ้าง")
print(resp)