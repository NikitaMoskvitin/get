import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)
def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
def vachiclen(value):
    a = decimal2binary(value)
    k = 0
    for i in range(7):
        k = k + a[i]/(2**(i+1))
    return 3.3*k    
try:
    while 1 > 0:
        a = input()
        if a == "q":
            break
        elif float(a)%1 != 0:
            print("ввели не целое число")
        elif int(a) < 0:
            print("ввели отрицательное число")
        elif int(a) > 255:
            print("Вели число больше 255")
        else:
            GPIO.output(dac, decimal2binary(int(a)))
            print(vachiclen(int(a)))
except ValueError:
    print("Ввели не число")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
