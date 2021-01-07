from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    print("hey?")
    return "Hello. I am alive!"

def run():
  print("i think im alive?")
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    print("wha")
    t = Thread(target=run)
    t.start()