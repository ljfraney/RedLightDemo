import RPi.GPIO as GPIO
import time

pinNumber = 23
onSeconds = 2
offSeconds = 1
repeatTimes = 4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pinNumber,GPIO.OUT)

for i in range(0, repeatTimes):
    print(str(i) + ": LED on");
    GPIO.output(pinNumber,GPIO.HIGH)
    time.sleep(onSeconds)
    GPIO.output(pinNumber,GPIO.LOW)
    print(str(i) + ": LED off")
    time.sleep(offSeconds)

print("Goodbye.")
