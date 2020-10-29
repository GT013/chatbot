from wit import Wit

wit_access_token = "6VK62DOSFZVG5G3NUFOPI5LRPAIQTLVT"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	
	try:
		entity = list(resp['entities'])[0]
	except:
		pass

	return (entity)

#print(wit_response("ทุนสองค่ะกับทุน1"))