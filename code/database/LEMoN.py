from picamera import PiCamera
from time import sleep
import food_predictor.py

camera=PiCamera()

camera.start_preview()
sleep(5)
camera.capture('Desktop/piImage.jpg')
camera.stop_preview()
predict('Desktop/piImage.jpg')