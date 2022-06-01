import time
from RPi import GPIO
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




# Code voor Hardware
def setup_gpio():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(6, GPIO.OUT)
    GPIO.output(6, GPIO.HIGH)
    # temp_inlezen()
    
  

def temp_inlezen():
    temp_prev=0
    while True:
        mcp=MCP3008()
        x = mcp.read()
        # print(x)
        temp_c = round((x* 3.3/1023)*100, 2)
        # Print both temperatures
        time.sleep(1)
        if temp_c != temp_prev:
            DataRepository.create_historiek(1,datetime.now(),temp_c, "temperatuurwaarde")
            print(F'Temp: {temp_c}ºC {datetime.now()} ')
            socketio.emit('B2F_send_temp', {'tempwaarde': temp_c},broadcast=True)
        temp_prev=temp_c


def get_ip():
    # perv_wifi=""
    while True:
        ip=check_output(['hostname','--all-ip-addresses'])
        # print(ip)
        wifi=str(ip[16:30])
        # print(wifi)
        socketio.emit('B2F_send_ip',wifi,broadcast=True)
        
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
    # vraag de status op van de lampen uit de DB
    # waarde = temp_inlezen()
    # return  f"{waarde}"


@socketio.on('connect')
def initial_connection():
    print('A new client connect')
    
    # # Send to the client!
    # vraag de status op van de lampen uit de DB
   


# def sent_temp():
#     waarde = temp_inlezen()
#     emit('B2F_connected', {'tempwaarde': waarde},broadcast=True)



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

# START een thread op. Belangrijk!!! Debugging moet UIT staan op start van de server, anders start de thread dubbel op
# werk enkel met de packages gevent en gevent-websocket.
# def all_out():
#     while True:
#         print('*** We zetten alles uit **')
#         DataRepository.update_status_alle_lampen(0)
#         GPIO.output(ledPin, 0)
#         status = DataRepository.read_status_lampen()
#         socketio.emit('B2F_status_lampen', {'lampen': status})
#         time.sleep(15)

# def start_thread():
#     print("**** Starting THREAD ****")
#     thread = threading.Thread(target=temp_inlezen, args=(), daemon=True)
#     thread.start()


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
# ANDERE FUNCTIES


if __name__ == '__main__':
    try:
        start=time.time()
        setup_gpio()
        start_chrome_thread()
        # start_thread()
        start_ip_thread()
        start_temp_thread()
    
        stop=time.time()
        
        print(stop-start)
        print("**** Starting APP ****")
        socketio.run(app, debug=False, host='0.0.0.0')
    except KeyboardInterrupt:
        print ('KeyboardInterrupt exception is caught')
    finally:
        GPIO.cleanup()

