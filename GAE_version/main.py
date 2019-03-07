from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('x1bKztnJMLSChnta0jYtKZMWljs7ETgWuw5CEm7cM5mKmAM438HL1RZURFBjUuAyW9sU79MgRFQTRvG1LQXa3K6xMVrL1XFjIWw+x1rfNsKmTwgOwbD/W3yDhL56eAaXhMlbWKaF+pNMQHzDanQfQQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('793043c0f8f8c9db13acf3603599ee8a')



# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
@app.route("/")
def hello():
    return "<h1>Hello World</h1>"



# 處理訊息
@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
    #msg_file = open(r'Reply_Message\No_Such_Service.txt')
    msg = open(r'Rply_Msg/No_Such_service.txt', 'r').read()
    message = TextSendMessage(text=msg) #Encode event.message.text into which api can recognized
    line_bot_api.reply_message(event.reply_token, message) #reply encoded message as message to line server

@handler.add(MessageEvent, message=TextMessage)
def handle_textmessage(event):
    msg = open(r'Rply_Msg/No_Such_service.txt', 'r').read()
    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(event.reply_token, message)
    


    
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
