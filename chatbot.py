import os
import sys
from flask import Flask, request
from bot import wit_response
from pymessenger import Bot
import requests,json
chatbot = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAcLG6xt7eoBAJcXzEJMCDfHkn4h8QlU0WHaDJSnHH54G1rNQJzaZAe5GzVqBIeSDzYJ1vcAh3Q7XL03aYKG5g7l9dNzfWcz0b2wDnIwg6bSigVwgpFiVGIRO6Urtzlj2ZA1KfM5I75NKh5RzI05GMCaPAd1C8bJVAL4cyigZDZD"

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
                    response=None
                    rsp = None
                    entity, intents = wit_response(messaging_text)    
            
                    #############################################################

                    
                    url = requests.get("https://raw.githubusercontent.com/GT013/information/main/databasebot.json")
                    json_string = url.content
                    infor = json.loads(json_string)
                    
                    for obj in infor:

                        E1 = obj['entity1']
                        E2 = obj['entity2']
                        G1 = obj['intents1']
                        G2 = obj['intents2']

                        if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
                            response = obj['response1']     
                            break    
                        else:
                            response=None
                            #response = "แชทบอทสวัสดีค่ะ😃 สอบถามเรื่องอะไรดีคะ\nพิมพ์ 1.เรื่องทุนต่าง ๆ ของสถาบัน\nพิมพ์ 2.ทุนกยศ.\nพิมพ์ 3.ติดต่อแอดมิน\nกรุณาพิมพ์หมายเลขที่ต้องการจะสอบถาม"                        
                    bot.send_text_message(sender_id, response)

                    for obj2 in infor:

                        E1 = obj2['entity1']
                        E2 = obj2['entity2']
                        G1 = obj2['intents1']
                        G2 = obj2['intents2'] 

                        if E1 == entity and G1 == intents or E2 == entity and G2 == intents or intents == "greeting":
                            rsp = obj2['response2']
                            break
                    bot.send_text_message(sender_id, rsp)
                    
                 #############################################################

    return "ok", 200


def log(message):
    print(message)
    sys.stdout.flush()


if __name__ == "__main__":
    chatbot.run(debug=True, port=80)