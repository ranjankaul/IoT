import ntptime
from machine import RTC
from ntptime import settime
rtc = RTC()
settime()
print(rtc.datetime())

