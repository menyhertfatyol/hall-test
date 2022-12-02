import time
import importlib.util
try:
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except (RuntimeError, ModuleNotFoundError):
    import fake_rpigpio.utils
    fake_rpigpio.utils.install()

GPIO.VERBOSE = False
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(11):
            print("No magnet")
        else:
            print("Magnet")

        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
