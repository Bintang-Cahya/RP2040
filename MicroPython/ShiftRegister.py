from machine import Pin
from time import sleep

data = Pin(2, Pin.OUT)
latch = Pin(3, Pin.OUT)
clock = Pin(4, Pin.OUT)

def shift(num):
    latch.low()
    for i in range(8):
        data.value(num%2)
        num = int(num/2)
        #sleep(0.01)
        clock.high()
        #sleep(0.01)
        clock.low()
    latch.high()

for x in range(129):
    shift(x)
    sleep(0.1)