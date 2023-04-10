import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 0.5)
p.start(0)
try:
    while True:
        a = int(input())
        p.start(a)
        

finally:
    GPIO.output(22, 0)
    GPIO.cleanup()