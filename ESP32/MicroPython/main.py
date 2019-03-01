from machine import I2C,Pin
import time
import esp32
import ssd1306
import network
import sys
import machine
import utime
from machine import RTC
from machine import idle
import ntptime
from ntptime import settime
from dht import DHT22

############################################################## Display - Initial_Setting ###########################################################
i2c = I2C(-1,Pin(5),Pin(4))
display = ssd1306.SSD1306_I2C(128,32,i2c)
############################################################## Network - Settings ##################################################################
sta_if = network.WLAN(network.STA_IF)

if not sta_if.isconnected():
          sta_if.active(True)
          wifis = sta_if.scan()
          print(wifis)
          for wifi in wifis:
        	   ssid = wifi[0]
        	   if  ssid == b'ssid*':
    		                 display.text("connecting to",15,0)
    		                 display.text("ssid",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, 'Password')
                                 if not sta_if.isconnected():
			                      print('network config:', sta_if.ifconfig())
                      			      display.fill(0)
                                              display.show()
                                              display.text("Connected @ " ,15,0)
                                              display.text(sta_if.ifconfig()[0] ,15,10)
                                              display.show()

                   if  ssid == b'ssid*':
 		                 display.text("connecting to",15,0)
                                 display.text("ssid*",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, 'password')
                                 if not sta_if.isconnected():
					       print('network config:', sta_if.ifconfig())
                                               display.fill(0)
                                               display.show()
                                               time.sleep(2)
                                               display.text("Connected @ " ,15,0)
                                               display.text(sta_if.ifconfig()[0] ,15,10)
                                               display.show()

                   if  ssid == b'ssid':
                                 display.text("connecting to",15,0)
                                 display.text("ssid*",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, 'password')
                                 if not sta_if.isconnected() :
			                      print('network config:', sta_if.ifconfig())
                                              display.fill(0)
                                              display.show()
                                              time.sleep(2)
                                              display.text("Connected @ " ,15,0)
                                              display.text(sta_if.ifconfig()[0] ,15,10)
                                              display.show()


display.fill(0)
display.show()
sensor = DHT22(Pin(15,Pin.IN,Pin.PULL_UP))
while True:
      display.fill(0)
      display.show()
      sensor.measure()
      t = sensor.temperature()
      h = sensor.humidity()
      t = str(t)
      h = str(h)     
      display.text("temp : "+t,15,0)
      display.text("humid: "+h,15,10)
      display.show()
      print(t,h)
      time.sleep(4)







