# **Micropythings**
Repo for misc micropython


## **Etherum Sell price to display**
**File:** [ethsell.py](ethsell.py)

First Gets Etherum sell price from Coinbase API and prints it (in Euros) in a Matrix dot display every 60 seconds.


**Links:**
+ [Coinbase API Prices endpoint](https://developers.coinbase.com/api/v2#prices)
+ [urequest](https://makeblock-micropython-api.readthedocs.io/en/latest/public_library/Third-party-libraries/urequests.html)
+ [max7129](https://github.com/jgbrown32/ESP8266_MAX7219)


**Hardware used:**
+ Wemos D1 Mini [Amazon](https://www.amazon.es/dp/B01N9RXGHY/)
+ Matix 4x32 Display [Amazon](https://www.amazon.es/dp/B079HVW652/)
+ x5 Jumper Wires [Amazon](https://www.amazon.es/dp/B074P726ZR/)

### **Wires Setup**
|Wemos|Display|
|-|-|
|5V|VCC|
|GND|GND|
|D5|CLK|
|D7|DIN|
|D8|CS|




