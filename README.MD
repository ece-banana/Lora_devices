# LORA dev board
----------
## Process
- [x] simple example
- [x] set of functions to send & recieve data
- [x] make a lib for micropython
## TO DO
- [x] make a video for students
- [ ] make illustration of connection
- [x] find the dashboard apps:
### Dashboaeds
 - NodeRED (Full control)
 - Grafana (to-do)
 - io.adafruit.com (10 feed, can be grouped)
 - thingSpeak (limited sending rate)
# Addition interfaces
### Telegram, Discord
can be done through HTTP requests (urequests for micropython)
``` python
# reciever
while(True):
    if(ser.inWaiting()==8):
        a = ser.read(8)
        ser.write(a[:4])
        break
    else:
        pass
```

``` python
# sender
def test():
    a = time.monotonic()
    ser.write(b'\x00\x00\x00'+ 'hello'.encode())
    while(ser.inWaiting()<4):
        pass
    r = ser.read(4)
    b = time.monotonic()
    print(r, b-a, a,b)
```
