import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from MCP3008 import MCP3008
from datetime import datetime

import time
while True:
    try:
        reader = SimpleMFRC522()

        
        id, text = reader.read()
        print(id)
        print(text)
    except Exception as x:
        print(x)
   