from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

line_bot_api = LineBotApi('J3qXfmH1zNrGfzzbGXURrPuTR6bxp9Jy/1127suhISMu0WQ4eXy6YgHCv4zVG0lZywGW6GfOGJ12fpXDB5Sp7GqFQ0qTArSdxz3xnhAYm4zmeqRk3AvtBR2i2YVLUo3CPKkNfzfcsijTSMvBlZT/vQdB04t89/1O/w1cDnyilFU=')
line_bot_api.push_message('Ub1ffb1538ff6e0efc6c7c0d7a977da42', TextSendMessage(text='Hello World!!!'))