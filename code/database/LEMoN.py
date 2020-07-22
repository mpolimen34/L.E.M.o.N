from picamera import PiCamera
from time import sleep
import food_predictor

camera=PiCamera()

camera.start_preview()
sleep(5)
camera.capture('images/piImage.jpg')
camera.stop_preview()
print(food_predictor.predict('images/piImage.jpg'))