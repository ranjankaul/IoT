from machine import I2C,Pin
import time
import esp32
import ssd1306
import network
import sys
import machine
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect('babakajaal', 'vanillatuba560')
    while not sta_if.isconnected():
        pass
        print('network config:', sta_if.ifconfig())

i2c = I2C(-1,Pin(5),Pin(4))
display = ssd1306.SSD1306_I2C(128,32,i2c)
display.fill(0)
temp = esp32.raw_temperature()
temp = str(temp)
hall = str(esp32.hall_sensor())
display.text("temp:"+temp,15,0)
display.text("hall:"+hall,20,10)
time.sleep_ms(2000)

#def  local_time():
#     import utime as time
#     now = time.time()
#     y,mo,d,h,mi,sec,ms,diny = time.localtime()
#     y,mo,d = str(y,mo,d)
#     return (y,mo,d)

#y,mo,d = local_time()

#display.text(y+":"+mo+":"+d ,25,0)
#display.text(h+":"+mi+":"+sec,35,0)
display.show()
