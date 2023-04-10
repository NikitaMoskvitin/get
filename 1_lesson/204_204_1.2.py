import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.IN)
GPIO.output(22,GPIO.input(23))