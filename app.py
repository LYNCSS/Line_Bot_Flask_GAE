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
line_bot_api = LineBotApi('g3ywxE0lX42Mwt1T+kxVxlCuAcTefdnQjiyEgszbOOf1BR6BVovAIdoo2HSnxgOzW9sU79MgRFQTRvG1LQXa3K6xMVrL1XFjIWw+x1rfNsIjwInfiyjF2U4jra2G+1ZzCdWoEcELiyxmi3BJCl6F0wdB04t89/1O/w1cDnyilFU=')
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



# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text) #Encode event.message.text into which api can recognized
    line_bot_api.reply_message(event.reply_token, message) #reply encoded message as message to line server

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
