from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

ayy = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('czuy7XcbD0Lvr8Tvnp0jdDRIK+vXW31FyV1PfMxMua7DhvGDyMrdKHyBxVYQwGBzW9sU79MgRFQTRvG1LQXa3K6xMVrL1XFjIWw+x1rfNsIFjpYi52zzzpqCIujrspNYxhMZ3Iwa/gCFsPkwZD4zmgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('793043c0f8f8c9db13acf3603599ee8a')



# 監聽所有來自 /callback 的 Post Request
@ayy.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    ayy.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #msg_file = open(r'Reply_Message\No_Such_Service.txt')
    msg = '您好，城翔早午餐目前尚無提供回復對話的功能，不過我們有提供下列功能:'
    message = TextSendMessage(text=msg) #Encode event.message.text into which api can recognized
    line_bot_api.reply_message(event.reply_token, message) #reply encoded message as message to line server

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    ayy.run(host='0.0.0.0', port=port)
