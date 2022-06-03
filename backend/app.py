import time
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from helpers.klasseknop import Button
import threading
import spidev
import time
from MCP3008 import MCP3008
from flask_cors import CORS
from flask_socketio import SocketIO, emit, send
from flask import Flask, jsonify
from repositories.DataRepository import DataRepository
from datetime import datetime
from subprocess import check_output

from selenium import webdriver
        
        

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
readerstatus=0
tempstatus=0

# Code voor Hardware
def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)

    # temp_inlezen()
  
def kaart_lezer():
    global readerstatus
    while True:
        if tempstatus==0:
            # try:
                readerstatus=1
                reader = SimpleMFRC522()
                id, text = reader.read()
                print("hi")
                
                print(id)
                print(text)
                readerstatus=0
                open_door()
                time.sleep(1)
        else:
            print( F"{readerstatus} , {tempstatus}")
            time.sleep(0.5)
            # except  as x:
                # print(x)
def temp_inlezen():
    global tempstatus
    while True:
        if readerstatus==0:
            tempstatus=1
            temp_prev=0
            mcp=MCP3008()
            x = mcp.read()
            # print(x)
            temp_c = round((x* 3.3/1023)*100, 2)
            # Print both temperatures
            if temp_c != temp_prev:
                # DataRepository.create_historiek(1,datetime.now(),temp_c, "temperatuurwaarde")
                print(F'Temp: {temp_c}ºC {datetime.now()} ')
                socketio.emit('B2F_send_temp', {'tempwaarde': temp_c},broadcast=True)
                temp_prev=temp_c
                tempstatus=0
                time.sleep(1)
        else:
            print( F"{readerstatus} , {tempstatus}")
            time.sleep(0.4)

def get_ip():
    # perv_wifi=""
    while True:
        ip=check_output(['hostname','--all-ip-addresses'])
        # print(ip)
        wifi=str(ip[16:30])
        # print(wifi)
        socketio.emit('B2F_send_ip',wifi,broadcast=True)
        time.sleep(0.001)

# Code voor Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheim!'
socketio = SocketIO(app, cors_allowed_origins="*", logger=False,
                    engineio_logger=False, ping_timeout=1)

CORS(app)


@socketio.on_error()        # Handles the default namespace
def error_handler(e):
    print(e)



# API ENDPOINTS


@app.route('/')
def hallo():
    return "Server is running, er zijn momenteel geen API endpoints beschikbaar."

@app.route('/api/v1/temp/')
def temp():
    
    print('A new client connect')
    # # Send to the client!
   

@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    
    # # Send to the client!
    # vraag de status op van de lampen uit de DB
   





@socketio.on('F2B_sent')
def listenToBtn(data):
    print(data)
    print(data['status'])
    if data['status']==0:
        GPIO.output(6, GPIO.LOW)
        # print("hi")

    elif data['status']==1:
        GPIO.output(6, GPIO.HIGH)
        # print("po")
    else:
        print("fout")




def start_chrome_kiosk():
    import os

    os.environ['DISPLAY'] = ':0.0'
    options = webdriver.ChromeOptions()
    # options.headless = True
    # options.add_argument("--window-size=1920,1080")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("--disable-extensions")
    # options.add_argument("--proxy-server='direct://'")
    options.add_argument("--proxy-bypass-list=*")
    options.add_argument("--start-maximized")
    options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--kiosk')
    # chrome_options.add_argument('--no-sandbox')         
    # options.add_argument("disable-infobars")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost")
    while True:
        pass
def open_door():
    GPIO.output(6, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(6, GPIO.LOW)

def start_chrome_thread():
    print("**** Starting CHROME ****")
    chromeThread = threading.Thread(target=start_chrome_kiosk, args=(), daemon=True)
    chromeThread.start()

def start_temp_thread():
    print("**** Starting temp ****")
    tempmeasure = threading.Thread(target=temp_inlezen, args=(), daemon=True)
    tempmeasure.start()

def start_ip_thread():
    print("**** Starting ip ****")
    ipSent = threading.Thread(target=get_ip, args=(), daemon=True)
    ipSent.start()

def start_rfid_thread():
    print("**** Starting RFID ****")
    Rfid = threading.Thread(target=kaart_lezer, args=(), daemon=True)
    Rfid.start()
# ANDERE FUNCTIES


if __name__ == '__main__':
    try:
        start=time.time()
        setup_gpio()
        start_chrome_thread()
        # start_thread()
        start_temp_thread()
        time.sleep(1)
        start_rfid_thread()
        start_ip_thread()

        # time.sleep(2)
        stop=time.time()
        
        print(stop-start)
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        GPIO.cleanup()

    finally:
        GPIO.cleanup()

