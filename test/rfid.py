import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from MCP3008 import MCP3008
from datetime import datetime

import time
temp_prev=0
while True:
    reader = SimpleMFRC522()

    
    id, text = reader.read()
    print(id)
    print(text)
    
    mcp=MCP3008()
    x = mcp.read()
    # print(x)
    temp_c = round((x* 3.3/1023)*100, 2)
    # Print both temperatures
    time.sleep(1)
    if temp_c != temp_prev:
        # DataRepository.create_historiek(1,datetime.now(),temp_c, "temperatuurwaarde")
        print(F'Temp: {temp_c}ºC {datetime.now()} ')
        # socketio.emit('B2F_send_temp', {'tempwaarde': temp_c},broadcast=True)
    temp_prev=temp_c
    time.sleep(0.001)