from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions, types
from keep_alive import keep_alive
import asyncio
import os
import time
from random import randrange
from telethon import errors

api_id = os.getenv('app_id')
api_hash = os.getenv('app_hash')



keep_alive()

ses_string = os.getenv('ses_string')
alph = ['a','b','c','d','e','f','g','h','i','g','k','A','B','D','C','E','G','F','x','X','v','V','w','W','l','L','m','M','n','N','R','r','q','Q','p','P','j','J','s','S','z','Z']
with TelegramClient(StringSession(ses_string), api_id, api_hash) as client:
    while True:
        try:
            time.sleep(2500)
            #print("woken")
            usernamer = ""
            for i in range(0,randrange(32-7)+7):
                usernamer+=alph[randrange(alph.__len__())]
            #print(usernamer)
            result = client(functions.account.CheckUsernameRequest(
                username=usernamer
            ))
            print(result)
            if not result:
              continue
            result = client(functions.account.UpdateUsernameRequest(
                username=usernamer
            ))
        except errors.FloodWaitError as e:
            print('Have to sleep', e.seconds, 'seconds')
            time.sleep(e.seconds+10)
      #print(result)





