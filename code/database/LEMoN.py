from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import food_predictor
import smbus

bus=smbus.SMBus(1)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
camera=PiCamera()

bus.write_i2c_block_data(0x70,0x00,[0x02])
GPIO.output(7,1)
camera.start_preview()
sleep(5)
camera.capture('images/piImage.jpg')
camera.stop_preview()

bus.write_i2c_block_data(0x70,0x00,[0x01])
GPIO.output(7,0)
camera.start_preview()
sleep(5)
camera.capture('images/piImageNoIR.jpg')
camera.stop_preview()

print(food_predictor.predict('images/piImage.jpg',False))
GPIO.cleanup()