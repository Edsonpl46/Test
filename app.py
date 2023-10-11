from xmlrpc.client import NOT_WELLFORMED_ERROR
import pywhatkit
import keyboard
import time
from datetime import datetime
''
contatos =['+5581997128979']

while len(contatos) >=1:

    pywhatkit.sendwhatmsg(contatos[0],'BOLSONARO É O CARAI', datetime.now().hour,datetime.now (). minute + 2)

    del contatos [0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
