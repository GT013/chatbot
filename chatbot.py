import os
import sys
import json
import requests
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
                    rsp =None
                    #############################################################
                    url = requests.get("https://raw.githubusercontent.com/GT013/chatbot/master/i.json")
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
                        else:
                            response = "แชทบอทสวัสดีค่ะ😃 สอบถามเรื่องอะไรดีคะ\n1.ทุนต่าง ๆ ของสถาบัน\n2.ทุนกยศ.\n3.ติดต่อแอดมิน\nกรุณาพิมพ์หมายเลขที่ต้องการจะสอบถาม"                        

                    bot.send_text_message(sender_id, response)

                    for obj2 in infor:

                        E1 = obj2['entity']['E1']
                        E2 = obj2['entity']['E2']
                        G1 = obj2['intents']['I1']
                        G2 = obj2['intents']['I2'] 

                        if E1 == entity and G1 == intents or E2 == entity and G2 == intents:
                            rsp = obj2['rsp']
                            break
                    bot.send_text_message(sender_id, rsp)
                    
                    
                    answer = None
                    response3 = None
                    if entity == 'three:three' and intents == 'number':  
                        response3 = input("พิมพ์คำถามทิ้งไว้แล้วแอดมินจะติดกลับให้เร็วที่สุดค่ะหรือติดต่อได้ที่\n📞โทร : 02-xxx-xxxxx\n📧 E-mail : admin@kmitl.ac.th")
                        bot.send_text_message(sender_id, response3)
                        answer = "แล้วจะติดต่อกลับค่ะ ^^"  
                        bot.send_text_message(sender_id, answer)        
                    else:
                        pass

                    
                    
                    
                        
                        

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    chatbot.run(debug=True, port=80)
