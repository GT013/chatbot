import os, sys
from flask import Flask, request
from bot import wit_response
from pymessenger import Bot


chatbot = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAcLG6xt7eoBAAlsT8cp0ZBYhvQcbbZBhXatrwvz9qvZCBfbBw4bdCVUB644NiBHuoDv7rLoHdoCDrLHyZBZBW49f5TOSt5KSWb5MHFTGnlUO7ZCER16S6YSCZBwZCahyglkis19ZAt42ZAgGbE4ZApfTjEZC4utqNmd0yjJEP9qjGINa5p04Qw02tlZC"

bot = Bot(PAGE_ACCESS_TOKEN)


@chatbot.route('/', methods=['GET'])
def verify():
	
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "project4":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Test loading...", 200


@chatbot.route('/', methods=['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object'] == 'page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				
				sender_id = messaging_event['sender']['id']

				if messaging_event.get('message'):
	
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text = 'no text'

					response = None

					entity = wit_response(messaging_text)
					if entity == 'question:question':
						response = "1.ทุนสนับสนุนการศึกษา 2.ทุนเรียนดี-ทุนนำเสนอผลงาน 3.ทุน กยศ. 4.ติดต่อแอดมิน"
					elif entity == 'Scholarship_2:Scholarship_2':
						response = "เงื่อนไขการรับทุนเรียนดี-ทุนนำเสนอผลงานและกำหนดการสามารถติดตามได้ที่ https://office.kmitl.ac.th/osda/kmitl/ทุนเรียนดี-ทุนนำเสนอผลง/"
					elif entity =='Scholarship_1:Scholarship_1':
						response = "เงื่อนไขการรับทุนสนับสนุนการศึกษาและกำหนดการสามารถติดตามได้ที่ https://office.kmitl.ac.th/osda/kmitl/ทุนสนับสนุนการศึกษา/#1563854022569-d50c8d0b-0222"
					elif entity == 'Scholarship_K:Scholarship_K':
						response = "รายละเอียดทุนและกำหนดการสามารถติดตามได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751617-557051c0-5791"
						
					if response == None:
						response = "รอแอดมินตอบกลับนะคะ"
						
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	chatbot.run(debug = True, port = 80)