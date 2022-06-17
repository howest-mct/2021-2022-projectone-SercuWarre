import time
from tkinter import image_types
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
import os
from selenium import webdriver
        
        

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
sensor_file_name = '/sys/bus/w1/devices/28-03219779d03f/w1_slave'

# Code voor Hardware
def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.LOW)
    GPIO.setup (21, GPIO .IN, pull_up_down = GPIO.PUD_UP)


def kaart_lezer():
    try:
        reader = SimpleMFRC522()
        while True:
                # print("hi")
                id, text = reader.read()
                print(id)
                ids=str(id)
                print(text)   
                open_door()
                socketio.emit('B2F_user',{'user':ids},broadcast=True)
                DataRepository.create_historiek(0,3,datetime.now(),0, "badge scanned")
                # time.sleep(1)
                # data=DataRepository.read_user()
                # for item in data:
                #     userid=item['userid']
                #     name=item['naam']
                #     # print(name)
                #     if item['RFid']==ids:
                #         # DataRepository.create_frigo_historiek(userid,text,datetime.now())
            
                time.sleep(0.001)

    except  Exception as x:
        print(F"thread kaart {x}")           
        
               
def temp_inlezen():
    temp_prev=0
    # try:  
    while True:
        sensor_file = open(sensor_file_name)
        line = sensor_file.readlines()[-1]
        # print(line)
        uitkomst = line[line.rfind("t"):]
        # print(uitkomst)
        geheel = int(uitkomst[2:])
        temperatuur = geheel/1000
        if temperatuur<=temp_prev-0.08 or temperatuur>=temp_prev+0.08 :
            print(f"T={temperatuur}")
            DataRepository.create_historiek(1,0,datetime.now(),temperatuur, "temperatuur Waarde")
            socketio.emit('B2F_send_temp', {'tempwaarde': temperatuur},broadcast=True)
            temp_prev=temperatuur
        time.sleep(0.001)

    # except  Exception as x:
        # print(F"thread temp {x}")
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
    print("hi")
    print('A new client connect')
    # # Send to the client!

@app.route('/users')
def user():
    return  jsonify( DataRepository.read_user())

@app.route('/drinks')
def drinks():
    return jsonify(DataRepository.Read_drinks())
@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    
   
   
@socketio.on('F2B_power')
def power():
    print("shutting down")
    # os.system("sudo shutdown -h now") +




@socketio.on('F2B_sent')
def listenToBtn(data):
    open_door()

@socketio.on('F2B_update_min_fridge')
def updatefridge(data):
    print(data)
    dict=data['dict']
    user=dict['users']
    bieren=[dict['bier']]
    print(bieren)
    teller=1
    for item in bieren:
        for i in item:
            print(i)
            if i !='0':
                DataRepository.create_frigo_historiek(user,teller,datetime.now(),i)
                DataRepository.update_drinks_min(i,teller)
            teller+=1
@socketio.on('F2B_update_plus_fridge')
def update_fridge(data):
    # print(data)
    dict=data['dict']
    bier=[dict['bier']]
    # print(bieren)
    teller=1
    for item in bier:
        for i in item:
            # print(i)
            if i !='0':
                DataRepository.update_drinks_plus(i,teller)
            teller+=1
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

def stuur_data():
    while True:
        status=DataRepository.read_historiek()
        users=DataRepository.read_frigo_historiek()
        bar=DataRepository.read_bar()
        frigoLijst=[]
        lijst=[]
        barlijst=[]
        for b in bar:
            aantal=str(b['aantal'])
            b['aantal']=aantal
            date=str(b['datum'])
            b['datum']=date
            barlijst.append(b)
        socketio.emit('B2F_bar_grafiek',barlijst)
        for i in users:
            
            date=str(i['datum'])
            i['datum']=date
            frigoLijst.append(i)
        socketio.emit('B2F_frigo_historiek',frigoLijst)
        for item in status:
            # print(item)
            # print("/n")
            datum=str(item['actiedatum'])
            item['actiedatum']=datum
            # print(item)
            lijst.append(item)
        socketio.emit('B2F_historiek',  lijst)
        items=DataRepository.read_temp()
        waarde=[]

        for i in items:
            datum=str(i['actiedatum'])
            i['actiedatum']=datum
            waarde.append(i)
        waarde.reverse()
        socketio.emit('B2F_temp_chart',{'waarde':waarde},broadcast=True)
        
        time.sleep(5)
def open_door():
    try:
        socketio.emit('B2F_Frigo') 
        GPIO.output(6, GPIO.HIGH)
        DataRepository.create_historiek(0,2,datetime.now(),1, "deur open")
        print("deur open")
        input = GPIO.input (21)
        while input!=1:
            input = GPIO.input (21)
            print (input)
            time.sleep (0.2)
        
        time.sleep(1)
        GPIO.output(6, GPIO.LOW)
        DataRepository.create_historiek(0,1,datetime.now(),0, "deur toe")
        print("deur toe")
        time.sleep(0.001)
    
    except  Exception as x:
        print(F"deur {x}")
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

def start_send_data_thread():
    print("**** Starting send data ****")
    data = threading.Thread(target=stuur_data, args=(), daemon=True)
    data.start()
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
        start_send_data_thread()
        # time.sleep(2)
        
        print("**** Starting APP ****")
        stop=time.time()
        print(stop-start)
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
        GPIO.cleanup()

    finally:
        GPIO.cleanup()

