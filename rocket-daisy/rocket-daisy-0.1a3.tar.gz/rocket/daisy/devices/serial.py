
import os
import fcntl
import struct
import termios

from rocket.daisy.devices.bus import Bus
from rocket.daisy.decorators.rest import request, response

TIOCINQ   = hasattr(termios, 'FIONREAD') and termios.FIONREAD or 0x541B
TIOCM_zero_str = struct.pack('I', 0)

class Serial(Bus):
    def __init__(self, device="/dev/ttyAMA0", baudrate=9600):
        if not device.startswith("/dev/"):
            device = "/dev/%s" % device
        
        if isinstance(baudrate, str):
            baudrate = int(baudrate)

        aname = "B%d" % baudrate
        if not hasattr(termios, aname):
            raise Exception("Unsupported baudrate")
        self.baudrate = baudrate

        Bus.__init__(self, "UART", device, os.O_RDWR | os.O_NOCTTY)
        fcntl.fcntl(self.fd, fcntl.F_SETFL, os.O_NDELAY)
        
        #backup  = termios.tcgetattr(self.fd)
        options = termios.tcgetattr(self.fd)
        # iflag
        options[0] = 0

        # oflag
        options[1] = 0

        # cflag
        options[2] |= (termios.CLOCAL | termios.CREAD)
        options[2] &= ~termios.PARENB
        options[2] &= ~termios.CSTOPB
        options[2] &= ~termios.CSIZE
        options[2] |= termios.CS8

        # lflag
        options[3] = 0

        speed = getattr(termios, aname)
        # input speed
        options[4] = speed
        # output speed
        options[5] = speed
        
        termios.tcsetattr(self.fd, termios.TCSADRAIN, options)
        
    def __str__(self):
        return "Serial(%s, %dbps)" % (self.device, self.baudrate)
    
    def __family__(self):
        return "Serial"
    
    def available(self):
        s = fcntl.ioctl(self.fd, TIOCINQ, TIOCM_zero_str)
        return struct.unpack('I',s)[0]
    
    @request("GET", "")
    @response("%s")
    def readString(self):
        if self.available() > 0:
            return self.read(self.available()).decode()
        return ""
    
    @request("POST", "", "data")
    def writeString(self, data):
        if isinstance(data, str):
            self.write(data.encode())
        else:
            self.write(data)
