import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)

input = GPIO.input(13)
while True:
    if (input):
        print("Locked")