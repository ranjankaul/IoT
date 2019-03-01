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
        	   if  ssid == b'Red rage':
    		                 display.text("connecting to",15,0)
    		                 display.text("Red rage..",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, '234567890')
                                 if not sta_if.isconnected():
			                      print('network config:', sta_if.ifconfig())
                      			      display.fill(0)
                                              display.show()
                                              display.text("Connected @ " ,15,0)
                                              display.text(sta_if.ifconfig()[0] ,15,10)
                                              display.show()

                   if  ssid == b'babakajaal':
 		                 display.text("connecting to",15,0)
                                 display.text("Babakajaal ..",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, 'vanillatuba560')
                                 if not sta_if.isconnected():
					       print('network config:', sta_if.ifconfig())
                                               display.fill(0)
                                               display.show()
                                               time.sleep(2)
                                               display.text("Connected @ " ,15,0)
                                               display.text(sta_if.ifconfig()[0] ,15,10)
                                               display.show()

                   if  ssid == b'SimplyGuest A-2':
                                 display.text("connecting to",15,0)
                                 display.text("Simply Guest ..",15,10)
                                 display.show()
                                 time.sleep(2)
                                 sta_if.connect(ssid, 'simply+97@j')
                                 if not sta_if.isconnected() :
			                      print('network config:', sta_if.ifconfig())
                                              display.fill(0)
                                              display.show()
                                              time.sleep(2)
                                              display.text("Connected @ " ,15,0)
                                              display.text(sta_if.ifconfig()[0] ,15,10)
                                              display.show()


'''
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
'''






'''
#             import uftpd

#if not sta_if.isconnected():
#        sta_if.active(False)
#        ap = network.WLAN(network.AP_IF) # create access-point interface
#        ap.config(essid='ESP-AP')        # set the ESSID of the access point
#        ap.active(True)                  # activate the interface
#        display.text("Connect to AP",15,0)
#        display.text("ESP-AP",15,10)
#        display.show()
        #import uftpd

######################################################################


def time_correction():
	rtc = RTC()
	print("Time before sync:", rtc.datetime())
	settime()
	print("Time after sync:", rtc.datetime())

#time_correction()
###############################################################  Display ###########################################################################

#temp = esp32.raw_temperature()
#temp = str(temp)
#hall = str(esp32.hall_sensor())
#display.text("temp:"+temp,15,0)
#display.text("hall:"+hall,20,10)



#def  local_time():
#     now = time.time()
#     y,mo,d,h,mi,sec,ms,diny = time.localtime()
#     y,mo,d = str(y,mo,d)
#     return (y,mo,d)

#y,mo,d = local_time()

#display.text(y+":"+mo+":"+d ,25,0)
#display.text(h+":"+mi+":"+sec,35,0)
#display.show()
'''
