# +---------------------------------------------------------------------------+
#
#      Program:    direction_converter.py
#
#      Purpose:    translation table
#                  referenced by the RC skidloader webiopi adapter				
#      
#      Target:     ARMV61A
#
#      Author:     Martin Shishkov
#
#      License:    GPL 3
# +---------------------------------------------------------------------------+

from enum import IntEnum
class directions(IntEnum):
    Ahead     = 0
    Left      = 1
    Right     = 2
    Stop      = 3
    Backward  = 4
    ArmUp     = 5
    ArmDown   = 6
    TiltUp    = 7
    TiltDown  = 8
    Lights	  = 9
    Camera	  = 10
    Sound	  = 11
    Parked	  = 12
    LR	  	  = 13


def directionToInt(direction):
    switcher = {
        "Ahead"     : directions.Ahead,
        "Left"      : directions.Left,
        "Right"     : directions.Right,
        "Stop"      : directions.Stop,
        "Backward"  : directions.Backward,
        "ArmUp"  	: directions.ArmUp,
        "ArmDown"   : directions.ArmDown,
        "TiltUp" 	: directions.TiltUp,
        "TiltDown" 	: directions.TiltDown,
        "Lights" 	: directions.Lights,
        "Camera" 	: directions.Camera,
        "Sound" 	: directions.Sound,
        "Parked" 	: directions.Parked,
        "LR" 		: directions.LR
    }
    return switcher.get(direction)
    
def directionToArray(direction):
    switcher = {
        "Ahead"     : [0x0,0xA,0x0,0x0,0xA,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "Left"      : [0x1,0xA,0x0,0x0,0x8,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "Right"     : [0x0,0xA,0x0,0x1,0x3,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "Stop"      : [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "Backward"  : [0x1,0xA,0x0,0x1,0xA,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "ArmUp"  	: [0x0,0x0,0x0,0x0,0x0,0x0,0xB,0x6,0x6,0x0,0x0,0x0,0x0,0x0,0xD],
        "ArmDown"   : [0x0,0x0,0x0,0x0,0x0,0x0,0x4,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
        "TiltUp" 	: [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x5,0x6,0x6,0x0,0x0,0xD],
        "TiltDown" 	: [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xA,0xC,0xC,0x0,0x0,0xD],
        "Lights" 	: [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xC,0xC,0xF,0xF,0xD],
        "Camera" 	: [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xF,0xF,0xD],
        "Sound" 	: [0x0,0x0,0x0,0x0,0x0,0x6,0x0,0x6,0x0,0x0,0xC,0x0,0xC,0xC,0xD],
        "Parked" 	: [0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x3,0x0,0x0,0x0,0x0,0xD],
        "DI" 		: [0x0,0x0,0x0,0x0,0x0,0x0,0x5,0x6,0x6,0xA,0xC,0xC,0x0,0x0,0x0],
        "GG" 		: [0x0,0x0,0x0,0x0,0x0,0x0,0x5,0x6,0x6,0xA,0xC,0xC,0x0,0x0,0x0],
        "ER" 		: [0x0,0x0,0x0,0x0,0xE,0x0,0xA,0x0,0x0,0xC,0x0,0x0,0x0,0x0,0xD]
    }

    #high, low = byte >> 4, byte & 0x0F
    print ("Command:----------------- ", direction, " ------------------------")
    sequence = ("".join(hex(byte & 0x0F) for byte in switcher.get(direction)))
    sequence = sequence.replace("0x", "")
    sequence = sequence.upper()
    print (sequence)
    print ("-----------------------------------------------------------")
    return (sequence)
    
def directionToJoystick(direction, L : int, R : int):
    L = int(L)
    R = int(R)
    
    switcher = {
        "LR"      	: [0x0,L,0x0,0x0,R,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xD],
    }

    #high, low = byte >> 4, byte & 0x0F
    print ("Command:----------------- ", direction, " ------------------------")
    sequence = ("".join(hex(byte & 0x0F) for byte in switcher.get(direction)))
    sequence = sequence.replace("0x", "")
    sequence = sequence.upper()
    print (sequence)
    print ("-----------------------------------------------------------")
    return (sequence)

def intToDirection(i):
    switcher = {
		directions.Ahead 		:	"Ahead",
		directions.Left 		:	"Left",
		directions.Right 		:	"Right",
		directions.Stop 		:	"Stop",
		directions.Backward 	:	"Backward",
		directions.ArmUp 		:	"ArmUp",
		directions.ArmDown 		:	"ArmDown",
		directions.TiltUp 		:	"TiltUp",
		directions.TiltDown 	:	"TiltDown",
		directions.Lights 		:	"Lights",
		directions.Camera 		:	"Camera",
		directions.Sound 		:	"Sound",
		directions.Parked 		:	"Parked",
		directions.LR 			:	"LR"
    }
    return switcher.get(i)