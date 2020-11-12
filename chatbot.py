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
					if entity == 'greeting:greeting':
						response = "1.ทุนต่าง ๆ ของสถาบัน\n2.ทุนกยศ.\n3.เรื่องอื่น ๆ\nกรุณาเลือกหัวข้อที่ต้องการจะสอบถาม เช่น อยากถามเรื่องอื่นๆค่ะ"
					elif entity == 'KYS:KYS':
						response = "ทุนกยศ.\n1.คุณสมบัติสำหรับการขอกู้กยศ.\n2.รายละเอียดของทุนกยศ.\n3.เอกสารประกอบการกู้กยศ.\n4.กำหนดการการกู้กยศ.\nกรุณาเลือกหัวข้อที่ต้องการจะสอบถาม เช่น อยากรู้เอกสารการกู้กยศ."
					elif entity == 'property_of_k:property_of_k':
						response = "สามารถดูรายละเอียดได้ที่ https://office.kmitl.ac.th/osda/studentloan/"
					elif entity == 'detail_of_k:detail_of_k':
						response = "กยศ. ลักษณะที่ 1 ขาดแคลนทุนทรัพย์\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา)\n-ค่าครองชีพ 2,400 บาท/เดือน *ตามที่นักศึกษาประสงค์ขอกู้ยืม\n-กยศ. ลักษณะที่ 2\n-ศึกษาในสาขาวิชาที่เป็นความต้องการหลักซึ่งมีความชัดเจนของการผลิตกำลังคนและมีความจำเป็นต่อการพัฒนาประเทศ\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา) \n-ค่าครองชีพ 2,400 บาท/เดือน *หากจะกู้ยืมค่าครองชีพ จะต้องเป็นผู้มีรายได้รวมของครอบครัวไม่เกิน 200,000 บาทต่อปี"
					elif entity == 'dcm_of_k:dcm_of_k':
						response = "สามารถดูรายละเอียดได้ที่ \nhttps://office.kmitl.ac.th/osda/studentloan/#1562124714078-a8a6b529-77ac"
					elif entity == 'time_of_k:time_of_k':
						response = "สามารถติดตามกำหนดการได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751146-e22dcd72-ed5d"
					if response == None:
						response = "รอแอดมินตอบกลับนะคะ"
						
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	chatbot.run(debug = True, port = 80)