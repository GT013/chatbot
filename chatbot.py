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

					entity,intents = wit_response(messaging_text)

					if entity == 'greeting:greeting' and intents == 'greeting':
						response = "1.ทุนต่าง ๆ ของสถาบัน\n2.ทุนกยศ.\n3.ติดต่อแอดมิน\nกรุณาเลือกหมายเลขที่ต้องการจะสอบถาม"
					elif entity == 'one:one' and intents == 'number':
						response = "ทุนต่าง ๆ ของสถาบัน\nS1.ทุนเรียนดี-ทุนนำเสนอผลงาน\nS2.ทุนสนับสนุนการศึกษา\nกรุณาเลือกหัวข้อตัวเลขที่ต้องการจะสอบถาม เช่น S1\nหรืออ่านรายละเอียดทุนเพิ่มเติมได้ที่\nhttps://office.kmitl.ac.th/osda/kmitl/#1573006604624-d5ec5ed1-4c6a"
					elif entity == 'S1:S1' and intents == 'sec_1':
						response = "ทุนเรียนดี-ทุนนำเสนอผลงาน\nT1.ทุนเรียนดี\nT2.ทุนผู้สร้างชื่อเสียงในนามสถาบัน\nT3.ทุนผู้ทำคุณประโยชน์ให้แก่สถาบัน\nT4.ทุนสนับสนุนการนำเสนอผลงานวิชาการ\nT5.ทุนสนับสนุนการแลกเปลี่ยนและฝึกงานต่างประเทศ"
					elif entity == 'S2:S2' and intents == 'sec_1':
						response = "ทุนสนับสนุนการศึกษา\nE1.ทุนอุดหนุนการศึกษาประเภท ก.\nE2.ทุนอุดหนุนการศึกษาประเภท ข.\nE3.ทุนสนับสนุนนักศึกษาในภาวะวิกฤติ\nE4.ทุนให้ยืมเพื่อการศึกษากรณีฉุกเฉิน\nE5.ทุนช่วยเหลือนักศึกษาในสถานการณ์การแพร่ระบาดของโรค COVID 19"
					elif entity == 'two:two' and intents == 'number':
						response = "ทุนกยศ.\nK1.คุณสมบัติสำหรับการขอกู้กยศ.\nK2.รายละเอียดของทุนกยศ.\nK3.เอกสารประกอบการกู้กยศ.\nK4.กำหนดการการกู้กยศ."
					elif entity == 'three:three' and intents == 'number':
						response = "กรุณาพิมพ์คำถามแล้วแอดมินจะติดต่อกลับให้เร็วที่สุดค่ะหรือติดต่อได้ที่ 02-xxxxx"
					elif entity == 'P_K:P_K' and intents == 'property_KYS':
						response = "ติดตามรายละเอียดเพิ่มเติมได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751617-557051c0-5791"
					elif entity == 'D_K:D_K' and intents == 'detail_KYS':
						response = "กยศ. ลักษณะที่ 1 ขาดแคลนทุนทรัพย์\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา)\n-ค่าครองชีพ 2,400 บาท/เดือน *ตามที่นักศึกษาประสงค์ขอกู้ยืม\n-กยศ. ลักษณะที่ 2\n-ศึกษาในสาขาวิชาที่เป็นความต้องการหลักซึ่งมีความชัดเจนของการผลิตกำลังคนและมีความจำเป็นต่อการพัฒนาประเทศ\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา) \n-ค่าครองชีพ 2,400 บาท/เดือน *หากจะกู้ยืมค่าครองชีพ จะต้องเป็นผู้มีรายได้รวมของครอบครัวไม่เกิน 200,000 บาทต่อปี\nอ่านรายละเอียดเพิ่มเติมได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124714090-5249f1f4-4a57"
					elif entity == 'Do_K:Do_K' and intents == 'Document_KYS':
						response = "สามารถดูรายละเอียดได้ที่ \nhttps://office.kmitl.ac.th/osda/studentloan/#1562124714078-a8a6b529-77ac"
					#elif entity == 'dcm_of_k:dcm_of_k':
					#	response = "สามารถดูรายละเอียดได้ที่ \nhttps://office.kmitl.ac.th/osda/studentloan/#1562124714078-a8a6b529-77ac"
					elif entity == 'T_K:T_K':
						response = "สามารถติดตามกำหนดการได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751146-e22dcd72-ed5d"
					elif entity == None or intents == None:
						response = None
						
					bot.send_text_message(sender_id, response)

	return "ok", 200


def log(message):
	print(message)
	sys.stdout.flush()


if __name__ == "__main__":
	chatbot.run(debug = True, port = 80)