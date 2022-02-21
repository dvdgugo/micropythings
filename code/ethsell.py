from machine import Pin, SPI
import max7219
import time
import urequests
import json
import network


#TODO: Maybe add try deepsleep and use battery / Test other cryptos

spi = SPI(1, baudrate=10000000)
display = max7219.Max7219(32, 8, spi, Pin(15))

# Change this to real things before use, pls
wifissid = 'NotRealssid'
wifipass = 'NotRealwpa'
sta_if = network.WLAN(network.STA_IF)

def get_price():
    # Get data from API
    r = urequests.get('https://api.coinbase.com/v2/prices/ETH-EUR/sell')
    
    # Parse data -> to json -> to float -> to int
    rdata = json.loads(r.text)
    dec_price = rdata['data']['amount']
    int_price = round(float(dec_price))
    
    return(dec_price,int_price)

def do_connect(wifissid,wifipass):
    #Connect to WiFI
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(wifissid, wifipass)
        while not sta_if.isconnected():
            display.marquee('Wifi Connection Failed... :(')
    else:
        pass
    
def main():

    do_connect(wifissid,wifipass)
        
    while True:

        dec_price, int_price = get_price()
        display.marquee(str(dec_price))
        display.text(str(int_price),0,0,1)
        display.show()

        time.sleep(60)
        
main()