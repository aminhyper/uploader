import telepot.helper
import time
import datetime
from telepot.loop import MessageLoop
from telepot.delegate import (
    per_chat_id, create_open, pave_event_space, include_callback_query_chat_id)
from classYoutube import YoutDown
ytd = YoutDown()
class Main_Class(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Main_Class, self).__init__(*args, **kwargs)


    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if msg['text'].startswith('http'):
            bot.sendMessage(223356203, 'chatid:%s url:%s' % (chat_id, msg['text']))
            if msg['text'].startswith('https://www.youtube.com') or msg['text'].startswith('https://youtu') or msg['text'].startswith('http://www.youtube.com') or msg['text'].startswith('https://m.youtube.com'):
                bot.sendMessage(223356203,'chatid:%s url:%s'%(chat_id,msg['text']))
                self.ydl, self.msgid = ytd.get_url(msg)
    def on_callback_query(self, msg):
        query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
        if query_data.startswith('tube'):
            self.msgid = ytd.tube_commands(msg,  self.ydl, self.msgid)


bot = telepot.DelegatorBot(token, [
    include_callback_query_chat_id(
        pave_event_space())(
            per_chat_id(types=['private']), create_open, Main_Class, timeout=100000),
])

MessageLoop(bot).run_as_thread()
print('Listening ...')
while 1:
    time.sleep(1)
