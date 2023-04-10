import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
try:
    T = float(input())
    t = T/512
    while True:
        for i in range(256):
            GPIO.output(dac, decimal2binary(i))
            time.sleep(t)
        for i in range(256):
            GPIO.output(dac, decimal2binary(255-i))
            time.sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()