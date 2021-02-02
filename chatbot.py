import os
import sys
import json
import requests
from flask import Flask, request
from bot import wit_response
from pymessenger import Bot
from numpy import random

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
                    #############################################################
                    
                    url = requests.get("https://raw.githubusercontent.com/GT013/information/main/i.json")
                    json_string = url.content
                    infor = json.loads(json_string)
                    entity, intents = wit_response(messaging_text)
                    for obj in infor:

                        E1 = obj['entity']['E1']
                        E2 = obj['entity']['E2']
                        G1 = obj['intents']['I1']
                        G2 = obj['intents']['I2']

                        if E1 == entity and G1 == intents or E2 == entity and G2 == intents:
                            response = obj['response']
                            break
                        #elif entity=="three:three" and intents == "number":
                            #response= "กรุณาพิมพ์คำถามแล้วแอดมินจะติดต่อกลับให้เร็วที่สุดค่ะหรือติดต่อได้ที่ 02-xxxxx"
                            #if messaging_event.get('message'):
                                #response = "แล้วจะติดต่อกลับให้เร็วที่สุดค่ะ ^^"
                        else:
                            response = "ลองพิมพ์ 'สวัสดี'"                        

                        bot.send_text_message(sender_id, response)

                    
                    # elif entity == 'P_K:P_K' and intents == 'property_KYS' or entity == 'k1:k1' and intents == 'T_KYS':
                        # response = "ติดตามรายละเอียดเพิ่มเติมได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751617-557051c0-5791"
                    # elif entity == 'D_K:D_K' and intents == 'detail_KYS' or entity == 'k2:k2' and intents == 'T_KYS':
                        # response = "กยศ. ลักษณะที่ 1 ขาดแคลนทุนทรัพย์\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา)\n-ค่าครองชีพ 2,400 บาท/เดือน *ตามที่นักศึกษาประสงค์ขอกู้ยืม\n-กยศ. ลักษณะที่ 2\n-ศึกษาในสาขาวิชาที่เป็นความต้องการหลักซึ่งมีความชัดเจนของการผลิตกำลังคนและมีความจำเป็นต่อการพัฒนาประเทศ\n-ค่าธรรมเนียมการศึกษา (2 ภาคการศึกษา) \n-ค่าครองชีพ 2,400 บาท/เดือน *หากจะกู้ยืมค่าครองชีพ จะต้องเป็นผู้มีรายได้รวมของครอบครัวไม่เกิน 200,000 บาทต่อปี\nอ่านรายละเอียดเพิ่มเติมได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124714090-5249f1f4-4a57"
                    # elif entity == 'Do_K:Do_K' and intents == 'Document_KYS' or entity == 'k3:k3' and intents == 'T_KYS':
                        # response = "สามารถดูรายละเอียดเอกสารที่ต้องใช้ได้ที่ \nhttps://office.kmitl.ac.th/osda/studentloan/#1562124714078-a8a6b529-77ac"
                    # elif entity == 'dcm_of_k:dcm_of_k':
                    # response = "สามารถดูรายละเอียดได้ที่ \nhttps://office.kmitl.ac.th/osda/studentloan/#1562124714078-a8a6b529-77ac"
                    #elif entity == 'T_K:T_K' or entity == 'k4:k4' and intents == 'T_KYS':
                    #response = "สามารถติดตามกำหนดการได้ที่ https://office.kmitl.ac.th/osda/studentloan/#1562124751146-e22dcd72-ed5d"

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    chatbot.run(debug=True, port=80)
