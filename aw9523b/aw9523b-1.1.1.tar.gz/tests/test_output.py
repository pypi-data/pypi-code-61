from AW9523B import EX_GPIO,Port0
import time

led1 = Port0.PIN5
led2 = Port0.PIN6

EX_GPIO.setup(led1, EX_GPIO.OUTPUT)
EX_GPIO.setup(led2, EX_GPIO.OUTPUT)



if __name__ == "__main__":
    while 1:
        time.sleep(5)
        EX_GPIO.output(led1,EX_GPIO.HIGH)
        EX_GPIO.output(led2,EX_GPIO.LOW)
        time.sleep(5)
        EX_GPIO.output(led1,EX_GPIO.LOW)
        EX_GPIO.output(led2,EX_GPIO.HIGH)

