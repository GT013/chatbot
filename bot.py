from wit import Wit

wit_access_token = "HGFLWF45I5DTAWUMAN3YSMCFEL5MU3JA"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	#intents = None
	try:
		#entity = list(resp['entities'])[0]
		entity = list(resp['entities'])[0]
		#intents = list(resp['intents'])[0][1]
	except:
		pass

	return (entity)

print(wit_response("1"))

#resp = client.message("กำหนดการการกู้กยศ.")
#print(resp)