from wit import Wit

wit_access_token = "HGFLWF45I5DTAWUMAN3YSMCFEL5MU3JA"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	intents = None
	try:
		entity = list(resp['entities'])[0]
		intents = resp['intents'][0]['name']	
	except:
		pass

	return (entity,intents)

print(wit_response("k4"))

resp = client.message("เอกสาร ก ย ศ")
print(resp)