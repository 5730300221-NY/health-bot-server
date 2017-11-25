# encoding: utf-8
from flask import Flask, request
from utils import wit_response
import json
import requests
#from db import doQuery,doInsert
#from database import docreate,insertUser

global LINE_API_KEY
LINE_API_KEY = 'Bearer 77/rUD66AxteA86L+M7a1f8KtwtcXXt98K9X9uPHNpVB6xftyxYXTOVJihjNFeOzQyOfPY6KO1BVUO974Jkjlm5FkO3JKRZkv9O/BLJLpFpCrdhkjGHLq6QFh0MaEBbM5ZZz3wb6eJtmQM8cCkz/EgdB04t89/1O/w1cDnyilFU='


app = Flask(__name__)
 
@app.route('/')
def index():
    return 'This is chatbot server.'
@app.route('/bot', methods=['POST'])

def bot():

    replyStack = list()
   

    msg_in_json = request.get_json()

    replyToken = msg_in_json["events"][0]['replyToken']
    userID = msg_in_json["events"][0]["source"]["userId"]
    msgType = msg_in_json["events"][0]["message"]["type"]

    if msgType != 'text':
        return 'OK', 200

    text = msg_in_json["events"][0]["message"]["text"].strip()

    user_detail = {}
    user_detail["id"] = userID

    rsp1,rsp2 = wit_response(text)
    #rsp = wit_response(text)
    """if(rsp1 == "age_of_person"):

        user_detail["age"] = rsp2
        rsp = insertUser(user_detail)"""

    # replyStack.append(rsp1)
    replyStack.append(rsp2)

    reply(replyToken, replyStack[:5])
    
    return 'OK',200






def reply(replyToken, textList):

    LINE_API = 'https://api.line.me/v2/bot/message/reply'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Authorization': LINE_API_KEY
    }
    msgs = []
    for text in textList:
        msgs.append({
            "type":"text",
            "text":text
        })
    data = json.dumps({
        "replyToken":replyToken,
        "messages":msgs
    })
    requests.post(LINE_API, headers=headers, data=data)
    return








if __name__ == '__main__':
    app.run()