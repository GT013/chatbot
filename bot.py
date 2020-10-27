from wit import Wit

wit_access_token = "32XITT53VFSLFD6MDFSZ455DDCBXY4FN"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	
	try:
		entity = list(resp['entities'])[0]
	except:
		pass

	return (entity)

#print(wit_response("สวัสดีค่ะ"))