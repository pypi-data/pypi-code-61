from AW9523B import EX_GPIO,Port0,Port1
import time

fiveWaySwitch = [Port1.PIN7, Port1.PIN6, Port1.PIN5, Port1.PIN4, Port0.PIN7,
                    Port1.PIN0, Port1.PIN1, Port1.PIN2, Port1.PIN3, Port0.PIN0]

def inputCallback(pin):
    print("inputCallback", pin)


if __name__ == "__main__":
    for pin in fiveWaySwitch:
        EX_GPIO.setup(pin, EX_GPIO.INPUT)
    EX_GPIO.inputCB = inputCallback
    while 1:
        time.sleep(1)
