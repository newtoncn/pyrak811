from sys import exit
from time import time, sleep
from rak811 import Mode, Rak811
import traceback as tb

def test_rak_construct():
    '''
    Test Instantiation
    :return:
    '''
    lora = Rak811()

def test_rak_mode():
    lora = Rak811()

    lora.mode = Mode.LoRaP2P

def test_rak_send_command():
    lora = Rak811()

    lora.mode = Mode.LoRaP2P

    lora.txc(b'ffffff')

def test_rak_rec_command():
    lora = Rak811()

    wait_time = 20

    lora.mode = Mode.LoRaP2P

    lora.rx_get(wait_time)