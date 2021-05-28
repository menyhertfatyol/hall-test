import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
    """
    import FakeRPi.GPIO as GPIO
    OR
    import FakeRPi.RPiO as RPiO
    """

    import FakeRPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
input = GPIO.input(11)

try:
    while True:
        if input:
            print("No magnet")
        else:
            print("Magnet")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
