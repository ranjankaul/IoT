import network
wlan = network.WLAN(network.STA_IF)
a = wlan.scan()
for a in range(len(a)):
      print((a[0][0]))
