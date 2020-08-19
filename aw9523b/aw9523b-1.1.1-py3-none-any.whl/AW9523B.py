#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author             : Jam
# @Fiel Name          : AW9523B.py
# @Create Date        : 2020-08-14 10:42:48
# @Last Modified by   : magic-office-05
# @Last Modified time : 2020-08-14 10:54:13

from enum import Enum, auto
import time
import Adafruit_GPIO.I2C as i2c
import RPi.GPIO as GPIO

class Port0(Enum):
    PIN0 = 0
    PIN1 = 1
    PIN2 = 2
    PIN3 = 3
    PIN4 = 4
    PIN5 = 5
    PIN6 = 6
    PIN7 = 7

class Port1(Enum):
    PIN0 = 0
    PIN1 = 1
    PIN2 = 2
    PIN3 = 3
    PIN4 = 4
    PIN5 = 5
    PIN6 = 6
    PIN7 = 7

class AW9523B(object):
    """docstring for AW9523B."""
    class Register(Enum):
        INPUT_PORT0 = 0x00
        INPUT_PORT1 = auto()
        OUTPUT_PORT0 = auto()
        OUTPUT_PORT1 = auto()
        CONFIG_PORT0 = auto()
        CONFIG_PORT1 = auto()
        INT_PORT0 = auto()
        INT_PORT1 = auto()
        ID = 0x10
        CTL = auto()
        MS0 = auto()
        MS1 = auto()
        DIM0 = 0x20
        DIM1 = auto()
        DIM2 = auto()
        DIM3 = auto()
        DIM4 = auto()
        DIM5 = auto()
        DIM6 = auto()
        DIM7 = auto()
        DIM8 = auto()
        DIM9 = auto()
        DIM10 = auto()
        DIM11 = auto()
        DIM12 = auto()
        DIM13 = auto()
        DIM14 = auto()
        DIM15 = auto()
        SW_RSTN = 0x7f

    INPUT = LOW = False
    OUTPUT = HIGH = True
    inputCB = None
    outputList = list(Port0)+list(Port1)
    inputList = list()
    def __init__(self, addr=0x58,intPin=27):
        super(AW9523B, self).__init__()
        GPIO.setmode(GPIO.BCM)
        self.intPin = intPin
        self.addr = addr
        self.setAddr(addr)

        if self.isConnected():
            self.softReset()
            time.sleep(.1)

        GPIO.setup(self.intPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.intPin, GPIO.FALLING, callback=self.intCB)
        #clean interrupt
        self.readInput()

    def setIntPin(self,pinBCM):
        GPIO.remove_event_detect(self.intPin)
        GPIO.cleanup(self.intPin)
        self.intPin = pinBCM
        GPIO.setup(self.intPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.intPin, GPIO.FALLING, callback=self.intCB)
        #clean interrupt
        self.readInput()

    def intCB(self,channel):
        pin = self.readInput()
        if pin and self.inputCB:
            self.inputCB(pin)

    def setAddr(self, addr):
        self.addr=addr
        self.bus = i2c.get_i2c_device(addr)

    def getAddr(self):
        return self.addr

    def softReset(self):
        self.bus.write8(self.Register.SW_RSTN.value, 0x00)

    def isConnected(self):
        return self.bus.readS8(self.Register.ID.value) == 0x23

    def readInput(self):
        port0Input = self.bus.readS8(self.Register.INPUT_PORT0.value)
        port1Input = self.bus.readS8(self.Register.INPUT_PORT1.value)
        # print("port0:",hex(port0Input),"port1:",hex(port1Input))
        for x in Port0:
            if x in self.inputList and port0Input & 1 << (x.value) == 0:
                return x
        for x in Port1:
            if x in self.inputList and port1Input & 1 << (x.value) == 0:
                return x

    def setup(self, pin, gpioType, interrup=True):

        if pin in Port0:
            r1 = self.Register.CONFIG_PORT0.value
            r2 = self.Register.INT_PORT0.value
        elif pin in Port1:
            r1 = self.Register.CONFIG_PORT1.value
            r2 = self.Register.INT_PORT1.value
        else:
            return False

        conf = self.bus.readS8(r1)
        if gpioType == self.OUTPUT:
            conf &= ~(1 << pin.value)
            if not pin in self.outputList:
                self.outputList.append(pin)
                if pin in self.inputList:
                    self.inputList.remove(pin)
        elif gpioType == self.INPUT:

            intConf = self.bus.readS8(r2)
            if interrup:
                intConf &= ~(1 << pin.value)
            else:
                intConf |= (1 << pin.value)
            self.bus.write8(r2, intConf)
            conf |= (1 << pin.value)
            if not pin in self.inputList:
                self.inputList.append(pin)
                if pin in self.outputList:
                    self.outputList.remove(pin)
        self.bus.write8(r1, conf)
        return True

    def output(self, pin, value):
        if not pin in self.outputList:
            raise RuntimeError("{} has not been set up as an OUTPUT!!".format(pin))

        if pin in Port0:
            r = self.Register.OUTPUT_PORT0.value
        elif pin in Port1:
            r = self.Register.OUTPUT_PORT1.value
        else:
            return False
        conf = self.bus.readS8(r)
        if value == self.LOW:
            conf &= ~(1 << pin.value)
        elif value == self.HIGH:
            conf |= (1 << pin.value)
        else:
            return False
        self.bus.write8(r, conf)

EX_GPIO = AW9523B()

