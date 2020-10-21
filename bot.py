from wit import Wit

wit_access_token = "HCEFKTG6MGSPZQBZDTCYA7GUDM5JBNXF"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	
	try:
		entity = resp['entities'][0]
	except:
		pass

	return (entity)

#resp = client.message("ขอบคุณ")
#print(resp)