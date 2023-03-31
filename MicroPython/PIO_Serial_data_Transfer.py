from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
from time import sleep

@asm_pio(sideset_init=(PIO.OUT_LOW, PIO.OUT_LOW), out_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_RIGHT, 
 autopull=True, pull_thresh=8)
def prog():
    pull()   .side(0)
    label("target")
    out(pins, 1)   .side(2)
    jmp(not_osre, "target") .side(0)
    nop()   .side(1)

sm = StateMachine(0, prog, freq=100000000, sideset_base=Pin(2), out_base=Pin(0))
#Serial data output
sm.active(1)
for i in range (129):
    sm.put(i)
    #print(i)
    #sleep(0.001)
