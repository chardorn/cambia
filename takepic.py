import picamera
from time import sleep

camera = picamera.PiCamera()

try:
    camera.start_preview()
    sleep(1)
    camera.capture('image_test.jpg', resize=(500,281))
    camera.stop_preview()
    pass
finally:
    camera.close()
