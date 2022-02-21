#import tm1637
import time
#from machine import Pin, PWM
#tm = tm1637.TM1637(clk=Pin(16), dio=Pin(17))

'''
# show "12:59"
print()
tm.numbers(12, 59)

https://github.com/mcauser/micropython-tm1637
'''
mins = 0
segs = 0
b   = 300
r = 5

def count(m,s,b):
    while r > 0: 
        while s < 60:
            print(f'{m}:{s}',end="\r")
            #tm.numbers(m,s)
            s+=1
            time.sleep(1)
            
        if s == 60:
            m+=1
            s=0
        if m == 25:
            while b > 0 :
                print(str(b),end="\r")
                #tm.number(b)
            b-=1

            if b == 0:
                s = 0
                m = 0
                b = 300



count(mins,segs,b)
