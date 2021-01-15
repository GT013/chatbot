import os
import sys
import json
import requests
import pandas as pd
from flask import Flask, request
from bot import wit_response
from pymessenger import Bot


with open('inform.json',encoding='utf8') as f:
    #s=f.read()
    obj = json.load(f)

q = input("entity : ")
t = input("intents : ")

for data in obj:
    #print(data['entity'])
        if data['entity'] == q and data['intents'] == t:
            print(data['response'])
        else:
            print("ยังไม่ได้เพิ่มหรือไม่มี")

#entity = obj[0]['entity']




   



    