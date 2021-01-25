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

#with TelegramClient(StringSession(), api_id, api_hash) as client:
#
#    ses_string = client.session.save()
    
# Or this (keep it saved in .env for your security reasons):
ses_string = os.getenv('ses_string')
    
keep_alive()

alph = ['a','b','c','d','e','f','g','h','i','g','k','A','B','D','C','E','G','F','x','X','v','V','w','W','l','L','m','M','n','N','R','r','q','Q','p','P','j','J','s','S','z','Z']
with TelegramClient(StringSession(ses_string), api_id, api_hash) as client:
    while True:
        try:
            # Waits 20000 seconds (~5.5 hours) each iteration, wait time is enormous since FloodWaitErrors are irritating. THAT should be enough I hope. 
            time.sleep(20000)
            

            usernamer = ""
            for i in range(0,randrange(32-7)+7):
                usernamer+=alph[randrange(alph.__len__())]
              
            result = client(functions.account.CheckUsernameRequest(
                username=usernamer
            ))

            if result:
              print("Randomly generated username is available, it should be now changed.")
            else:
              print("Randomly generated username is already taken...")


            if not result:
              continue
            result = client(functions.account.UpdateUsernameRequest(
                username=usernamer
            ))
        except errors.FloodWaitError as e:
            print('Have to sleep ' + str(e.seconds) + ' seconds')
            time.sleep(e.seconds+10)
            





