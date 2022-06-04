# example of forcefully closing a thread with an exception
from random import random
from time import sleep
from threading import Thread
import sys
 
# task function
def task():
    # loop forever
    while True:
        # generate a random value between 0 and 1
        value = random()
        print(f'.{value}')
        # block
        sleep(value)
        # check if we should forcefully close the thread
        if value > 0.9:
            print('Closing thread')
            raise Exception('Stop now!')
 
# create and configure the new thread
thread = Thread(target=task)
# start the new thread
thread.start()
# wait for the thread to terminate
thread.join()
# main continues on
print('Main continuing on...')