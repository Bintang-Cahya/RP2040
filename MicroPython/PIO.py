from machine import Pin
from time import sleep
import rp2

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def blink():
    wrap_target()
    set(pins, 1)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    set(pins, 0)   [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    nop()          [31]
    wrap()

# State Machine (0), Program blink(), frekuensi 2KHz, base pin 25
sm = rp2.StateMachine(0, blink, freq=2000, set_base=Pin(25))

while True:
    sm.active(1)
    sleep(2)
    sm.active(0)
    sleep(2)