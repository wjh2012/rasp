from picamera import PiCamera

import time

camera = PiCamera()

camera.resolution = (2592, 1944)

time.sleep(2)

camera.capture('example.jpg')