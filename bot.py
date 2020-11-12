from wit import Wit

wit_access_token = "PFZOON223DGRVC2DZXCIJG3CPJH4ASBG"
client = Wit(access_token=wit_access_token)

def wit_response(message_text):
	
	resp = client.message(message_text)
	entity = None
	
	try:
		#entity = list(resp['entities'])[0]
		entity = list(resp['entities'])[0]
	except:
		pass

	return (entity)

#print(wit_response("กำหนดการการกู้กยศ."))

#resp = client.message("สวัสดีนะ")
#print(resp)