from machine import I2C,Pin
import time
import ssd1306
import sys
import machine
i2c = I2C(-1,Pin(5),Pin(4))
display = ssd1306.SSD1306_I2C(128,32,i2c)
display.fill(0)
display.text("Hello World",15,0)
display.show()

