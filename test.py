import os
import sys
import json
import requests
import pandas as pd
from flask import Flask, request
from bot import wit_response
from pymessenger import Bot

r = requests.get('https://github.com/GT013/chatbot/blob/master/inform.json')
data=r.json()


#with open('inform.json',encoding='utf8') as f:
   # s=f.read()

   # print(s)



    