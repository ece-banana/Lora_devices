import serial
PORT = 'COM1' # name of port, on linux it maight be smth like ttyUSB0

port = serial.Serial(PORT, timeout=1) # timeout important to read empty buffer, prevents freezing

if(not port.is_open):
    port.open()
# check buffer for information
def recv(raw=0):
    if(port.in_waiting):
        if(raw):
            print(port.read(100))
        else:
            print(port.read(100).decode())
# simple function to send data
def send(s, raw=0):
    header = b'\x00\x01\x17' # header first 1st & 2nd bytes address 3rd "chan." (formula 420 + chan#) in our case 0x17 = 23 = 420 + 23 = 433 MHz 
    if(raw):
        mess = s
    else:
        mess = s.encode()
    port.write(header+mess)



