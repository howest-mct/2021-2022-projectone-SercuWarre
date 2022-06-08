import time
from RPi import GPIO
from mfrc522 import SimpleMFRC522
from MFRC522 import MFRC522
from helpers.klasseknop import Button
import threading
import spidev
import time
from MFRC522 import MFRC522
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
sensor_file_name = '/sys/bus/w1/devices/28-22c662000900/w1_slave'

# Code voor Hardware
def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)

def kaart_lezer():
    try:
        reader = SimpleMFRC522()
        while True:
                print("hi")
                id, text = reader.read()
                print(id)
                ids=str(id)
                print(text)    
                open_door()
                time.sleep(1)
                DataRepository.create_historiek(0,3,datetime.now(),0, "badge scanned")
                data=DataRepository.read_user()
                for item in data:
                    userid=item['userid']
                    if item['RFid']==ids:
                        DataRepository.create_frigo_historiek(userid,datetime.now())
            
                time.sleep(0.001)

    except  Exception as x:
        print(F"thread kaart {x}")           
        
               
def temp_inlezen():
    temp_prev=0
    try:
        while True:
            sensor_file = open(sensor_file_name)
            line = sensor_file.readlines()[-1]
            uitkomst = line[line.rfind("t"):]
            geheel = int(uitkomst[2:])
            temperatuur = geheel/1000
            if temperatuur<=temp_prev-0.5 or temperatuur>=temp_prev+0.5:
                print(f"T={temperatuur}")
                DataRepository.create_historiek(1,0,datetime.now(),temperatuur, "temperatuur Waarde")
                socketio.emit('B2F_send_temp', {'tempwaarde': temperatuur},broadcast=True)
                temp_prev=temperatuur
            time.sleep(0.001)

    except  Exception as x:
        print(F"thread temp {x}")
def get_ip():
    # perv_wifi=""
    try:
        while True:
            ip=check_output(['hostname','--all-ip-addresses'])
            # print(ip)
            wifi=str(ip[16:30])
            # print(wifi)
            socketio.emit('B2F_send_ip',wifi,broadcast=True)
            time.sleep(0.001)
    except  Exception as x:
        print(F"thread ip {x}")
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
    status=DataRepository.read_historiek()
    for item in status:
        # print(item)
        # print("/n")
        datum=str(item['actiedatum'])
        item['actiedatum']=datum
        # print(item)
        socketio.emit('B2F_historiek',  item)

   
   





@socketio.on('F2B_sent')
def listenToBtn(data):
    open_door()




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
    try:
        GPIO.output(6, GPIO.HIGH)
        DataRepository.create_historiek(0,2,datetime.now(),1, "deur open")
        print("deur open")
        time.sleep(3)
        GPIO.output(6, GPIO.LOW)
        DataRepository.create_historiek(0,1,datetime.now(),0, "deur toe")
        print("deur toe")
        time.sleep(0.001)
    
    except  Exception as x:
        print(F"thread deur {x}")
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
        start_ip_thread()
        start_rfid_thread()

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

