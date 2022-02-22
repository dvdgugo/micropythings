import tm1637
from time import sleep
from machine import Pin, PWM

tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))
bz = PWM(Pin(14))

mins = 0
segs = 0
br = 300
rt = 5

def beep(n,l,s):
    
    bz.freq(500)
    for x in range(n):          # n repeats
        bz.duty_u16(1000)  
        sleep(l)                # l beep duration
        bz.duty_u16(0)
        sleep(s)                # s silence duration


def count(m,s,b,r):
    while r > 0: 
        while s < 60:
            tm.numbers(m,s)
            s+=1
            sleep(1)

        if s == 60:
            m+=1
            s=0

        if m == 25:
            beep(1,1,0)
            while b > 0 :
                tm.number(b)
                sleep(1)
                b-=1

            if b == 0:
                s = 0
                m = 0
                b = 300
                r-= 1
    
    tm.hex(0xdead)
    
beep(3,0.2,0.1)
count(mins,segs,br,rt)