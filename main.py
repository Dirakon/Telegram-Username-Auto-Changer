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

# Use this (retrieve sessionString in the runtime):

with TelegramClient(StringSession(), api_id, api_hash) as client:

    ses_string = client.session.save()
    
# Or this (keep it saved in .env):
#ses_string = os.getenv('ses_string')
    

keep_alive()

alph = ['a','b','c','d','e','f','g','h','i','g','k','A','B','D','C','E','G','F','x','X','v','V','w','W','l','L','m','M','n','N','R','r','q','Q','p','P','j','J','s','S','z','Z']
with TelegramClient(StringSession(ses_string), api_id, api_hash) as client:
    while True:
        try:
            # Waits 2500 seconds (~40 minutes) each iteration
            time.sleep(10)
            


            usernamer = ""
            for i in range(0,randrange(32-7)+7):
                usernamer+=alph[randrange(alph.__len__())]
              
            result = client(functions.account.CheckUsernameRequest(
                username=usernamer
            ))

            # Prints True if the randomly generated username is available
            print(result)


            if not result:
              continue
            result = client(functions.account.UpdateUsernameRequest(
                username=usernamer
            ))
        except errors.FloodWaitError as e:
            print('Have to sleep ' + str(e.seconds) + ' seconds')
            time.sleep(e.seconds+10)
            





